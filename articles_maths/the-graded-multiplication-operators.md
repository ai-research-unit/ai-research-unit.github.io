# __The Graded Multiplication Operators__

## Introduction

A Clifford algebra is not merely an algebra; it is a **graded** algebra, written as the direct sum of its even part and its odd part, with the parts multiplying according to the addition of parities. Every operator on it therefore has a parity of its own, and every statement about operators has a graded and an ungraded form that differ by a sign. The multiplication operators are the simplest place where the two forms are visible: the left multiplication by an element of parity $|x|$ shifts the grading by $|x|$, and the left and the right multiplications, which always commute as ordinary operators, have a graded commutator that vanishes unless both elements are odd.

This article fixes the graded operators. The **signed multiplication operators** are the multiplication operators twisted by the grade involution: the left multiplication by $\alpha(x) = (-1)^{|x|}x$ instead of by $x$, and likewise on the right. They are not new operators – each is the conjugate of an ordinary multiplication by the parity operator $\Gamma(y) = \alpha(y)$, and this is the precise sense in which the sign is a twist of the grading rather than a second structure. The sign rule of the graded commutator then explains why the signed member of the two-sided family is the one that sees the odd part, which is the reason the group of this article exists.

The Clifford algebra, its grading and its three intrinsic involutions are *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*; the grading and the reason the signed member is not a second structure are *The Grading of the Clifford Algebra with Signed Inner Conjugation*; the one-sided operators and their composition are *One-Sided Operators on a Clifford Algebra*; the signed inner conjugation itself is *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*. Those are cited; this article adds the parity of an operator, the twisting by the grade involution, the graded commutator, and the super-structure that organises them. The base is a field $F$ of characteristic not $2$ and $q$ is non-degenerate.

## The Grading and the Parity of an Operator

**Definition.** The **grading** of the Clifford algebra is the decomposition $\mathrm{Cl}(V,q) = \mathrm{Cl}^{0}(V,q)\oplus\mathrm{Cl}^{1}(V,q)$ into the spans of the products of an even and of an odd number of vectors; it satisfies $\mathrm{Cl}^{i}\mathrm{Cl}^{j}\subseteq\mathrm{Cl}^{i+j}$, so the algebra is a $\mathbb{Z}/2$-graded algebra. The **grade involution** is the automorphism $\alpha$ with $\alpha(y) = (-1)^{i}y$ on $\mathrm{Cl}^{i}$; it is the parity operator of the graded algebra.

**Definition.** A linear operator $T$ on the graded vector space $\mathrm{Cl}(V,q)$ is **even** when $T(\mathrm{Cl}^{i}) \subseteq \mathrm{Cl}^{i}$ and **odd** when $T(\mathrm{Cl}^{i}) \subseteq \mathrm{Cl}^{i+1}$; it is **graded**, or homogeneous of parity $|T|$, when it is one of the two. The **graded commutator** of two homogeneous operators is

$$
[T, U\} = TU - (-1)^{|T||U|}UT .
$$

**Proposition.** For a homogeneous element $x$ the left multiplication $L_x$ and the right multiplication $R_x$ are homogeneous operators of parity $|x|$:

$$
L_x(\mathrm{Cl}^{i}) \subseteq \mathrm{Cl}^{i + |x|}, \qquad R_x(\mathrm{Cl}^{i}) \subseteq \mathrm{Cl}^{i + |x|} .
$$

**Proof.** $L_x(y) = xy$ lies in $\mathrm{Cl}^{|x|+i}$ for $y \in \mathrm{Cl}^{i}$ because the product adds the parities; the same computation on the right.

**Proposition (the graded commutators of the multiplication operators).** For homogeneous $x$ and $y$,

$$
[L_x, R_y\} = \bigl(1 - (-1)^{|x||y|}\bigr)L_{xy} , \qquad [L_x, L_y\} = L_{xy - (-1)^{|x||y|}yx} , \qquad [R_x, R_y\} = R_{yx - (-1)^{|x||y|}xy} .
$$

In particular the left and the right families commute as ordinary operators, $L_xR_y = R_yL_x = L_{xy}$; their graded commutator $[L_x,R_y\}$ vanishes when a factor is even and equals $2L_{xy}$ when both elements are odd; and the graded commutator $[L_x,L_y\}$ vanishes exactly when $xy = (-1)^{|x||y|}yx$, which holds for two orthogonal vectors but not for two general even elements, the even part of a Clifford algebra being a Clifford algebra in its own right.

