
# __The Signed Left Multiplication on an Ordered Algebra__

## Introduction

The **signed left multiplication** of a graded algebra is the one-sided operator

$$
L^{\alpha}_a : x\mapsto a\,\alpha(x) ,
$$

the left multiplication with the argument twisted by the grade involution. It is the one-sided companion of the signed sandwich, and it has the same factorisation: if $\Gamma$ is the grading operator, then

$$
L^{\alpha}_a = L_a\circ\Gamma = \Gamma\circ L_a ,
$$

so the signed left multiplication is the ordinary left multiplication composed with the grading, and in the graded case it acts on a homogeneous element by the sign of its parity, $L^{\alpha}_a x = \varepsilon_x\,ax$. Its composition law is the **twisted law**

$$
L^{\alpha}_a\,L^{\alpha}_b = L_{a\,\alpha(b)} ,
$$

which is the ordinary left multiplication with the twisted parameter, and which is the one-sided counterpart of the composition law of the signed sandwich. The operator is an involution of the underlying vector space exactly when $a$ is a **reflection element**, $\alpha(a) = a^{-1}$, and the elements it fixes are the eigenvectors of $L_a$ with the parity as eigenvalue: the fixed points of $L_a$ on the even part and the $-1$ eigenvectors on the odd part.

The article is the one-sided member of the signed family of the category. It compares the signed left multiplication with the unsigned one, states the composition law and the fixed-point description, and records what the order adds: the signed left multiplication is positive when the grade involution preserves the cone and $a$ is positive, and it is the negative of the unsigned multiplication on the odd part, so that the order detects the parity exactly as it does for the sandwich. The unsigned and signed left multiplications, the ordered algebra and the composition law are *The Left and Right Multiplication Operators on an Ordered Algebra* and *The Signed Sandwich on an Ordered Algebra*; the grading and the grade involution are *Superalgebras and Graded Structures* of Part I; the reflections and the reflection elements are *Reflections as Signed Two-Sided Operators on an Ordered Algebra*; the order is *Ordered Vector Spaces and the Order Unit* and *Positive Operators on an Ordered Space*; and the graded action on a module, which is the module version of this operator, is *The Graded Action on a Module over an Ordered Algebra* which follows. The adjoint of this operator is *The Signed Adjoint of the Left Multiplication on an Ordered Algebra* at the end of the category.

## Definition and First Properties

**Definition.** For $a\in A$ the **signed left multiplication** and the **signed right multiplication** are

$$
L^{\alpha}_a : A\to A, \quad L^{\alpha}_a x = a\,\alpha(x) , \qquad R^{\alpha}_a : A\to A, \quad R^{\alpha}_a x = \alpha(x)\,a .
$$

When the grade involution is the identity, $L^{\alpha}_a = L_a$ and $R^{\alpha}_a = R_a$ are the ordinary one-sided multiplications.

**Proposition (linearity, factorisation and the vanishing).** $L^{\alpha}_a$ and $R^{\alpha}_a$ are linear in $x$ and in the parameter. With the grading operator $\Gamma$ of *The Signed Sandwich on an Ordered Algebra*,

$$
L^{\alpha}_a = L_a\circ\Gamma = \Gamma\circ L_a , \qquad R^{\alpha}_a = R_a\circ\Gamma = \Gamma\circ R_a ,
$$

so each signed one-sided multiplication is the unsigned one composed with the grading, and it vanishes if and only if $a = 0$ in a unital algebra when $\alpha$ is surjective.

*Proof.* Linearity is that of $\alpha$ and of the multiplication; the factorisation is $\alpha = \Gamma$ on the underlying vector space and the commutation of the grading with the left multiplication, $\Gamma(ax) = \alpha(a\alpha(x))\cdot$ — computed in the graded case as $\varepsilon_a\varepsilon_x = \varepsilon_{ax}$, so that $\Gamma L_a = L_a\Gamma$ on the homogeneous elements. The vanishing uses $L^\alpha_a(1) = a$ when $\alpha(1) = 1$.

**Proposition (bijectivity).** The signed left multiplication is bijective if and only if $a$ is a unit and the grade involution is bijective; in particular it is bijective for every unit $a$ in a graded algebra with an automorphism $\alpha$.

