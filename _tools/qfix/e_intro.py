p = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/articles_maths/introduction-to-the-quaternion-algebra.md'
t = open(p, encoding='utf-8').read()

new1 = ("The quaternion space $\\mathbb{R}^4$ with basis $e_0,e_1,e_2,e_3$ carries the **quaternion product** "
        "$\\tilde p\\tilde q$, the multiplication of the quaternion algebra $\\mathbb{H}$, and that product is the "
        "subject of this article. The article defines it, proves the four algebra axioms for it, and reads off the "
        "classes of element and the structure statements the rest of the block names: bilinearity, associativity, "
        "the two-sided unit $e_0$, the division property, the centre, simplicity and the presentation. It is the "
        "entry point of the block; the norm and the group of units are *Norm and Invertibility in the Quaternion "
        "Algebra*, below this article in this category, and the ideal theory is *Ideals and Simplicity of the "
        "Quaternion Algebra*, below this article in this category.")

new2 = ("The article is short by design. Almost everything that can be said about the quaternion product is an "
        "instance of the general theory of an associative division algebra with unit, and the interest of the "
        "block is that the classes of element are as small as an algebra permits. What is specific to "
        "$\\mathbb{H}$ is the coordinate rule, the sixteen products of the basis, the two generators and the "
        "presentation; these are what is written out. The further products the same space carries — the "
        "symmetrisation, the antisymmetrisation and the product with the conjugation read in the first slot — "
        "belong to the *Quaternioid Algebraic Structures* category and are cited there rather than here.")

i = t.index('The quaternion space')
j = t.index('\n\n', i)
t = t[:i] + new1 + t[j:]
i = t.index('The article is short by design.')
j = t.index('\n\n', i)
t = t[:i] + new2 + t[j:]
open(p, 'w', encoding='utf-8').write(t)
print('ok')