**Proof.** $L_xL_y = L_{xy}$ and $R_xR_y = R_{yx}$ are the multiplicativity of the left family and the anti-multiplicativity of the right family; $L_xR_y = R_yL_x = L_{xy}$ because both operators send $z$ to $xzy$. Substituting into $[T,U\} = TU - (-1)^{|T||U|}UT$ gives the three displays, the factor $1 - (-1)^{|x||y|}$ being zero unless $|x| = |y| = 1$, when it is $2$; and $L_{xy - (-1)^{|x||y|}yx} = 0$ is equivalent to $xy = (-1)^{|x||y|}yx$ because the left family is faithful, $L_z(1) = z$. The Clifford algebra is graded commutative exactly when that relation holds for all homogeneous pairs, which is the degenerate case named below.

**Corollary (the sign rule for the signed family).** For homogeneous $x$ and $y$ the signed families satisfy

$$
[\Lambda^{\alpha}_x, \Lambda^{\alpha}_y\} = \varepsilon_x\varepsilon_y\,[L_x, L_y\} , \qquad [\Lambda^{\alpha}_x, \mathrm{P}^{\alpha}_y\} = \varepsilon_x\varepsilon_y\,[L_x, R_y\} ,
$$

so the graded commutators of the signed family are the graded commutators of the ordinary family rescaled by the two signs, and they vanish under exactly the same conditions.

**Proof.** $\Lambda^{\alpha}_x = \varepsilon_xL_x$ and $\mathrm{P}^{\alpha}_y = \varepsilon_yR_y$ with $\varepsilon_x, \varepsilon_y$ real scalars of modulus one, and $|\Lambda^{\alpha}_x| = |x|$, $|\mathrm{P}^{\alpha}_y| = |y|$, so the rescaled operators have the same parities and the graded commutator is bilinear.

**Remark (the ordinary bracket against the graded bracket).** The two families commute as operators, so the ordinary bracket $[L_x,R_y] = 0$ carries no information; the graded bracket is zero when a factor is even and is $2L_{xy}$ for two odd factors, so it is the bracket that detects the parity. This is the reason the statements of the signed family are stated with the graded bracket and not with the ordinary one.

## The Signed Multiplication Operators

**Definition.** For $x \in \mathrm{Cl}(V,q)$ the **signed left multiplication** and the **signed right multiplication** are

$$
\Lambda^{\alpha}_x(y) = \alpha(x)\,y, \qquad \mathrm{P}^{\alpha}_x(y) = y\,\alpha(x) .
$$

They are the multiplication operators twisted by the grade involution: on a homogeneous $x$ they are $\Lambda^{\alpha}_x = (-1)^{|x|}L_x$ and $\mathrm{P}^{\alpha}_x = (-1)^{|x|}R_x$.

**Proposition (the twisting).** Let $\Gamma$ be the parity operator, $\Gamma(y) = \alpha(y)$. Then $\Gamma$ is an involutive operator on the Clifford algebra, and for every $x$

$$
\Gamma\, L_x\, \Gamma = L_{\alpha(x)}, \qquad \Gamma\, R_x\, \Gamma = R_{\alpha(x)} .
$$

So the signed multiplication operators are the conjugates of the ordinary ones by the parity operator, and twisting by the grading is exactly passing from the ordinary family to the signed family.

**Proof.** $\Gamma^{2} = \mathrm{id}$ because $\alpha$ is an involution; for every $z$, $\Gamma L_x\Gamma(z) = \alpha\bigl(x\,\alpha(z)\bigr) = \alpha(x)\alpha^{2}(z) = \alpha(x)z = \Lambda^{\alpha}_x(z)$, using that $\alpha$ is an algebra automorphism. The right-handed identity is the same computation with the product on the other side.

**Proposition (composition).** The signed families compose by

$$
\Lambda^{\alpha}_x \circ \Lambda^{\alpha}_z = \Lambda^{\alpha}_{x z}, \qquad \mathrm{P}^{\alpha}_x \circ \mathrm{P}^{\alpha}_z = \mathrm{P}^{\alpha}_{z x} ,
$$

