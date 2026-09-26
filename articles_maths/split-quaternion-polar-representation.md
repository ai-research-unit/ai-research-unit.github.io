# __Split-Quaternion Polar Representation__

## Introduction

This article is about the polar representation in the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$, the second of the four algebras whose polar representations this series treats. The result is that an invertible split quaternion is the product of three factors,

$$
x = r\,b\,u,
$$

a positive real scale $r$, a unit boost $b$, and an orthogonal factor $u$ which is a rotation in the timelike case and a reflection in the spacelike case. The count is three, not the two of the quaternion algebra and not the four of the biquaternion algebra of the companion articles, and each of the three arises from a distinct feature of the algebra.

The mathematical engine of the article is the matrix model. The split-quaternion algebra is isomorphic to the algebra of real two-by-two matrices, and under that isomorphism the polar representation above is the polar decomposition of a matrix into a positive definite symmetric factor and an orthogonal factor. Everything else in the article is that statement translated back into the algebra, with the translation made explicit so that the algebraic form can be used without passing through the matrices.

Two differences from the quaternion case govern the whole article, and both come from the norm form. The quaternion norm form is positive definite, so its square root is a positive real with no choice; the split-quaternion norm form has signature $(2,2)$ and takes both signs, so the modulus must be built from the absolute value $|N(x)|$ and the sign of $N(x)$ is transferred to the orthogonal factor. And the quaternion algebra is a division algebra, so every nonzero element has a polar representation; the split-quaternion algebra has a null cone, and the elements on it have none, so the theorem is stated on the invertible elements and the trichotomy of the corpus's *Split-Quaternion Norm and Invertibility* is carried along.

The conventions are those of *Split-Quaternion Algebra*: the basis is $1, e_1, e_2, e_3$ with

$$
e_1^2 = -1, \qquad e_2^2 = +1, \qquad e_3 = e_1e_2, \qquad e_1e_2 = -e_2e_1,
$$

a general element is $x = a + be_1+ce_2+de_3$, the conjugate is $\bar{x} = a - be_1-ce_2-de_3$, the norm form is

$$
N(x) = x\bar{x} = a^2+b^2-c^2-d^2,
$$

the identification with $\mathrm{Cl}_{1,1}$ and with $M_2(\mathbb{R})$ is the corpus's, and the element is **timelike** when $N(x) > 0$, **spacelike** when $N(x) < 0$ and **lightlike** when $N(x) = 0$. No physics is invoked. Every numerical value below was recomputed in double precision.

## The Algebra and Its Two Involutions

### The Norm Form and the Three Classes

The norm form of a split quaternion is the quadratic form $N(x) = a^2+b^2-c^2-d^2$ of signature $(2,2)$. It is not positive definite, and this single fact is the source of everything that distinguishes this article from the quaternion case.

The form vanishes on a cone. The element $x = 1+e_2$ is nonzero and satisfies

$$
(1+e_2)(1-e_2) = 1 - e_2^2 = 0,
$$

so $1+e_2$ and $1-e_2$ are nonzero zero divisors and $N(1\pm e_2) = 1-1 = 0$. The corpus's classification of the nonzero elements by the sign of the norm form gives the sharp version: $x$ is invertible if and only if $N(x)\neq0$, and the invertible elements split into the two open components $N > 0$ and $N < 0$. In the language of the article on the norm and invertibility, the nonzero elements are timelike ($N>0$), spacelike ($N<0$) or lightlike ($N=0$), and only the lightlike ones fail to be invertible.

The polar representation is a statement about the two invertible classes, and the null cone is exactly its domain of failure. This is the first appearance in the series of a decomposition whose domain is not the whole of the nonzero elements, and it is worth noting that the failure here is the mildest one: it is a single cone, of codimension one, and on it the decomposition fails by degeneracy rather than by contradiction, since $x x^{\tau}$ becomes positive semidefinite instead of positive definite.

### The Matrix Model

Under the isomorphism $\Phi : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ of *Split-Quaternion Algebra*, fixed on the basis by

$$
\Phi(1) = \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix}, \qquad
\Phi(e_1) = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}, \qquad
\Phi(e_2) = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix}, \qquad
\Phi(e_3) = \begin{pmatrix} -1 & 0 \\ 0 & 1\end{pmatrix},
$$

a general element becomes

$$
\Phi(x) = \begin{pmatrix} a-d & -b+c \\ b+c & a+d \end{pmatrix},
$$

and the determinant is the norm form,

