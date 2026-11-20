#!/usr/bin/env python3
"""Convert a practical subset of cURL commands into JavaScript fetch code."""
import argparse, json, shlex, sys

FLAGS={"-L","--location","-s","--silent","-S","--show-error","-i","--include","--compressed","--fail","--fail-with-body","--globoff","--http1.1","--http2","-k","--insecure"}
VALUE_FLAGS={"-X","--request","-H","--header","-d","--data","--data-raw","--data-binary","--url"}

def parse_curl(command):
    tokens=shlex.split(command)
    if tokens and tokens[0]=="curl": tokens=tokens[1:]
    url=method=body=None; headers={}; i=0
    while i<len(tokens):
        token=tokens[i]
        if token in VALUE_FLAGS:
            if i+1>=len(tokens): raise ValueError(f"Missing value after {token}")
            value=tokens[i+1]; i+=2
            if token in ("-X","--request"): method=value.upper()
            elif token in ("-H","--header"):
                if ":" not in value: raise ValueError(f"Header must contain ':' : {value}")
                key,val=value.split(":",1); headers[key.strip()]=val.strip()
            elif token=="--url": url=value
            else:
                body=value
                if method is None: method="POST"
            continue
        if token in FLAGS or (token.startswith("-") and len(token)>2 and set(token[1:])<=set("sSif")):
            i+=1; continue
        if token.startswith("-"): raise ValueError(f"Unsupported option: {token}")
        if url is None: url=token
        else: raise ValueError(f"Unexpected argument: {token}")
        i+=1
    if not url: raise ValueError("No URL found")
    return {"url":url,"method":method or "GET","headers":headers,"body":body}

def to_fetch(req):
    lines=[f"const response = await fetch({json.dumps(req['url'])}, {{"]
    lines.append(f"  method: {json.dumps(req['method'])},")
    if req["headers"]: lines.append("  headers: "+json.dumps(req["headers"],indent=4)+",")
    if req["body"] is not None: lines.append("  body: "+json.dumps(req["body"])+",")
    lines += ["});","if (!response.ok) throw new Error(`HTTP ${response.status}`);","const data = await response.text();"]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("command",nargs="?")
    a=p.parse_args(); command=a.command if a.command is not None else sys.stdin.read()
    try: print(to_fetch(parse_curl(command.strip())))
    except ValueError as e: p.error(str(e))
if __name__=="__main__": main()
