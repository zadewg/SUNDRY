import requests, time

fname = "list.txt"
with open(fname, 'r') as f:
	#array = []
	for line in f:
		comp = str(line).replace(' ', '').replace('\n', '')

		html = requests.get("http://www.formulacionquimica.com/%s/" % comp)
		parse = html.content

		p1i = parse.index('tica:</b>') + 10
		p1f = parse.index('</p><p><b class="tnom">Nomenclatura stock')

		p2i = parse.index("tock:</b>") + 10 
		p2f = parse.index('</p><p><b class="tnom">Nomenclatura tradicional')

		p3i = parse.index("onal:</b>") + 10 
		p3f = parse.index('</p><p><b class="tnom">Tipo de compuesto')

		sistematica = (parse[int(p1i):-(len(parse)- p1f)])
		stock = (parse[int(p2i):-(len(parse)- p2f)])
		tradicional = (parse[int(p3i):-(len(parse)- p3f)])

		print("{}\n{}\n\nSistematica: {}\nStock: {}\nTradicional: {}\n".format("="*47,comp, sistematica, stock, tradicional )) 
                time.sleep(1)
