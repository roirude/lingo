/**
 * Reproduces Python 3's `repr()` for a string.
 *
 * The YAML curriculums are written by hand, line by line, and their labels
 * were quoted via `{x!r}` in the original Python version. For the Node port
 * to produce bit-identical files, it needs the same quoting rules:
 *
 *   - single quotes by default;
 *   - double quotes if the string contains an apostrophe and no `"`;
 *   - the chosen delimiter, the backslash, and control characters are
 *     escaped; printable non-ASCII characters are left as-is.
 */
export function pyRepr(s) {
  const quote = s.includes("'") && !s.includes('"') ? '"' : "'";
  let out = quote;
  for (const ch of s) {
    if (ch === '\\') out += '\\\\';
    else if (ch === quote) out += '\\' + ch;
    else if (ch === '\n') out += '\\n';
    else if (ch === '\r') out += '\\r';
    else if (ch === '\t') out += '\\t';
    else if (ch < ' ' || ch === '\x7f') {
      out += '\\x' + ch.codePointAt(0).toString(16).padStart(2, '0');
    } else out += ch;
  }
  return out + quote;
}
