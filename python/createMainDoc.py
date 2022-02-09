
def inject_into_template(
  output_file,
  string,
  template='tex/doc.tex.template',
  replacement_char='###'
):
  with open(template) as file:
    content = file.read().replace(replacement_char, string)
  
  with open(output_file, 'w') as file:
    file.write(content)

def generateDoc(filename, items):
  if items == '':
    itemMap = {
      5: True,
      4: True,
      3: True,
      2: True,
      1: True,
    }
  else:
    itemMap = {
      5: '5' in items,
      4: '4' in items,
      3: '3' in items,
      2: '2' in items,
      1: '1' in items,
    }
  
  innerContent = '\n'.join(f'\\input{{texdata/n{n}.tex}}' for n,v in itemMap.items() if v)
  inject_into_template(filename, innerContent)
    
if __name__ == "__main__":

  def inner(n):
    return f"""
    \\NXinnerpage{{{n}}}
    \\input{{texdata/n{n}.tex}}
    """
  inject_into_template('build/main.tex', f"""
    \\fullFrontpage{{}}
    {inner(5)}
    {inner(4)}
    {inner(3)}
    {inner(2)}
    {inner(1)}
  """)

  for n in range(1,6):
    inject_into_template(f'build/n{n}.tex', f"""
      \\NXfrontpage{{{n}}}
      \\input{{texdata/n{n}.tex}}
    """)