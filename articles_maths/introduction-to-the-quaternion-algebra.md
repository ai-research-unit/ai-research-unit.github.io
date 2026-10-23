# __Introduction to the Quaternion Algebra__

## Introduction

The quaternion algebra $\mathbb{H}$ is the space $\mathbb{R}^4$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ under the **quaternion product** $\tilde q_1\tilde q_2$, the multiplication of the algebra. This article defines that product, proves the four algebra axioms for it, and reads off the four classes of element and the two structure statements that the rest of the block can name: bilinearity, associativity, the two-sided unit $e_t$, the division property, the centre, simplicity and the presentation. It is the entry point of the block; the norm and the group of units are *Norm and Invertibility in the Quaternion Algebra*, below this article in this category, and the ideal theory is *Ideals and Simplicity of the Quaternion Algebra*, below this article in this category.

The article is short by design. Almost everything that can be said about the quaternion product is an instance of the general theory of an associative division algebra with unit, and the interest of the block is that the classes of element are as small as an algebra permits. What is specific to $\mathbb{H}$ is the coordinate rule, the sixteen products of the basis, the two generators and the presentation; these are what is written out.

## The Product in Coordinates

**Definition.** On $\mathbb{R}^4$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the **quaternion product** of $\tilde q_1=\sum_\mu q_{1\mu} e_\mu$ and $\tilde q_2=\sum_\nu q_{2\nu} e_\nu$ is the bilinear extension of the rules

$$
e_t e_t=e_t,\qquad e_t \vec e_k=\vec e_k e_t=\vec e_k,\qquad \vec e_k^2=-e_t\quad(k=1,2,3),
$$

$$
\vec e_x \vec e_y=\vec e_z=-\vec e_y \vec e_x,\qquad \vec e_y \vec e_z=\vec e_x=-\vec e_z \vec e_y,\qquad \vec e_z \vec e_x=\vec e_y=-\vec e_x \vec e_z.
$$

The resulting algebra is written $\mathbb{H}$ and called the **quaternion algebra**; its elements are quaternions and its product is the quaternion product of the block.

**Proposition (the coordinate rule).** The product is well defined by the rules above and is given on coordinates by

$$
\boxed{\;
\begin{aligned}
(\tilde q_1\tilde q_2)_t &= q_{1t}q_{2t}-q_{1x}q_{2x}-q_{1y}q_{2y}-q_{1z}q_{2z},\\
(\tilde q_1\tilde q_2)_x &= q_{1t}q_{2x}+q_{1x}q_{2t}+q_{1y}q_{2z}-q_{1z}q_{2y},\\
(\tilde q_1\tilde q_2)_y &= q_{1t}q_{2y}-q_{1x}q_{2z}+q_{1y}q_{2t}+q_{1z}q_{2x},\\
(\tilde q_1\tilde q_2)_z &= q_{1t}q_{2z}+q_{1x}q_{2y}-q_{1y}q_{2x}+q_{1z}q_{2t}.
\end{aligned}
\;}
$$

*Proof.* The rules determine the product of every pair of basis elements and hence, by bilinearity, the product of every pair of elements; this is the well-definedness. Expanding $\bigl(\sum_\mu q_{1\mu} e_\mu\bigr)\bigl(\sum_\nu q_{2\nu} e_\nu\bigr)$ with the basis rules and collecting the four coordinates gives the displayed formulas.

**Theorem (the sixteen products).** The products of the basis elements are

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

*Proof.* Read the definition: $\vec e_k^2=-e_t$ is the diagonal of the imaginary block, and $\vec e_x \vec e_y=\vec e_z$, $\vec e_y \vec e_z=\vec e_x$, $\vec e_z \vec e_x=\vec e_y$ with the three reversed products negated are the off-diagonal entries.

**Corollary.** The product is bilinear, and it is determined by its values on the sixteen basis pairs: a bilinear product on $\mathbb{R}^4$ is the same datum as a table of sixteen products of basis elements.

## The Algebra Axioms

**Theorem (associativity).** $(\tilde q_1\tilde q_2)\tilde q_3=\tilde q_1(\tilde q_2\tilde q_3)$ for all $\tilde q_1,\tilde q_2,\tilde q_3\in\mathbb{H}$.

*Proof.* Let $L_{\tilde q_4}$ be the left multiplication $\tilde q\mapsto\tilde q_4\tilde q$, a linear map of $\mathbb{R}^4$. In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the maps