so the signed left family is multiplicative in the written order, exactly like the ordinary left family, and the signed right family is anti-multiplicative, exactly like the ordinary right family; the twisting does not change the order.

**Proof.** Both identities are the computation $\Gamma L_x\Gamma\,\Gamma L_z\Gamma = \Gamma L_{xz}\Gamma$ and the right-handed analogue.

**Remark (why the signed left multiplication is the useful one).** The signed left multiplication by a vector $u$ is $\Lambda^{\alpha}_u(y) = -uy$, and its composition with the inverse of the other factor produces the reflection. Heuristically the sign flips the direction of an odd factor and turns the conjugation into a reflection; the precise statement is the reflection formula of *Two-Sided Operators with the Signed Product* and *The Sandwich with the Signed Product*.

## The Super-Structure

**Definition.** A **superalgebra** is an associative algebra with a $\mathbb{Z}/2$-grading for which the product is graded; it is **graded commutative** when $xy = (-1)^{|x||y|}yx$ for homogeneous elements. A Clifford algebra is a superalgebra, and it is graded commutative only in the degenerate cases, its even part being a Clifford algebra in its own right.

**Definition.** The **super-commutant** of a set of homogeneous operators $\mathcal{S}$ is the set of homogeneous operators $T$ with $[T, U\} = 0$ for every $U \in \mathcal{S}$. The **supercentre** of the algebra is the super-commutant of the multiplication operators inside the algebra.

**Proposition.** The supercentre of the Clifford algebra is the centre, $Z(\mathrm{Cl}(V,q))$, and the super-commutant of the left multiplications is

$$
\{L_x : x \in \mathrm{Cl}(V,q)\}^{\mathrm{s}} = \{\, R_y : y \in \mathrm{Cl}^{0}(V,q) \,\} \oplus \{\, \Gamma R_y : y \in \mathrm{Cl}^{1}(V,q) \,\},
$$

the even part of the super-commutant being the right multiplications and the odd part their conjugates by the parity operator.

**Proof.** The graded centre of a graded algebra is the set of homogeneous elements super-commuting with every element, and for a Clifford algebra it coincides with the centre. For the operator statement, let $T$ be homogeneous and super-commute with every $L_x$. If $T$ is even then $[T,L_x\} = [T,L_x]$ for all $x$, so $T$ lies in the ordinary commutant $\{L_x\}' = \{R_y\}$ of *One-Sided Operators on a Clifford Algebra*. If $T$ is odd, write $T = \Gamma S$; the condition $TL_x = (-1)^{|x|}L_xT$ becomes, after substituting $\Gamma L_{\alpha(x)} = L_x\Gamma$ and $L_{\alpha(x)} = (-1)^{|x|}L_x$, the condition $SL_x = L_xS$ for every $x$, so $S \in \{R_y\}$ and $T = \Gamma R_y$; the parity of $\Gamma R_y$ is that of $y$, which forces $y$ odd.

**Remark (the super-structure as the bookkeeping of the sign).** Nothing in the last proposition is new mathematics: the parity operator $\Gamma$ implements the grade involution, and conjugating by it turns every ordinary statement into its signed form. The value of the superlanguage is bookkeeping – it names the operator $\Gamma$, it makes the sign rule $[L_x,R_y\} = \bigl(1-(-1)^{|x||y|}\bigr)L_{xy}$ a statement about graded commutators, and it exposes the signed family as the twist of the ordinary one. This is the sense in which *The Grading of the Clifford Algebra with Signed Inner Conjugation* says that the signed member is not a second structure.

## Worked Cases

### A Vector in $\mathrm{Cl}_{0,3}(\mathbb{R})$

With $e_j^{2} = -1$ let $x = e_1$, so $|x| = 1$. Then $L_{e_1}$ is an odd operator and $\Lambda^{\alpha}_{e_1} = -L_{e_1}$. On the basis $1, e_1, e_2, e_3, e_1e_2, e_1e_3, e_2e_3, \omega = e_1e_2e_3$ the ordinary left multiplication by $e_1$ carries $\mathrm{Cl}^{0}$ to $\mathrm{Cl}^{1}$ and $\mathrm{Cl}^{1}$ to $\mathrm{Cl}^{0}$, so it is odd and its presence in the supercommutant of the even operators is destroyed by the graded bracket; the signed version differs from it by the global sign $-1$, which is the twist.

### An Even Element

