import pytesseract
from urllib import request
from PIL import Image
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = \
        r"C:\Users\tian.xiaoyi\AppData\Local\Tesseract-OCR\tesseract.exe"
    url = "data:image/jpg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIs" \
          "IxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA" \
          "eAGQDAREAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM" \
          "2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NX" \
          "W19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBC" \
          "SMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tP" \
          "U1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+gAoA4bxz8TbDwTf2thNZXFxczqsmQQqLGWIJzySRg8AfiK9zKsiq5jCVSMkktPO9v61MqlVQdhmu+PrlPGeneGfDdnDqN47B7" \
          "1nYhIYsf3h0OCDnnHAwSeKwmUQeDnjMXJwjtHu36fh/kkEqnvKMSLxj8SZ/CniaHSY9ElvxJbifMTYbGSDgYPTFVluSRxuGdd1FGztrsE6nK7WNbwj8QNG8Yb4rN3hvYxmS1mGHH09a5MxyfEYC0qmsXs1s" \
          "VCopbHV15RYjHCk4zgUIDx1PjoLbUrq0vtCmYQysm+J8EAHHKkV9i+E+enGdOqtV1Of2+tmjuvB/j3S/Gi3H9nw3UbwY3idAOvoQTXh5llFfL7e1ad+xrCop7HU15RYUAFABQAUAeL/ALQdnatpmjXplRbtJni" \
          "WPPzOhGSfoCB/31X2nB1SaqVadvdsn6P/AIP6HNiErJm98GNF06x8GLrETebfXxZrmZ+q7ScJ9O/vn6Y4OJ8VWqYz2D0jHZevUujFKNzkkvfEHiL4r6l4k8P6SmpW9gfscDSyhETAxuyTzzuPHqK9Z0sJhcrhhMVU5HP" \
          "3nZXf9bIzvKU3KKK3izwX4h8O6Xd+N5tT8jW3ulaRbElEijYEHnvztH/661y7NMJiqscujC9NLTm1ba/pinCUVz31L+pfF/UJtA0Gy0Fll1242/aSU3gHptx6ng5+tYUOG6Ua9apidKSvbp8/kU6zslHc9P1fWrjw74Dn1bVG" \
          "j+229oGkCDCmYgAAe24gV8vhsLDFY5UKPwt6en/DGzlyxuzw74f3XjPTLe91fS/DX9qW2otl5ZRw2Cc4555/lX3GcU8urSjQrVuRw6I5qbmtUrnv+gWwj0uC5k0y1sLy4jV7iK3QLhiOhIHOOlfAYyd6rgpuUU7Js6orTY1K5SgoAK" \
          "ACgBrtsjZ8E7RnAGSaaV3YDyG48I6h8QbHW/EGp28kV1MjW+kWswK+QitjcwPQsQf84r6+GY0srnSwtF3itZtdW+i9Dn5HNOT+R1Xw98F3vhfwrNpGq3cdz5zlikJYCMEcqG4J/TrXlZzmlPGYpV6MbW79fOxpTg4xszpNE0DS/DlibLSbR" \
          "ba3LlyisWyx6nJJPYV5uKxlbFz9pXld7FxioqyG+I9JXXfDeo6W2M3MDRqT2bHyn8Dg08FiHhsRCsvstP5dfwFJXTR80eDLHUtMhuvFOlxrNe6FcA3lnKucwsCCw7gja4Pp17Gv0vM6tGs44Os7Rqr3ZLuv6VvuOOCa95dD1Tx7NqfxI8BaX/wi" \
          "Vo13BdTebcjzUQxbB9xtzDnce393PcV8tlEaOU46p9elyuKstG736qy7fmb1L1IrlMjw5pfxf0xdN0pI4rHSoXSNmH2VzHHu+Y9SScEmuvG4jIKznWbcpu7+2rvp2Jiqqsuh7dXxB0hQAUAFABQAUAFABQAUAFAFZdPsknlnWzt1mmXbLIIwGcejHHI" \
          "+taOtUcVFydltrt6CsjF8M+C9N8Iz3h0ma6S2ujva1kcNGjeq8ZHHHU9vSu7HZpWx0Y+3SvHr1t5kxgo7HR15pYUAFABQAUAf/9k1YQ=="
    while True:
        request.urlretrieve(url, 'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)
        
if __name__ == "__main__":
  main()