*Proof.* The composite of the bijection $\Gamma$ with the left multiplication $L_a$, which is bijective exactly for a unit $a$ in a unital algebra.

## The Composition Law

**Theorem.** The signed left multiplications compose by the **twisted law**

$$
L^{\alpha}_a\,L^{\alpha}_b = L_{a\,\alpha(b)} , \qquad R^{\alpha}_a\,R^{\alpha}_b = R_{\alpha(b)\,a} ,
$$

their products being **unsigned** multiplications with the twisted parameter; in particular

$$
\bigl(L^{\alpha}_a\bigr)^2 = L_{a\,\alpha(a)} ,
$$

which is the identity exactly when $a$ is a reflection element, $\alpha(a) = a^{-1}$.

*Proof.* $L^{\alpha}_a\bigl(L^{\alpha}_b x\bigr) = a\,\alpha\bigl(b\,\alpha(x)\bigr) = a\,\alpha(b)\,\alpha^2(x) = a\alpha(b)\,x$, using the multiplicativity of $\alpha$ and $\alpha^2 = \mathrm{id}$; the right-handed formula is the same computation on the other side. The square is the case $b = a$, and it is the identity exactly when $a\alpha(a) = 1$, which is $\alpha(a) = a^{-1}$, the reflection-element condition of *The Signed Sandwich on an Ordered Algebra*.

**Corollary (the one-sided family and the reflections).** When $a$ is a reflection element the signed left multiplication is an **involution of the underlying vector space**, and it is an algebra automorphism only in the trivial case $a = 1$; the two-sided conjugation $\tau_a = L^{\alpha}_a R_{\alpha(a)^{-1}}$ is the algebra reflection of the previous article, and it is the composition of the signed left multiplication with the right multiplication by $\alpha(a)^{-1}$, which for a reflection element is $a$.

*Proof.* The involution statement is the square formula. For multiplicativity, $L^{\alpha}_a(xy) = a\alpha(x)\alpha(y)$ while $L^{\alpha}_a(x)L^{\alpha}_a(y) = a\alpha(x)a\alpha(y)$; taking $x = 1$ forces $a = a^2$, and with that the two agree for all $y$ only if $\alpha(y) = a\alpha(y)$ for every $y$, that is, $a = 1$ in a unital algebra. The sandwich identity is $L^{\alpha}_a\bigl(R_{\alpha(a)^{-1}}x\bigr) = a\,\alpha\bigl(x\,\alpha(a)^{-1}\bigr) = a\alpha(x)\,\alpha(\alpha(a)^{-1}) = a\alpha(x)a^{-1} = \tau_a(x)$, using $\alpha(\alpha(a)^{-1}) = \alpha^2(a^{-1}) = a^{-1}$.

## The Elements Fixed

**Definition.** The **fixed set** of the signed left multiplication is

$$
\operatorname{Fix}(L^{\alpha}_a) = \{x\in A : a\,\alpha(x) = x\} ,
$$

and the kernel is $\ker L^{\alpha}_a = \alpha^{-1}\bigl(\{x : ax = 0\}\bigr)$.

**Proposition (the fixed elements are the parity eigenvectors).** On the homogeneous elements the fixed set is described by the eigenvalues of $L_a$:

$$
x\in\operatorname{Fix}(L^{\alpha}_a) \iff L_a x = \varepsilon_x\,x ,
$$

so the fixed set is the sum of the **fixed space of $L_a$ on the even part** and the **$(-1)$-eigenspace of $L_a$ on the odd part**,

$$
\operatorname{Fix}(L^{\alpha}_a) = \ker(L_a - I)\cap A_{\bar 0} \ \oplus\ \ker(L_a + I)\cap A_{\bar 1} .
$$

When the grade involution is the identity the fixed set is the ordinary fixed space of the left multiplication, $\{x : ax = x\}$.

*Proof.* For homogeneous $x$, $\alpha(x) = \varepsilon_x x$, so $a\alpha(x) = x$ is $\varepsilon_x ax = x$, that is, $ax = \varepsilon_x x$ because $\varepsilon_x^{-1} = \varepsilon_x$. Decomposing $x$ into its even and odd parts gives the direct sum, since $L^\alpha_a$ preserves the grading. The unsigned case is $\varepsilon_x = 1$.