Let $x = e_1e_2$, so $|x| = 0$. Then $L_x$ is even and $\Lambda^{\alpha}_x = L_x$: the twisting does nothing. So the signed family coincides with the ordinary one on the even part, which is the operator form of the statement that $\alpha$ fixes $\mathrm{Cl}^{0}$.

### Two Even Elements against Two Odd Ones

For $x = e_1e_2$ and $y = e_2e_3$, both even, one has $xy = -e_1e_3$ and $yx = e_1e_3$, so $[L_x, L_y\} = [L_x,L_y] = -2L_{e_1e_3}\neq0$: two even elements need not graded-commute, because the even part of a Clifford algebra is a Clifford algebra and is not commutative. For $x = e_1$ and $y = e_2$, both odd and orthogonal, $e_1e_2 = -e_2e_1$, so $[L_{e_1}, L_{e_2}\} = L_{e_1e_2+e_2e_1} = 0$; here the graded commutator does vanish, and the contrast is the point of the proposition.

### The Graded and the Ordinary Bracket

For $x = y = e_1$ in the same algebra, $[L_{e_1}, R_{e_1}] = 0$ while $[L_{e_1}, R_{e_1}\} = 2L_{e_1}R_{e_1}$, since $|x||y| = 1$ and $(-1)^{1} = -1$. The two brackets differ, and only the graded one detects that the two operators are both odd. This is the sign rule in its smallest nontrivial form.

## Summary

The Clifford algebra is a **graded algebra**, and every homogeneous element $x$ gives multiplication operators of parity $|x|$: the left multiplication shifts the grading by $|x|$, and so does the right. The left and the right families commute as ordinary operators, $L_xR_y = R_yL_x = L_{xy}$; their **graded commutator** $[L_x,R_y\} = \bigl(1-(-1)^{|x||y|}\bigr)L_{xy}$ vanishes when a factor is even and is $2L_{xy}$ when both elements are odd, so the sign rule lives entirely in the graded bracket. The **signed multiplication operators** $\Lambda^{\alpha}_x(y) = \alpha(x)y$ and $\mathrm{P}^{\alpha}_x(y) = y\alpha(x)$ are the conjugates of the ordinary ones by the parity operator $\Gamma(y) = \alpha(y)$; they coincide with the ordinary family on the even part and differ by the sign $-1$ on the odd part, and they compose in the same order. The super-commutant of the left multiplications is the right family together with its twist, and the supercentre is the centre. The construction is the bookkeeping of the sign, not a second structure, as *The Grading of the Clifford Algebra with Signed Inner Conjugation* states; the one-sided composition laws are *One-Sided Operators on a Clifford Algebra*, and the signed two-sided family built from these operators is *Two-Sided Operators with the Signed Product*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}^{i}(V,q)$ | Even and odd parts, $i = 0, 1$ |
| $\alpha$, $\Gamma(y) = \alpha(y)$ | Grade involution and the parity operator |
| $L_x$, $R_x$ | Ordinary left and right multiplication |
| $\Lambda^{\alpha}_x(y) = \alpha(x)y$, $\mathrm{P}^{\alpha}_x(y) = y\alpha(x)$ | Signed multiplication operators |
| $[T,U\} = TU - (-1)^{|T||U|}UT$ | Graded commutator |
| $L_xR_y = R_yL_x = L_{xy}$ | The two families commute |
| $[L_x,R_y\} = \bigl(1-(-1)^{|x||y|}\bigr)L_{xy}$ | The sign rule; $2L_{xy}$ for two odd factors |
| $\Gamma L_x \Gamma = L_{\alpha(x)}$ | Twisting by the grading |
| $\{L_x\}^{\mathrm{s}}$ | Super-commutant of the left multiplications |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the grading of a Clifford algebra and the parity of its multiplications.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grade involution and the graded structure.
- Pierre Deligne, Pavel Etingof, Daniel S. Freed, Lisa C. Jeffrey, David Kazhdan, John W. Morgan, David R. Morrison and Edward Witten, *Quantum Fields and Strings: A Course for Mathematicians*, vol. 1 (American Mathematical Society, 1999), for the language of superalgebras and graded commutators.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the graded structure of a Clifford algebra and for the fact that its even part is not commutative.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the parity of the Clifford multiplications and the chirality operator.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the grade involution on the low-dimensional algebras.
