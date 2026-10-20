def longestCommonPrefix(str: list[str]) -> str:
    if not str:
        return ""
    str.sort()
    first=str[0]
    last=str[-1]

    ans=[]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return"".join(ans)
        ans.append(first[i])
        return"".join(ans)