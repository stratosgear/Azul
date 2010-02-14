'''
Created on Feb 9, 2010

@author: stratos
'''
import clevercss


if __name__ == '__main__':
  try:
    in_styles = open('styles.clever', 'r')
    out_styles = open('styles.css', 'w')
    out_styles.write(clevercss.convert(in_styles.read()))
    out_styles.close()
    print('styles.css was created.')
  except:
    print('Cannot create styles.css.')
