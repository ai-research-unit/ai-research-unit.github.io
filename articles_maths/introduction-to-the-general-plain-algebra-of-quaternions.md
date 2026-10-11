# __Introduction to the General Plain Algebra of Quaternions__

## Introduction

The quaternion space $\mathbb{R}^4$, with basis $e_0,e_1,e_2,e_3$ and a bilinear product, carries six products; the present one is the **general plain product** $\tilde p\tilde q$, the multiplication of the quaternion algebra $\mathbb{H}$. This article defines that product, proves the four algebra axioms for it, and reads off the four classes of element and the two structure statements that the rest of the block can name: bilinearity, associativity, the two-sided unit $e_0$, the division property, the centre, simplicity and the presentation. It is the entry point of the block; the norm and the group of units are *Norm and Invertibility in the General Plain Algebra*, below this article in this category, the ideal theory is *Ideals and Simplicity of the General Plain Algebra*, below this article in this category, and the remaining five products are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, above this article in this category, which owns the family and is cited here rather than restated.

The article is short by design. Almost everything that can be said about the plain product is an instance of the general theory of an associative division algebra with unit, and the interest of the block is that the classes of element are as small as an algebra permits. What is specific to $\mathbb{H}$ is the coordinate rule, the sixteen products of the basis, the two generators and the presentation; these are what is written out.

## The Product in Coordinates

**Definition.** On $\mathbb{R}^4$ with basis $e_0,e_1,e_2,e_3$ the **general plain product** of $\tilde p=\sum_\mu p_\mu e_\mu$ and $\tilde q=\sum_\nu q_\nu e_\nu$ is the bilinear extension of the rules

$$
e_0e_0=e_0,\qquad e_0e_k=e_ke_0=e_k,\qquad e_k^2=-e_0\quad(k=1,2,3),
$$

$$
e_1e_2=e_3=-e_2e_1,\qquad e_2e_3=e_1=-e_3e_2,\qquad e_3e_1=e_2=-e_1e_3 .
$$

The resulting algebra is written $\mathbb{H}$ and called the **quaternion algebra**; its elements are quaternions and its product is the plain product of the block.

**Proposition (the coordinate rule).** The product is well defined by the rules above and is given on coordinates by

$$
\begin{aligned}
(\tilde p\tilde q)_0 &= p_0q_0-p_1q_1-p_2q_2-p_3q_3,\\
(\tilde p\tilde q)_1 &= p_0q_1+p_1q_0+p_2q_3-p_3q_2,\\
(\tilde p\tilde q)_2 &= p_0q_2-p_1q_3+p_2q_0+p_3q_1,\\
(\tilde p\tilde q)_3 &= p_0q_3+p_1q_2-p_2q_1+p_3q_0 .
\end{aligned}
$$

*Proof.* The rules determine the product of every pair of basis elements and hence, by bilinearity, the product of every pair of elements; this is the well-definedness. Expanding $\bigl(\sum_\mu p_\mu e_\mu\bigr)\bigl(\sum_\nu q_\nu e_\nu\bigr)$ with the basis rules and collecting the four coordinates gives the displayed formulas.

**Theorem (the sixteen products).** The products of the basis elements are

| | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

*Proof.* Read the definition: $e_k^2=-e_0$ is the diagonal of the imaginary block, and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$ with the three reversed products negated are the off-diagonal entries.

**Corollary.** The product is bilinear, and it is determined by its values on the sixteen basis pairs: a bilinear product on $\mathbb{R}^4$ is the same datum as a table of sixteen products of basis elements.

## The Algebra Axioms

**Theorem (associativity).** $(\tilde p\tilde q)\tilde r=\tilde p(\tilde q\tilde r)$ for all $\tilde p,\tilde q,\tilde r\in\mathbb{H}$.

*Proof.* Let $L_{\tilde a}$ be the left multiplication $\tilde x\mapsto\tilde a\tilde x$, a linear map of $\mathbb{R}^4$. In the basis $e_0,e_1,e_2,e_3$ the maps

$$
L_{e_1}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
L_{e_2}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