**Corollary (the fixed elements of a reflection element).** If $a$ is a reflection element then $\operatorname{Fix}(L^{\alpha}_a)$ is the fixed space of the involution $L^{\alpha}_a$ and the operator is diagonalisable with eigenvalues $\pm1$ on the invariant grading, the eigenvalue $\varepsilon_x$ being the parity of the eigenvector.

*Proof.* The operator is an involution by the composition law, so it is diagonalisable with eigenvalues $\pm1$; the eigenvectors are the eigenvectors of $L_a$ on the two grading pieces with the signs displayed.

## The Order and the Positivity

**Proposition (positivity of the signed left multiplication).** If the grade involution is **positive** and $a\geq0$, then $L^{\alpha}_a\geq0$ and $R^{\alpha}_a\geq0$. In general, with the parity sign $\varepsilon_x$, the signed left multiplication acts on the homogeneous elements as

$$
L^{\alpha}_a x = \varepsilon_x\,L_a x ,
$$

so it agrees with the unsigned left multiplication on the even part and is its negative on the odd part; it is positive for all positive $a$ exactly when the grade involution is positive, and otherwise the positive cone of the algebra detects the sign.

*Proof.* If $\alpha$ preserves the cone then $\alpha(x)\geq0$ for $x\geq0$ and the product $a\alpha(x)\geq0$ by the positive bilinearity of the ordered algebra. The parity formula is the definition of $\varepsilon_x$ applied to $\alpha(x)$; the failure of positivity is the presence of odd positive elements, on which the operator is the negative of a positive operator.

**Corollary (the relation to the unsigned left multiplication in the order).** The signed left multiplication is the **order-theoretic mirror** of the unsigned one: on the even part they coincide, and on the odd part the signed operator is the negative, so that an even $a$ that is positive gives a positive operator whose order interval structure agrees with the unsigned one, and an odd positive element reverses it.

*Proof.* Immediate from the parity formula and the agreement of the grading pieces with the order when $\alpha$ is positive.

## The Relation to the Signed Sandwich

**Proposition.** The signed sandwich of *The Signed Sandwich on an Ordered Algebra* factorises through the signed one-sided multiplications,

$$
\Theta^{\alpha}_{a,b} = L^{\alpha}_a\,R_{\alpha(b)} = L_a\,R^{\alpha}_{\alpha(b)} ,
$$

and the signed conjugation of the reflection article is $\tau_a = L^{\alpha}_a R_{\alpha(a)^{-1}}$, which for a reflection element is $L^{\alpha}_aR_a$. Consequently the two-sided operator is the composition of the two one-sided operators, and the one-sided operator is the two-sided one with the other factor equal to the identity.

*Proof.* $L^{\alpha}_a(R_{\alpha(b)}x) = a\,\alpha\bigl(x\,\alpha(b)\bigr) = a\,\alpha(x)\,\alpha^2(b) = a\alpha(x)b = \Theta^{\alpha}_{a,b}(x)$; the second form is the same computation with the factors exchanged. For the conjugation, $R_{\alpha(a)^{-1}}x = x\alpha(a)^{-1}$ and $\alpha(\alpha(a)^{-1}) = a^{-1}$, so $L^{\alpha}_aR_{\alpha(a)^{-1}}x = a\alpha(x)a^{-1} = \tau_a(x)$; the reflection-element identity $\alpha(a)^{-1} = a$ gives $L^\alpha_aR_a$.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{R})$ with the identity grade involution. The signed left multiplication is the unsigned one, $L^{\alpha}_a = L_a : x\mapsto ax$, its fixed set is $\{x : ax = x\}$, and it is an involution only if $a$ is an involution, in which case it is the projection onto the $1$-eigenspace along the $(-1)$-eigenspace when $a$ is diagonalisable. The order is the operator order of *Positive Operators on an Ordered Space*, and $L_a\geq0$ exactly when $a$ maps the positive cone into itself.

### The Biquaternion Algebra

Let $A = \mathbb{B} = M_2(\mathbb{C})$ with $\alpha$ the conjugation by $\operatorname{diag}(1,-1)$. For the odd element $a$ with $a^2 = -1$ the signed left multiplication has square $L_{a\alpha(a)} = L_{-a^2} = L_1 = I$, so it is an involution of the underlying vector space; its fixed set is the $1$-eigenspace of $L_a$ on the diagonal part and the $(-1)$-eigenspace on the off-diagonal part. The operator is not an algebra automorphism, and its two-sided completion $L^{\alpha}_a R_a$ is the signed conjugation of the previous article, which is. This is the cleanest instance in which the one-sided signed operator is an involution and the two-sided one is the reflection.