$$
L_{\vec e_x}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
L_{\vec e_y}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}
$$

satisfy $L_{\vec e_x}^2=L_{\vec e_y}^2=-\mathrm I_4$ and $L_{\vec e_x}L_{\vec e_y}=-L_{\vec e_y}L_{\vec e_x}$, as a direct matrix computation shows; set $L_{\vec e_z}=L_{\vec e_x}L_{\vec e_y}$ and $L_{e_t}=\mathrm I_4$. Since $L$ is additive in its subscript and $\{e_\mu\}$ is a basis, the assignment $\tilde q_4\mapsto L_{\tilde q_4}$ is linear; and it is multiplicative on the basis: $L_{\vec e_x \vec e_x}=L_{-e_t}=-\mathrm I_4=L_{\vec e_x}^2$, likewise for $\vec e_y$, and $L_{\vec e_x \vec e_y}=L_{\vec e_z}=L_{\vec e_x}L_{\vec e_y}$, $L_{\vec e_y \vec e_x}=-L_{\vec e_z}=L_{\vec e_y}L_{\vec e_x}$. Every product of basis elements is a word in $\vec e_x,\vec e_y$ with a sign, so linearity propagates the four checks to $L_{\tilde q_1\tilde q_2}=L_{\tilde q_1}L_{\tilde q_2}$ for all $\tilde q_1,\tilde q_2$. Applying both sides to $\tilde q_3$ gives the associativity.

**Theorem (the unit).** $e_t$ is a two-sided unit: $e_t\tilde q=\tilde qe_t=\tilde q$.

*Proof.* The first row and the first column of the table.

**Proposition (non-commutativity).** $\mathbb{H}$ is not commutative: $\vec e_x \vec e_y=\vec e_z$ while $\vec e_y \vec e_x=-\vec e_z$.

*Proof.* The table.

## The Division Property

**Theorem.** Every non-zero quaternion is invertible: for $\tilde q\neq0$ there is $\tilde q^{-1}$ with $\tilde q\tilde q^{-1}=\tilde q^{-1}\tilde q=e_t$.

*Proof.* The conjugate is $\tilde q^{\natural}=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$ and the quaternion norm is $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=\tilde q^{\natural}\tilde q=\sum_\mu q_\mu^2$. For $\tilde q\neq0$ the norm is a positive real, and the inverse is $\tilde q^{-1}=\tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$; both products are $e_t$. The norm, its multiplicativity and the full invertibility criterion are *Norm and Invertibility in the Quaternion Algebra*, below this article in this category.

**Corollary.** $\mathbb{H}$ has no zero divisor and no non-zero nilpotent: $\tilde q_1\tilde q_2=0$ forces $\tilde q_1=0$ or $\tilde q_2=0$, and $\tilde q_3^2=0$ forces $\tilde q_3=0$.

*Proof.* If $\tilde q_1\tilde q_2=0$ with $\tilde q_2\neq0$, multiply on the right by $\tilde q_2^{-1}$; then $\tilde q_1=0$. For the nilpotent, $\tilde q_3^2=0$ and $\tilde q_3\neq0$ would exhibit $\tilde q_3$ as a zero divisor with itself.

**Theorem (the idempotents).** The idempotents of the quaternion product are exactly $0$ and $e_t$.

*Proof.* If $\tilde q^2=\tilde q$ then $\tilde q(\tilde q-e_t)=0$, and by the corollary $\tilde q=0$ or $\tilde q=e_t$; both are idempotent.

The classes of element of $\mathbb{H}$ are therefore as small as an associative algebra permits: the zero divisors, the non-zero nilpotents and the nontrivial idempotents are all absent, and the root sets are computed in *Square Roots of Minus One, Zero and Plus One in the Quaternion Algebra*, below this article in this category. The folding of these empty classes into the present block is deliberate, and it is the point of *The Specificities of the Quaternion Algebra*, below this article in this category.

## The Centre and Simplicity

**Theorem (the centre).** The centre of $\mathbb{H}$ is the scalar line $\mathbb{R}e_t$.

*Proof.* If $\tilde q$ commutes with $\vec e_x,\vec e_y,\vec e_z$ then $\tilde q$ has zero vector part: commuting with $\vec e_x$ forces $q_y=q_z=0$ and commuting with $\vec e_y$ forces $q_x=0$. Every scalar commutes with every element.