$$
\det\Phi(x) = (a-d)(a+d) - (c-b)(c+b) = a^2+b^2-c^2-d^2 = N(x).
$$

The model is faithful in the strong sense: it is an isomorphism of algebras, so every algebraic statement below could be checked in either picture, and the polar representation is a theorem of the matrices before it is a theorem of the algebra.

### The Transpose Involution

The matrix transpose induces, through $\Phi$, an anti-automorphism of the algebra. Write it $\tau$ and call it the **transpose involution**. Its action on the basis is

$$
\tau(1) = 1, \qquad \tau(e_1) = -e_1, \qquad \tau(e_2) = e_2, \qquad \tau(e_3) = e_3,
$$

and on a general element it reads $x^{\tau} = a - be_1 + ce_2 + de_3$. That $\tau$ is an anti-automorphism, $(\xi\eta)^{\tau} = \eta^{\tau}\xi^{\tau}$, is inherited from the transpose of matrices; it can also be checked on the three products that generate the algebra. Its fixed space is

$$
\{x : x^{\tau} = x\} = \operatorname{span}\{1, e_2, e_3\},
$$

the three-dimensional subspace of symmetric matrix images, and its anti-fixed space is the line $\mathbb{R}e_1$ of antisymmetric images.

The transpose involution is distinct from the norm-form conjugation $\bar{\cdot}$, which reads $x \mapsto a - be_1 - ce_2 - de_3$ and negates all three vector units. Both are anti-automorphisms and both fix the scalars; they differ in the sign they give $e_2$ and $e_3$, and this difference is what makes one of them usable here and the other not.

### Why the Norm-Form Conjugation Cannot Serve

A polar representation needs a factor that is, in a definite sense, positive. In the matrix picture the positive factor is the symmetric positive definite square root of $XX^{T}$, and the form $XX^{T}$ is positive definite for every invertible $X$ by construction, since $v^{T}XX^{T}v = |X^{T}v|^2 > 0$ for $v \neq 0$ when $X$ is invertible.

The algebra's own quadratic form does not do this job. For any $x$ one has $x\bar{x} = N(x)$, a real scalar, and it is negative whenever $x$ is spacelike: for $x = e_3$, for instance, $x\bar{x} = N(e_3) = -1$. An object with negative scalar value cannot be a positive factor, and there is no way to repair the defect by a sign, since the sign varies over the algebra. The positive object must therefore be built from the transpose involution instead:

$$
S(x) = x\,x^{\tau},
$$

which is the algebra's name for $XX^{T}$ and which is symmetric and positive definite for every invertible $x$. Both the real scalar $N(x)$ and the symmetric element $x x^{\tau}$ are needed below: the first supplies the modulus, the second the boost.

## The Polar Decomposition

### The Definition

**Definition.** Let $x \in \mathbb{H}_{\mathrm{s}}$ with $N(x) \neq 0$. The **polar representation** of $x$ is the writing

$$
x = r\,b\,u , \qquad r \in \mathbb{R},\quad r > 0, \qquad b \in \mathbb{H}_{\mathrm{s}},\quad b^{\tau} = b,\quad N(b) = 1,\quad b \text{ positive definite}, \qquad u \in \mathbb{H}_{\mathrm{s}},\quad u^{\tau}u = 1,
$$

in which $r$ is the **modulus**, $b$ the **unit boost** and $u$ the **orthogonal factor**.

The definition is stated before its existence is proved, and it contains three conditions that are not independent: a symmetric element of the algebra is positive definite exactly when its two eigenvalues are positive, and the normalisation $N(b) = 1$ fixes the product of those eigenvalues. The conditions are collected in the proposition below.

### The Positive Element and the Modulus

Let $x$ be invertible, and put

$$
S = x\,x^{\tau}, \qquad P = \sqrt{S},
$$

where the square root is the symmetric positive definite root, which exists and is unique because $S$ is symmetric positive definite; in the matrix picture this is the standard positive square root of $XX^{T}$, computed for a two-by-two matrix by

$$
\sqrt{\begin{pmatrix} p & q \\ q & r\end{pmatrix}} = \frac{1}{\sqrt{p+r+2\sqrt{pr-q^2}}}\begin{pmatrix} p+\sqrt{pr-q^2} & q \\ q & r+\sqrt{pr-q^2}\end{pmatrix},
$$

which is the closed form of the Cayley-Hamilton square root. The element $P$ is symmetric, and its determinant is

