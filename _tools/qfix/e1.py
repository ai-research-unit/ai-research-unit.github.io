p = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/articles_maths/introduction-to-the-quaternion-algebra.md'
t = open(p, encoding='utf-8').read()
i = t.index('## The Other Five Products')
j = t.index('## Summary', i)
new = """## The Companion Products

The quaternion product is one of several products the space $\\mathbb{R}^4$ carries. Taking its symmetric and antisymmetric parts gives the Jordan product and the cross product, and reading the first slot through the conjugation gives the quaternionic product $\\tilde p^{\\natural}\\tilde q$. Those companion products, and the structures they define, are the subject of the *Quaternioid Algebraic Structures* category, which defines them once and owns them; no companion product is re-derived here. What singles out the product of this article is that it is the associative one with a two-sided unit and the division property.

"""
open(p, 'w', encoding='utf-8').write(t[:i] + new + t[j:])
print('done')