**Theorem (simplicity).** $\mathbb{H}$ has no proper non-zero two-sided ideal, and it is a central simple $\mathbb{R}$-algebra of degree two, $\dim_\mathbb{R}\mathbb{H}=4=2^2$.

*Proof.* A two-sided ideal that contains a non-zero element contains a unit, hence the whole algebra; the centre is $\mathbb{R}e_t$ by the theorem above. The statements, the comparison with the complex and split cases, and the Brauer class are *Ideals and Simplicity of the Quaternion Algebra*, below this article in this category.

## Generators and Presentation

**Theorem.** The elements $\vec e_x,\vec e_y$ generate $\mathbb{H}$ as an $\mathbb{R}$-algebra: $\vec e_z=\vec e_x \vec e_y$, and every element is an $\mathbb{R}$-linear combination of $e_t,\vec e_x,\vec e_y,\vec e_x \vec e_y$.

**Theorem (the presentation).** The algebra $\mathbb{H}$ is presented by two generators and the relations

$$
\boxed{\;
\mathbb{H}\;\cong\;\bigl\langle\, \vec e_x,\vec e_y\;\bigm|\; \vec e_x^2=\vec e_y^2=(\vec e_x \vec e_y)^2=-e_t\,\bigr\rangle
\;},
$$

the relations meaning $\vec e_x^2=\vec e_y^2=-e_t$ and $\vec e_x \vec e_y=-\vec e_y \vec e_x$.

*Proof.* The three relations are the table. For the converse, the free associative algebra on two generators modulo the relations is spanned by the words in $\vec e_x,\vec e_y$; the relations reduce a word to a normal form $\sum a_{mn}\vec e_x^m\vec e_y^n$ with $m,n\in\{0,1\}$, hence to $\mathbb{R}e_t+\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_x \vec e_y$, and the four classes are linearly independent because their images $e_t,\vec e_x,\vec e_y,\vec e_z$ are. So the presented algebra has dimension four, contains $\mathbb{H}$, and equals it.

**Theorem (the one-generator subalgebra).** For a non-real $\tilde q$ the subalgebra $\mathbb{R}[\tilde q]$ generated by $\tilde q$ is isomorphic to $\mathbb{C}$; for $\tilde q$ real it is $\mathbb{R}$.

*Proof.* A non-real quaternion has non-zero vector part, and its vector part spans, with $e_t$, a two-dimensional subspace closed under the product, on which the multiplication is that of $\mathbb{C}$ with imaginary unit $\tilde\xi=\vec q/|\vec q|$ satisfying $\tilde\xi^2=-e_t$; the isomorphism sends $\tilde\xi$ to $i$. For real $\tilde q$ the generated algebra is the real line.

## Summary

The quaternion product on $\mathbb{R}^4$ is defined by the basis rules $\vec e_k^2=-e_t$, $\vec e_x \vec e_y=\vec e_z=-\vec e_y \vec e_x$ and their cyclic companions; it is bilinear, determined by its sixteen basis products, associative, non-commutative, and carries the two-sided unit $e_t$. It gives the division algebra $\mathbb{H}$: every non-zero element is invertible with $\tilde q^{-1}=\tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$, so there is no zero divisor, no non-zero nilpotent and no idempotent but $0$ and $e_t$. The centre is the scalar line $\mathbb{R}e_t$, the algebra is central simple of degree two, the generators $\vec e_x,\vec e_y$ present it by $\vec e_x^2=\vec e_y^2=(\vec e_x \vec e_y)^2=-e_t$, and the subalgebra generated by a single non-real element is a copy of $\mathbb{C}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, $\mathbb{R}^4$ with the quaternion product |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Basis, $e_t$ the unit, $\vec e_k^2=-e_t$ |
| $\tilde q_1\tilde q_2$ | The quaternion product |
| $\tilde q^{\natural}=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$ | The natural sign, the quaternion conjugation |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=\sum_\mu q_\mu^2$ | The quaternion norm, from *Norm and Invertibility in the Quaternion Algebra*, below this article in this category |
| $L_{\tilde q_4}$ | Left multiplication $\tilde q\mapsto\tilde q_4\tilde q$ |
| $\mathbb{R}[\tilde q]$ | Subalgebra generated by $\tilde q$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the product and the basis rules.
- Leonard Dickson, *Algebras and Their Arithmetics* (University of Chicago Press, 1923), for the presentation of the quaternion algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the algebra axioms and the structure of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for division rings, their centre and their simplicity.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion multiplication and its generators.