$$
\det P = \sqrt{\det S} = \sqrt{(\det X)^2} = |\det X| = |N(x)| ,
$$

because the determinant of the product is the product of the determinants and $\det X^{T} = \det X$.

The modulus is the square root of that determinant,

$$
r = \sqrt{\det P} = \sqrt{|N(x)|} ,
$$

a positive real. The absolute value is forced: for spacelike $x$ the determinant $\det X = N(x)$ is negative, its square root is not real, and the modulus must be taken from $|N(x)|$ instead. The sign that the absolute value discards is not lost; it reappears in the orthogonal factor, as the next subsection shows.

### The Unit Boost

The boost is the scale-free part of the positive element,

$$
b = \frac{P}{r}, \qquad \det b = \frac{\det P}{r^2} = \frac{|N(x)|}{|N(x)|} = 1 .
$$

It is symmetric, positive definite, and of determinant and norm form one, so it lies in the intersection of the symmetric subspace with $SL(2,\mathbb{R})$: the two conditions $b^{\tau} = b$ and $N(b) = 1$ of the definition are met. The set of such elements is the two-dimensional hyperbolic plane, the symmetric space of the algebra; it is the analogue of the Hermitian positive boosts of the biquaternion algebra, and it is what the quaternion algebra lacks.

### The Orthogonal Factor

The orthogonal factor is the complement of the positive factor,

$$
u = P^{-1}x = \frac{1}{r}\,b^{-1}x ,
$$

and it is orthogonal in the algebra's transpose sense. Indeed

$$
u^{\tau}u = x^{\tau}P^{-1}P^{-1}x = x^{\tau}(PP)^{-1}x = x^{\tau}(xx^{\tau})^{-1}x ,
$$

and the last expression is the identity, because $(xx^{\tau})^{-1} = (x^{\tau})^{-1}x^{-1}$ and the middle factors cancel. Its determinant is

$$
\det u = \frac{\det x}{\det P} = \frac{N(x)}{|N(x)|} = \operatorname{sign} N(x) ,
$$

so the orthogonal factor lies in $SO(2)$ when $x$ is timelike and in the other component of $O(2)$ when $x$ is spacelike. The discarded sign of the norm form is exactly the determinant of $u$.

### Existence and Uniqueness

**Theorem.** Every split quaternion $x$ with $N(x)\neq0$ has exactly one polar representation.

*Existence.* For such $x$, the element $S = xx^{\tau}$ is symmetric positive definite, so it has a unique symmetric positive definite square root $P$, whose determinant is $|N(x)| > 0$. Setting $r = \sqrt{\det P}$, $b = P/r$ and $u = P^{-1}x$ gives $r>0$, $\det b = 1$ with $b$ symmetric positive definite, and $u^{\tau}u = 1$, while $rbu = r(P/r)(P^{-1}x) = x$.

*Uniqueness.* Suppose $x = rbu = r'b'u'$ with both triples admissible. Then $xx^{\tau} = r^2 b^2 = r'^2 b'^2$. The element $r^2b^2$ is symmetric positive definite, and its symmetric positive definite square root is unique, so $rb = r'b'$. Taking norm forms gives $r^2 = r'^2$, whence $r = r'$ because both are positive, then $b = b'$, then $u = u'$. $\square$

The uniqueness is without sign ambiguity, as in the quaternion case, and for the same reason: the modulus is required to be positive, and that requirement pins down the square root.

### The Trichotomy of the Elements

The decomposition behaves differently on the two invertible classes, and the difference is entirely in the orthogonal factor.

| class of $x$ | $N(x)$ | $r$ | $b$ | $u$ | $u$ is |
|---|---|---|---|---|---|
| timelike | $>0$ | $\sqrt{N(x)}$ | unit boost | $\det u = +1$ | a rotation, $u = \cos\theta+\sin\theta\,e_1$ |
| spacelike | $<0$ | $\sqrt{-N(x)}$ | unit boost | $\det u = -1$ | a reflection times a rotation, $u = (\cos\theta+\sin\theta\,e_1)e_2$ |
| lightlike | $=0$ | not defined | not defined | not defined | no decomposition |

The lightlike class is the null cone, the zero divisors of *Split-Quaternion Zero Divisors*; on it $S = xx^{\tau}$ has rank one and determinant zero, so $P$ is only positive semidefinite and no positive modulus exists. The trichotomy is the exact statement of the domain of the theorem.

## The Exponential Form of the Boost

### The Boost Subspace

