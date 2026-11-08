"""把 src.html + vendor 库 + logo 合成一个可双击打开的单文件：dist/银行日记账拆分.html"""
import base64, pathlib
d = pathlib.Path(__file__).parent
html = (d / 'src.html').read_text(encoding='utf-8')
libs = '\n'.join((d / 'vendor' / f).read_text(encoding='utf-8') for f in ['xlsx.full.min.js', 'exceljs.min.js', 'jszip.min.js'])
logo = 'data:image/png;base64,' + base64.b64encode((d / 'logo-ink.png').read_bytes()).decode()
html = html.replace('/*LOGO*/', logo).replace('<script>/*VENDOR*/</script>', '<script>' + libs.replace('</script', '<\\/script') + '</script>')
(d / 'dist').mkdir(exist_ok=True)
out = d / 'dist' / '银行日记账拆分.html'
out.write_text(html, encoding='utf-8')
print(out, round(out.stat().st_size / 1e6, 2), 'MB')
(d / 'index.html').write_text(html, encoding='utf-8')   # GitHub Pages 用