### The Group Algebra

Let $A = \mathbb{R}[G]$ with the parity grading. The signed left multiplication by a group element is $L^{\alpha}_g(h) = g\alpha(h) = (-1)^{\lvert h\rvert}gh$, so on the basis it sends $h$ to $\pm gh$ according to the parity; its composition law is $L^{\alpha}_gL^{\alpha}_{g'} = L_{g\alpha(g')}$, which on the generators is the twisted product of the reflection elements, and the fixed elements are the elements whose image under the signed action is themselves. When the group algebra is ordered by a cone that the parity preserves, the signed left multiplication is positive exactly on the positive parameters, and the parity is a sign of the cone.

## Summary

The **signed left multiplication** $L^{\alpha}_a x = a\alpha(x)$ is the left multiplication twisted by the grade involution, and it factors as $L^{\alpha}_a = L_a\circ\Gamma = \Gamma\circ L_a$ through the grading operator; the signed right multiplication is the mirror image. The composition law is the **twisted law** $L^{\alpha}_aL^{\alpha}_b = L_{a\alpha(b)}$, whose products are **unsigned** multiplications with the twisted parameter; consequently $\bigl(L^{\alpha}_a\bigr)^2 = L_{a\alpha(a)}$ is the identity exactly when $a$ is a **reflection element**, so the signed left multiplication is an involution of the underlying vector space on the reflection elements, while it is an algebra automorphism only trivially. The **fixed elements** are the eigenvectors of $L_a$ with the parity as eigenvalue — the fixed space on the even part and the $(-1)$-eigenspace on the odd part — and the operator is positive when the grade involution preserves the cone and $a$ is positive, being the unsigned multiplication on the even part and its negative on the odd part, $L^{\alpha}_ax = \varepsilon_x L_a x$. The signed sandwich is the two-sided completion, $\Theta^{\alpha}_{a,b} = L^{\alpha}_aR_{\alpha(b)}$, and the two-sided conjugation is $\tau_a = L^{\alpha}_aR_{\alpha(a)^{-1}}$, which for a reflection element is $L^{\alpha}_aR_a$. The unsigned multiplications are *The Left and Right Multiplication Operators on an Ordered Algebra*; the twisted law and the reflection elements are *The Signed Sandwich on an Ordered Algebra* and *Reflections as Signed Two-Sided Operators on an Ordered Algebra*; the grading is *Superalgebras and Graded Structures*; the order is *Ordered Vector Spaces and the Order Unit* and *Positive Operators on an Ordered Space*; the module version is *The Graded Action on a Module over an Ordered Algebra*; and the adjoint is *The Signed Adjoint of the Left Multiplication on an Ordered Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\alpha}_a x = a\alpha(x)$ | Signed left multiplication |
| $R^{\alpha}_a x = \alpha(x)a$ | Signed right multiplication |
| $L^{\alpha}_a = L_a\Gamma = \Gamma L_a$ | Factorisation through the grading operator |
| $L^{\alpha}_aL^{\alpha}_b = L_{a\alpha(b)}$ | Twisted composition law |
| $\bigl(L^{\alpha}_a\bigr)^2 = L_{a\alpha(a)}$ | Square; an involution on a reflection element |
| $\operatorname{Fix}(L^{\alpha}_a)$ | Elements with $a\alpha(x) = x$ |
| $L^{\alpha}_ax = \varepsilon_x L_a x$ | Parity formula |
| $\Theta^{\alpha}_{a,b} = L^{\alpha}_aR_{\alpha(b)}$ | The signed sandwich as a two-sided completion |
| $\tau_a = L^{\alpha}_aR_{\alpha(a)^{-1}}$ | The reflected two-sided operator |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the graded left action and the parity of a Clifford algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the graded representation and the sign rule of a superalgebra.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1956), for the left and right representations of an associative algebra.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and their Applications* (Springer, 1999), for the one-sided multiplication operators of a Jordan structure.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the positivity of the one-sided multiplications in an ordered algebra.