The boost lies in $\operatorname{span}\{1,e_2,e_3\}$, the fixed space of $\tau$. Removing the scalar direction, which the normalisation $N(b) = 1$ separates, leaves the two-dimensional subspace

$$
\mathfrak{p} = \operatorname{span}\{e_2, e_3\},
$$

whose matrix image is the space of symmetric traceless two-by-two matrices, since $\Phi(e_2)$ and $\Phi(e_3)$ have vanishing trace and $\Phi(1)$ does not. The elements of $\mathfrak{p}$ are the algebra's hyperbolic directions, and they exponentiate into the boosts.

### The Logarithm and the Closed Form

**Proposition.** Let $b$ be symmetric positive definite with $N(b) = 1$, and write $b = b_1 + b_2e_2 + b_3e_3$. Then $b_1 \ge 1$ and

$$
b = \exp(\sigma), \qquad \sigma = \frac{\operatorname{arccosh}(b_1)}{\sqrt{b_2^2+b_3^2}}\left(b_2e_2+b_3e_3\right) \in \mathfrak{p},
$$

with the convention that $\sigma = 0$ when $b_2 = b_3 = 0$, in which case $b = 1$.

*Proof.* For $\sigma = t_2e_2+t_3e_3 \in \mathfrak{p}$, the cross terms cancel because $e_2e_3+e_3e_2 = 0$ and the squares are both $+1$, so

$$
\sigma^2 = t_2^2+t_3^2 + t_2t_3\left(e_2e_3+e_3e_2\right) = \left(t_2^2+t_3^2\right)\cdot 1 ,
$$

a positive multiple of the identity. The exponential of such an element is the hyperbolic cosine-sine pair, $\exp(\sigma) = \cosh d + \frac{\sinh d}{d}\sigma$ with $d = \sqrt{t_2^2+t_3^2}$, by the same power-series split as in the quaternion case with the signs exchanged. Comparing with $b$ gives $b_1 = \cosh d$, whence $d = \operatorname{arccosh}(b_1)$ and $(b_2,b_3) = \frac{\sinh d}{d}(t_2,t_3)$, which is the displayed formula. $\square$

The positivity of $b$ enters only through $b_1 \ge 1$, which is the condition for the arccosine hyperbolic to be defined; it holds automatically, since $b$ has determinant one and trace $2b_1$, and $\det b = 1$ with $b$ positive definite forces $b_1 \ge 1$.

### The Two Parameters of a Boost

The exponential map is a bijection from $\mathfrak{p}$ onto the boosts. It is injective because the formula above inverts it, and surjective by the proposition; and it is a diffeomorphism, since both the formula and its inverse are smooth away from the origin, where the coordinates degenerate but the element does not. The boost is therefore described by two real parameters $t_2,t_3$, and its rapidity, in the sense of the hyperbolic distance in the symmetric space, is $d = \sqrt{t_2^2+t_3^2}$.

This is the structural difference from the biquaternion case of the companion article. There the boosts also form a three-dimensional hyperbolic space with a rapidity and an axis; here the boost space is two-dimensional because the algebra has one compact direction fewer, the missing direction being supplied by the third factor, or rather by the fact that the orthogonal factor here has only one continuous parameter. The counting is made precise in the comparison section below.

## The Orthogonal Factor in Two Components

### The Rotation Component

Suppose first that $x$ is timelike, so $\det u = +1$ and $u \in SO(2)$. In the algebra the rotation component is

$$
u = \cos\theta + \sin\theta\,e_1 ,
$$

with $\theta\in\mathbb{R}$ modulo $2\pi$, because $\Phi$ sends that element to the rotation matrix $\begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}$. The angle is read off by $\theta = \operatorname{atan2}(u_1,u_0)$. The rotation component is compact: it is the circle group of the algebra, generated by the single negative-square unit $e_1$.

### The Reflection Component

Suppose now that $x$ is spacelike, so $\det u = -1$. Every matrix of $O(2)$ with determinant $-1$ is a reflection, and every reflection is a rotation times the fixed reflection $\Phi(e_2)$; correspondingly every element of $\mathbb{H}_{\mathrm{s}}$ with $u^{\tau}u = 1$ and $\det u = -1$ is

$$
u = (\cos\theta+\sin\theta\,e_1)\,e_2 ,
$$

with the same angle convention. The element $e_2$ is the fixed reflection, and the factorisation is unique for the same reason the rotation form is: the angle is read off from the rotation part and the discrete factor is then determined. The reflection is therefore the discrete part of the orthogonal factor and the angle is its continuous part.