satisfy $L_{e_1}^2=L_{e_2}^2=-\mathrm I_4$ and $L_{e_1}L_{e_2}=-L_{e_2}L_{e_1}$, as a direct matrix computation shows; set $L_{e_3}=L_{e_1}L_{e_2}$ and $L_{e_0}=\mathrm I_4$. Since $L$ is additive in its subscript and $\{e_\mu\}$ is a basis, the assignment $\tilde a\mapsto L_{\tilde a}$ is linear; and it is multiplicative on the basis: $L_{e_1e_1}=L_{-e_0}=-\mathrm I_4=L_{e_1}^2$, likewise for $e_2$, and $L_{e_1e_2}=L_{e_3}=L_{e_1}L_{e_2}$, $L_{e_2e_1}=-L_{e_3}=L_{e_2}L_{e_1}$. Every product of basis elements is a word in $e_1,e_2$ with a sign, so linearity propagates the four checks to $L_{\tilde p\tilde q}=L_{\tilde p}L_{\tilde q}$ for all $\tilde p,\tilde q$. Applying both sides to $\tilde r$ gives the associativity.

**Theorem (the unit).** $e_0$ is a two-sided unit: $e_0\tilde q=\tilde qe_0=\tilde q$.

*Proof.* The first row and the first column of the table.

**Proposition (non-commutativity).** $\mathbb{H}$ is not commutative: $e_1e_2=e_3$ while $e_2e_1=-e_3$.

*Proof.* The table.

## The Division Property

**Theorem.** Every non-zero quaternion is invertible: for $\tilde q\neq0$ there is $\tilde q^{-1}$ with $\tilde q\tilde q^{-1}=\tilde q^{-1}\tilde q=e_0$.

*Proof.* The conjugate is $\tilde q^{\natural}=q_0e_0-q_1e_1-q_2e_2-q_3e_3$ and the quaternion norm is $N(\tilde q)=\tilde q\tilde q^{\natural}=\tilde q^{\natural}\tilde q=\sum_\mu q_\mu^2$. For $\tilde q\neq0$ the norm is a positive real, and the inverse is $\tilde q^{-1}=\tilde q^{\natural}/N(\tilde q)$; both products are $e_0$. The norm, its multiplicativity and the full invertibility criterion are *Norm and Invertibility in the General Plain Algebra*, below this article in this category.

**Corollary.** $\mathbb{H}$ has no zero divisor and no non-zero nilpotent: $\tilde p\tilde q=0$ forces $\tilde p=0$ or $\tilde q=0$, and $\tilde a^2=0$ forces $\tilde a=0$.

*Proof.* If $\tilde p\tilde q=0$ with $\tilde q\neq0$, multiply on the right by $\tilde q^{-1}$; then $\tilde p=0$. For the nilpotent, $\tilde a^2=0$ and $\tilde a\neq0$ would exhibit $\tilde a$ as a zero divisor with itself.

**Theorem (the idempotents).** The idempotents of the plain product are exactly $0$ and $e_0$.

*Proof.* If $\tilde a^2=\tilde a$ then $\tilde a(\tilde a-e_0)=0$, and by the corollary $\tilde a=0$ or $\tilde a=e_0$; both are idempotent.

The classes of element of $\mathbb{H}$ are therefore as small as an associative algebra permits: the zero divisors, the non-zero nilpotents and the nontrivial idempotents are all absent, and the root sets are computed in *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, below this article in this category. The folding of these empty classes into the present block is deliberate, and it is the point of *The Specificities of the General Plain Algebra*, below this article in this category.

## The Centre and Simplicity

**Theorem (the centre).** The centre of $\mathbb{H}$ is the scalar line $\mathbb{R}e_0$.

*Proof.* If $\tilde a$ commutes with $e_1,e_2,e_3$ then $\tilde a$ has zero vector part: commuting with $e_1$ forces $a_2=a_3=0$ and commuting with $e_2$ forces $a_1=0$. Every scalar commutes with every element.

**Theorem (simplicity).** $\mathbb{H}$ has no proper non-zero two-sided ideal, and it is a central simple $\mathbb{R}$-algebra of degree two, $\dim_\mathbb{R}\mathbb{H}=4=2^2$.

*Proof.* A two-sided ideal that contains a non-zero element contains a unit, hence the whole algebra; the centre is $\mathbb{R}e_0$ by the theorem above. The statements, the comparison with the complex and split cases, and the Brauer class are *Ideals and Simplicity of the General Plain Algebra*, below this article in this category.