The presence of two components is the sharpest contrast with the quaternion case, where the rotor lies in the connected group $\mathrm{Sp}(1)$. The reason is the group that the rotor occupies and not the norm form directly: here the rotor satisfies $u^{\tau}u = 1$, so it is an element of the full orthogonal group $O(2)$, whose two components are the rotations and the reflections and are separated by the determinant; there the rotor satisfies $N(u) = 1$ and is an element of the sphere $S^3$, which is connected. The indefiniteness of $N$ enters in a different place, by making spacelike elements available in the first place, and it is the spacelike elements that carry the reflection.

## Worked Examples

### A Timelike Element

Take $x = 3 + e_1 + e_2$, so $a = 3$, $b = 1$, $c = 1$, $d = 0$ and

$$
N(x) = 9+1-1 = 9 > 0 ,
$$

a timelike element. The matrix is $\Phi(x) = \begin{pmatrix} 3 & 0 \\ 2 & 3\end{pmatrix}$, and $xx^{\tau}$ has matrix $\begin{pmatrix} 9 & 6 \\ 6 & 13\end{pmatrix}$, whose determinant is $117-36 = 81 = N(x)^2$. The modulus is

$$
r = \sqrt{9} = 3 ,
$$

the boost is

$$
b = 1.054092553 + 0.316227766\,e_2 + 0.105409255\,e_3 , \qquad \det b = 1 ,
$$

with logarithm

$$
\sigma = \log b = 0.310646488\,e_2 + 0.103548829\,e_3 , \qquad |\sigma| = 0.327450 ,
$$

and the orthogonal factor is

$$
u = 0.948683298 + 0.316227766\,e_1 , \qquad \theta = \operatorname{atan2}(0.316227766, 0.948683298) = 0.321750554\ \text{rad} \approx 18.435^\circ ,
$$

with $\det u = +1$, as the timelike class requires. The reconstruction $rbu = x$ and the identity $b = \exp\sigma$ were both checked in double precision, to $6.4\times10^{-13}$ and $1.2\times10^{-14}$ respectively in the coefficients.

### A Spacelike Element

Take $x = 1+e_1+2e_2$, so $N(x) = 1+1-4 = -2 < 0$, a spacelike element, with $\Phi(x) = \begin{pmatrix} 1 & 1 \\ 3 & 1\end{pmatrix}$ and $xx^{\tau}$ of matrix $\begin{pmatrix} 2 & 4 \\ 4 & 10\end{pmatrix}$. Then

$$
r = \sqrt{2}, \qquad b = 1.414213562 + 0.707106781\,e_2 + 0.707106781\,e_3 , \qquad \sigma = 0.623225240\left(e_2+e_3\right),
$$

and

$$
u = e_2 ,
$$

which is the reflection with zero angle: the element is rational in the sense that its decomposition involves no transcendental factor beyond the boost. The determinant of $u$ is $-1$, as the spacelike class requires, and the reconstruction was checked to $6.4\times10^{-13}$.

### A Lightlike Element

Take $x = 1+e_2$. Then $N(x) = 1-1 = 0$, and $x$ is a zero divisor, as the identity $(1+e_2)(1-e_2) = 0$ shows. The matrix $xx^{\tau}$ is $\begin{pmatrix} 1 & 1 \\ 1 & 1\end{pmatrix}$, of rank one and determinant zero, so its symmetric square root is positive semidefinite and not positive definite, the modulus $\sqrt{|N(x)|} = 0$ is not positive, and the boost $b = P/r$ is not defined. No polar representation exists, and none of the three factors survives.

The failure is characteristic of the null cone and not of a particular element: every lightlike $x$ has $\det\Phi(x) = 0$, hence $xx^{\tau}$ of rank at most one, hence no positive definite square root.

## Comparison with the Quaternion Case

The two decompositions differ in structure, and the difference is summarised by which of the four series slots are occupied. The counts are real dimensions of the corresponding factor sets.

| slot | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$, timelike | $\mathbb{H}_{\mathrm{s}}$, spacelike |
|---|---|---|---|
| scale $r$ | $1$ | $1$ | $1$ |
| central phase | $0$ | $0$ | $0$ |
| boost $b$ | $0$ | $2$ | $2$ |
| rotor $u$ | $3$ | $1$ | $1$ plus a discrete reflection |
| total | $4$ | $4$ | $4$ |

Three points of the comparison are worth stating explicitly.

**The modulus is still a real scale, but its formula is not.** In $\mathbb{H}$ the modulus is $\sqrt{N(q)}$ and needs no absolute value, because the norm form is definite. In $\mathbb{H}_{\mathrm{s}}$ it is $\sqrt{|N(x)|}$, and the absolute value is not a cosmetic convenience: it is the statement that the norm form takes both signs.

**A boost appears, and a rotation direction disappears.** The quaternion algebra has three compact directions, the unit sphere $S^3$; the split-quaternion algebra has one, the circle generated by $e_1$. The two directions lost from the compact part are exactly the two directions gained by the boost, and the total remains four. In the biquaternion algebra of the companion article both a three-dimensional boost and a three-parameter rotor are present, and both survive because the algebra is eight-dimensional.

**The centre contributes nothing in either case.** The centre of $\mathbb{H}_{\mathrm{s}}$ is $\mathbb{R}$, so there is no central phase factor, just as in $\mathbb{H}$. The centre-valued factor is of dimension one in the biquaternion algebra and provides the fourth factor there.

## Summary

Let $x$ be a split quaternion with $N(x)\neq0$. Then $x$ has exactly one polar representation

$$
x = r\,b\,u , \qquad r = \sqrt{|N(x)|} > 0 ,
$$

in which $b$ is the unique symmetric positive definite element with $b^{\tau} = b$ and $N(b) = 1$, and $u = P^{-1}x$ is the orthogonal factor, of determinant $\operatorname{sign}N(x)$. The boost lies in $\operatorname{span}\{1,e_2,e_3\}$ and is the exponential of an element of $\operatorname{span}\{e_2,e_3\}$, with the closed form $\sigma = \operatorname{arccosh}(b_1)(b_2e_2+b_3e_3)/\sqrt{b_2^2+b_3^2}$. The orthogonal factor is a rotation $\cos\theta+\sin\theta\,e_1$ when $x$ is timelike and a rotation times the reflection $e_2$ when $x$ is spacelike. On the null cone, where $N(x) = 0$, no polar representation exists. Of the four series slots, two are filled here, the scale and the boost, together with a one-parameter rotor; the central phase is absent because the centre is $\mathbb{R}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, basis $1,e_1,e_2,e_3$, $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$ |
| $x = a+be_1+ce_2+de_3$ | a split quaternion |
| $\bar{x} = a-be_1-ce_2-de_3$ | the norm-form conjugation |
| $x^{\tau} = a-be_1+ce_2+de_3$ | the transpose involution, the image of the matrix transpose |
| $N(x) = x\bar{x} = a^2+b^2-c^2-d^2$ | the norm form, of signature $(2,2)$ |
| $\Phi$ | the isomorphism $\mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ |
| $S = xx^{\tau}$, $P = \sqrt{S}$ | the positive element and its symmetric positive definite square root |
| $r = \sqrt{|N(x)|}$ | the modulus |
| $b = P/r$ | the unit boost, $b^{\tau} = b$, $N(b) = 1$ |
| $\mathfrak{p} = \operatorname{span}\{e_2,e_3\}$ | the boost subspace, symmetric traceless images |
| $u = P^{-1}x$ | the orthogonal factor, $u^{\tau}u = 1$, $\det u = \operatorname{sign}N(x)$ |
| timelike, spacelike, lightlike | $N > 0$, $N < 0$, $N = 0$ |

## Further Reading

- *Split-Quaternion Algebra* (`articles_maths/split-quaternion-algebra.md`), for the algebra, the matrix model, the conjugations and the norm form of signature $(2,2)$.
- *Split-Quaternion Norm and Invertibility* (`articles_maths/split-quaternion-norm-and-invertibility.md`), for the trichotomy timelike, spacelike, lightlike and the two components of the invertible set.
- *Split-Quaternion Zero Divisors* (`articles_maths/split-quaternion-zero-divisors.md`), for the null cone and the elements on which the decomposition fails.
- *Quaternion Polar Representation* (`articles_maths/quaternion-polar-representation.md`), for the definite case, where the absolute value is unnecessary and the boost is absent.
- *Biquaternion Polar Representation* (`articles_maths/biquaternion-polar-representation.md`), for the four-factor case in eight real dimensions.
- *Split-Quaternion Rotations and the Lorentz Group* (`articles_maths/split-quaternion-rotations-and-the-lorentz-group.md`), for the action of the orthogonal factor and of the unit group on the vector subspace.