## Generators and Presentation

**Theorem.** The elements $e_1,e_2$ generate $\mathbb{H}$ as an $\mathbb{R}$-algebra: $e_3=e_1e_2$, and every element is an $\mathbb{R}$-linear combination of $e_0,e_1,e_2,e_1e_2$.

**Theorem (the presentation).** The algebra $\mathbb{H}$ is presented by two generators and the relations

$$
\mathbb{H}\;\cong\;\bigl\langle\, e_1,e_2\;\bigm|\; e_1^2=e_2^2=(e_1e_2)^2=-e_0\,\bigr\rangle ,
$$

the relations meaning $e_1^2=e_2^2=-e_0$ and $e_1e_2=-e_2e_1$.

*Proof.* The three relations are the table. For the converse, the free associative algebra on two generators modulo the relations is spanned by the words in $e_1,e_2$; the relations reduce a word to a normal form $\sum a_{mn}e_1^me_2^n$ with $m,n\in\{0,1\}$, hence to $\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_1e_2$, and the four classes are linearly independent because their images $e_0,e_1,e_2,e_3$ are. So the presented algebra has dimension four, contains $\mathbb{H}$, and equals it.

**Theorem (the one-generator subalgebra).** For a non-real $\tilde a$ the subalgebra $\mathbb{R}[\tilde a]$ generated by $\tilde a$ is isomorphic to $\mathbb{C}$; for $\tilde a$ real it is $\mathbb{R}$.

*Proof.* A non-real quaternion has non-zero vector part, and its vector part spans, with $e_0$, a two-dimensional subspace closed under the product, on which the multiplication is that of $\mathbb{C}$ with imaginary unit $\tilde\xi=\mathbf a/|\mathbf a|$ satisfying $\tilde\xi^2=-e_0$; the isomorphism sends $\tilde\xi$ to $i$. For real $\tilde a$ the generated algebra is the real line.

## The Other Five Products

The six products of the quaternion space — the general plain product above, its symmetrisation and antisymmetrisation, and the three products built with the natural conjugation in the first slot — are defined once in *The 6 Products of the Quaternion $\mathbb{R}$ Space* and classified in *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, above this article in this category. The present block reads the first of the six; the other five have their own blocks, and no product is re-derived here. What the plain product contributes to the family is the two-sided unit, the associativity and the division property, and it is the only one of the six that has all three.

## Summary

The general plain product on $\mathbb{R}^4$ is defined by the basis rules $e_k^2=-e_0$, $e_1e_2=e_3=-e_2e_1$ and their cyclic companions; it is bilinear, determined by its sixteen basis products, associative, non-commutative, and carries the two-sided unit $e_0$. It gives the division algebra $\mathbb{H}$: every non-zero element is invertible with $\tilde q^{-1}=\tilde q^{\natural}/N(\tilde q)$, so there is no zero divisor, no non-zero nilpotent and no idempotent but $0$ and $e_0$. The centre is the scalar line $\mathbb{R}e_0$, the algebra is central simple of degree two, the generators $e_1,e_2$ present it by $e_1^2=e_2^2=(e_1e_2)^2=-e_0$, and the subalgebra generated by a single non-real element is a copy of $\mathbb{C}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, $\mathbb{R}^4$ with the general plain product |
| $e_0,e_1,e_2,e_3$ | Basis, $e_0$ the unit, $e_k^2=-e_0$ |
| $\tilde p\tilde q$ | The general plain product |
| $\tilde q^{\natural}=q_0e_0-q_1e_1-q_2e_2-q_3e_3$ | The natural sign, the quaternion conjugation |
| $N(\tilde q)=\tilde q\tilde q^{\natural}=\sum_\mu q_\mu^2$ | The quaternion norm, from *Norm and Invertibility in the General Plain Algebra*, below this article in this category |
| $L_{\tilde a}$ | Left multiplication $\tilde x\mapsto\tilde a\tilde x$ |
| $\mathbb{R}[\tilde a]$ | Subalgebra generated by $\tilde a$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the product and the basis rules.
- Leonard Dickson, *Algebras and Their Arithmetics* (University of Chicago Press, 1923), for the presentation of the quaternion algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the algebra axioms and the structure of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for division rings, their centre and their simplicity.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion multiplication and its generators.
