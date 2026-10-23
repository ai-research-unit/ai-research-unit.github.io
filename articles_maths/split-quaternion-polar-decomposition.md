
# __Split-Quaternion Polar Decomposition__

## Introduction

This article is about the polar decomposition in the split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$, the second of the four algebras whose polar decompositions this series treats. The result is that an invertible split quaternion is the product of three factors,

$$
\tilde q = r\,b\,\tilde u_{\mathrm r},
$$

namely

- a positive real scale $r$ ($r \in \mathbb{R}$, $r>0$);
- a unit boost $b$ ($b \in \mathrm{P} = \operatorname{span}\{\vec e_y,\vec e_z\}$, $\langle b\rangle_{\natural}=1$);
- an orthogonal factor $\tilde u_{\mathrm r}$, a rotation in the timelike case and a reflection in the spacelike case.

The count is three, not the two of the quaternion algebra and not the four of the biquaternion algebra of the companion articles, and each of the three arises from a distinct feature of the algebra.

The mathematical engine of the article is the matrix model. The split-quaternion algebra is isomorphic to the algebra of real two-by-two matrices, and under that isomorphism the polar decomposition above is the polar decomposition of a matrix into a positive definite symmetric factor and an orthogonal factor. Everything else in the article is that statement translated back into the algebra, with the translation made explicit so that the algebraic form can be used without passing through the matrices.

Two differences from the quaternion case govern the whole article, and both come from the split-quaternion norm. The quaternion norm is positive definite, so its square root is a positive real with no choice; the split-quaternion norm has signature $(2,2)$ and takes both signs, so the modulus must be built from the absolute value $|\langle\tilde q\rangle_{\natural}|$ and the sign of $\langle\tilde q\rangle_{\natural}$ is transferred to the orthogonal factor. And the quaternion algebra is a division algebra, so every nonzero element has a polar decomposition; the split-quaternion algebra has a null cone, and the elements on it have none, so the theorem is stated on the invertible elements and the three-class classification of the corpus's *Split-Quaternion Norm and Invertibility* is carried along.

The conventions and the symbols are those of *Split-Quaternion Algebra* and of the corpus (*Conventions in Mathematics*); the symbols this article uses are collected in §*Summary of Notation*.

The identification with $\mathrm{Cl}_{1,1}$ and with $M_2(\mathbb{R})$ is the corpus's, and the element is **timelike** when $\langle\tilde q\rangle_{\natural} > 0$, **spacelike** when $\langle\tilde q\rangle_{\natural} < 0$ and **lightlike** when $\langle\tilde q\rangle_{\natural} = 0$.

No physics is invoked.

## The Word as Exponentials

The word $\tilde q = r\,b\,\tilde u_{\mathrm r}$ is a product of three factors, and the scale and the boost are exponentials while the orthogonal factor is a rotation exponential times an optional discrete reflection:

$$
\boxed{\;
\tilde q = \exp(\ln r)\,\exp(\sigma)\cdot \tilde u_{\mathrm r} , \qquad r = \sqrt{\lvert \langle\tilde q\rangle_{\natural}\rvert} > 0 , \qquad \sigma\in\mathrm{P} = \operatorname{span}\{\vec e_y,\vec e_z\}
\;}
$$,

with $\tilde u_{\mathrm r} = \exp(\tfrac{\theta}{2}\vec e_x)$ in the timelike case and $\tilde u_{\mathrm r} = \exp(\tfrac{\theta}{2}\vec e_x)\,\vec e_y$ in the spacelike case.

| # | factor | name | real dimension | exponential | case | closed form | parameter and range | unit axis |
|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | $1$ | $\exp(\ln r)$ | hyperbolic | $r$ | $r = \sqrt{\lvert \langle\tilde q\rangle_{\natural}\rvert} > 0$ | $e_t$ |
| 2 | $b$ | boost | $2$ | $\exp(\sigma)$ | hyperbolic | $b \in \mathrm{P}$, $\langle b\rangle_{\natural} = 1$ | $\sigma \in \operatorname{span}\{\vec e_y,\vec e_z\}$ | $\sigma/\lvert\sigma\rvert$ |
| 3 | $\tilde u_{\mathrm r}$ | orthogonal factor | $1$ | $\exp\bigl(\tfrac{\theta}{2}\vec e_x\bigr)$ | trigonometric | $\cos\tfrac{\theta}{2} + \sin\tfrac{\theta}{2}\,\vec e_x$, times $\vec e_y$ in the spacelike case | rotation angle $\theta$, $\vec e_y$ discrete | $\vec e_x$ |

The exponent follows the rule of the series: the character of the exponential is trigonometric, hyperbolic or parabolic according to the square of the root of the exponent, the trigonometric case for a root of $-1$, the hyperbolic for a root of $+1$, and the parabolic for a nilpotent root. The scale root $1$ and the boost root $\sigma$ (whose square is the positive scalar $\lvert\sigma\rvert^2$) are hyperbolic, the rotation root $\vec e_x$ is trigonometric, and the reflection $\vec e_y$ is discrete and is not an exponential. The boost logarithm, its two parameters and the two components of the orthogonal factor are the subject of the sections below.

**The boost and the rotation do not commute, so the order is part of the word.** The bracket is $[\sigma,\tfrac{\theta}{2}\vec e_x] = \theta(t_3\vec e_y-t_2\vec e_z)$, a real pure element in the plane of $\vec e_y$ and $\vec e_z$, non-zero as soon as $\sigma$ and $\theta$ are; the product of the two exponentials is therefore not the exponential of the sum. Over $60$ random boosts and rotations the largest coefficient of the bracket is $6.59$ and the largest coefficient of the failure $\exp(\sigma+\tfrac{\theta}{2}\vec e_x)-\exp(\sigma)\exp(\tfrac{\theta}{2}\vec e_x)$ of the sum rule is $2.09$. Two rewritings are therefore unavailable: the interchange of the boost and the rotation, and their fusion into a single exponential. The scale is central and passes through both, so the order that matters is the relative order of the boost and the orthogonal factor. The obstruction can be **total**, not merely large. At the rotation angle $\theta = 2\pi$ the rotation factor is $\exp(\pi \vec e_x) = -1$, so the element is $-b$, whose determinant is $\langle b\rangle_{\natural} = 1$ and whose trace is $-2\cosh d$; its two eigenvalues are $-\exp(d)$ and $-\exp(-d)$, both negative and distinct. A real matrix with two distinct negative eigenvalues has no real logarithm, so that element is the exponential of no element of the algebra at all, and the product of two exponentials is the only exponential description it has.

## The Algebra and Its Two Involutions

### The Split-Quaternion Norm and the Three Classes

The split-quaternion norm is the quadratic form $\langle\tilde q\rangle_{\natural} = q_t^2+q_x^2-q_y^2-q_z^2$ of signature $(2,2)$. It is not positive definite, and this single fact is the source of everything that distinguishes this article from the quaternion case.

The form vanishes on a cone. The element $\tilde q = 1+\vec e_y$ is nonzero and satisfies

$$
(1+\vec e_y)(1-\vec e_y) = 1 - \vec e_y^2 = 0,
$$

so $1+\vec e_y$ and $1-\vec e_y$ are nonzero zero divisors and $\langle 1\pm \vec e_y\rangle_{\natural} = 1-1 = 0$. The corpus's classification of the nonzero elements by the sign of the split-quaternion norm gives the sharp version: $\tilde q$ is invertible if and only if $\langle\tilde q\rangle_{\natural}\neq0$, and the invertible elements split into the two open components $N > 0$ and $N < 0$. In the language of the article on the split-quaternion norm and invertibility, the nonzero elements are timelike ($N>0$), spacelike ($N<0$) or lightlike ($N=0$), and only the lightlike ones fail to be invertible.

The polar decomposition is a statement about the two invertible classes, and the null cone is exactly its domain of failure. This is the first appearance in the series of a decomposition whose domain is not the whole of the nonzero elements, and it is worth noting that the failure here is the mildest one: it is a single cone, of codimension one, and on it the decomposition fails by degeneracy rather than by contradiction, since $\tilde q \tilde q^{\tau}$ becomes positive semidefinite instead of positive definite.

### The Matrix Model

Under the isomorphism $\mathsf{M}_2 : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ of *Split-Quaternion Algebra*, fixed on the basis by

$$
\mathsf{M}_2(1) = \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_x) = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_z) = \begin{pmatrix} -1 & 0 \\ 0 & 1\end{pmatrix},
$$

a general element becomes

$$
\mathsf{M}_2(\tilde q) = \begin{pmatrix} q_t-q_z & -q_x+q_y \\ q_x+q_y & q_t+q_z \end{pmatrix},
$$

and the determinant is the split-quaternion norm,

$$
\det\mathsf{M}_2(\tilde q) = (q_t-q_z)(q_t+q_z) - (q_y-q_x)(q_x+q_y) = q_t^2+q_x^2-q_y^2-q_z^2 = \langle\tilde q\rangle_{\natural}.
$$

The model is faithful in the strong sense: it is an isomorphism of algebras, so every algebraic statement below could be checked in either picture, and the polar decomposition is a theorem of the matrices before it is a theorem of the algebra.

### The Transpose Involution

The matrix transpose induces, through $\mathsf{M}_2$, an anti-automorphism of the algebra. Write it $\tau$ and call it the **transpose involution**. Its action on the basis is

$$
\tau(1) = 1, \qquad \tau(\vec e_x) = -\vec e_x, \qquad \tau(\vec e_y) = \vec e_y, \qquad \tau(\vec e_z) = \vec e_z,
$$

and on a general element it reads $\tilde q^{\tau} = q_t e_t - q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$. That $\tau$ is an anti-automorphism, $(\tilde q_1\tilde q_2)^{\tau} = \tilde q_2^{\tau}\tilde q_1^{\tau}$, is inherited from the transpose of matrices; it can also be checked on the three products that generate the algebra. Its fixed space is

$$
\{\tilde q : \tilde q^{\tau} = \tilde q\} = \operatorname{span}\{1, \vec e_y, \vec e_z\},
$$

the three-dimensional subspace of symmetric matrix images, and its anti-fixed space is the line $\mathbb{R}\vec e_x$ of antisymmetric images.

The transpose involution is distinct from the conjugation that defines the split-quaternion norm, ${}^{\natural}$, which reads $\tilde q \mapsto q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$ and negates all three vector units. Both are anti-automorphisms and both fix the scalars; they differ in the sign they give $\vec e_y$ and $\vec e_z$, and this difference is what makes one of them usable here and the other not.

### Why the Conjugation That Defines the Split-Quaternion Norm Cannot Serve

A polar decomposition needs a factor that is, in a definite sense, positive. In the matrix picture the positive factor is the symmetric positive definite square root of $XX^{T}$, and the form $XX^{T}$ is positive definite for every invertible $X$ by construction, since $v^{T}XX^{T}v = |X^{T}v|^2 > 0$ for $v \neq 0$ when $X$ is invertible.

The algebra's own quadratic form does not do this job. For any $\tilde q$ one has $\tilde q\tilde{q}^{\natural} = \langle\tilde q\rangle_{\natural}$, a real scalar, and it is negative whenever $\tilde q$ is spacelike: for $\tilde q = \vec e_z$, for instance, $\tilde q\tilde{q}^{\natural} = \langle \vec e_z\rangle_{\natural} = -1$. An object with negative scalar value cannot be a positive factor, and there is no way to repair the defect by a sign, since the sign varies over the algebra. The positive object must therefore be built from the transpose involution instead:

$$
\Sigma(\tilde q) = \tilde q\,\tilde q^{\tau},
$$

which is the algebra's name for $XX^{T}$ and which is symmetric and positive definite for every invertible $\tilde q$. Both the real scalar $\langle\tilde q\rangle_{\natural}$ and the symmetric element $\tilde q \tilde q^{\tau}$ are needed below: the first supplies the modulus, the second the boost.

## The Polar Decomposition

### The Definition

**Definition.** Let $\tilde q \in \mathbb{H}_{\mathrm{s}}$ with $\langle\tilde q\rangle_{\natural} \neq 0$. The **polar decomposition** of $\tilde q$ is the writing

$$
\tilde q = r\,b\,\tilde u_{\mathrm r} , \qquad r \in \mathbb{R},\quad r > 0, \qquad b \in \mathbb{H}_{\mathrm{s}},\quad b^{\tau} = b,\quad \langle b\rangle_{\natural} = 1,\quad b \text{ positive definite}, \qquad \tilde u_{\mathrm r} \in \mathbb{H}_{\mathrm{s}},\quad \tilde u_{\mathrm r}^{\tau}\tilde u_{\mathrm r} = 1,
$$

in which $r$ is the **modulus**, $b$ the **unit boost** and $\tilde u_{\mathrm r}$ the **orthogonal factor**.

Both non-scalar factors are **unit elements**, that is, elements of norm one for the norm in view up to the sign of an indefinite norm (*Conventions in Mathematics*, §*The Unitary Convention*): the norm in view is the split-quaternion norm $\langle\cdot\rangle_{\natural}$, the boost is the level set $\langle b\rangle_{\natural}=1$ inside the positive definite elements, and the orthogonal factor has $\langle\tilde u_{\mathrm r}\rangle_{\natural}=\pm1$, the sign being that of the element. The phrase names the norm-one elements and not every invertible element: the **group of units** $\mathbb{H}_{\mathrm{s}}^\times = \{N\neq0\}$ is the wider set of invertible elements, treated later, and the two senses of the word are kept apart throughout.

The definition is stated before its existence is proved, and it contains three conditions that are not independent: a symmetric element of the algebra is positive definite exactly when its two eigenvalues are positive, and the normalisation $\langle b\rangle_{\natural} = 1$ fixes the product of those eigenvalues. The conditions are collected in the proposition below.

### The Positive Element and the Modulus

Let $\tilde q$ be invertible, and put

$$
\Sigma = \tilde q\,\tilde q^{\tau}, \qquad P = \sqrt{\Sigma},
$$

where the square root is the symmetric positive definite root, which exists and is unique because $\Sigma$ is symmetric positive definite; in the matrix picture this is the standard positive square root of $XX^{T}$, computed for a two-by-two matrix by

$$
\sqrt{\begin{pmatrix} p & q \\ q & r\end{pmatrix}} = \frac{1}{\sqrt{p+r+2\sqrt{pr-q^2}}}\begin{pmatrix} p+\sqrt{pr-q^2} & q \\ q & r+\sqrt{pr-q^2}\end{pmatrix},
$$

which is the closed form of the Cayley-Hamilton square root. The element $P$ is symmetric, and its determinant is

$$
\det P = \sqrt{\det S} = \sqrt{(\det X)^2} = |\det X| = |\langle\tilde q\rangle_{\natural}| ,
$$

because the determinant of the product is the product of the determinants and $\det X^{T} = \det X$.

The modulus is the square root of that determinant,

$$
r = \sqrt{\det P} = \sqrt{|\langle\tilde q\rangle_{\natural}|} ,
$$

a positive real. The absolute value is forced: for spacelike $\tilde q$ the determinant $\det X = \langle\tilde q\rangle_{\natural}$ is negative, its square root is not real, and the modulus must be taken from $|\langle\tilde q\rangle_{\natural}|$ instead. The sign that the absolute value discards is not lost; it reappears in the orthogonal factor, as the next subsection shows.

### The Unit Boost

The boost is the scale-free part of the positive element,

$$
b = \frac{P}{r}, \qquad \det b = \frac{\det P}{r^2} = \frac{|\langle\tilde q\rangle_{\natural}|}{|\langle\tilde q\rangle_{\natural}|} = 1 .
$$

It is symmetric, positive definite, and of determinant and norm one, so it lies in the intersection of the symmetric subspace with $SL(2,\mathbb{R})$: the two conditions $b^{\tau} = b$ and $\langle b\rangle_{\natural} = 1$ of the definition are met. The set of such elements is the two-dimensional hyperbolic plane, the symmetric space of the algebra; it is the analogue of the Hermitian positive boosts of the biquaternion algebra, and it is what the quaternion algebra lacks.

### The Orthogonal Factor

The orthogonal factor is the complement of the positive factor,

$$
\tilde u_{\mathrm r} = P^{-1}\tilde q = \frac{1}{r}\,b^{-1}\tilde q ,
$$

and it is orthogonal in the algebra's transpose sense. Indeed

$$
\tilde u_{\mathrm r}^{\tau}\tilde u_{\mathrm r} = \tilde q^{\tau}P^{-1}P^{-1}\tilde q = \tilde q^{\tau}(PP)^{-1}\tilde q = \tilde q^{\tau}(\tilde q\tilde q^{\tau})^{-1}\tilde q ,
$$

and the last expression is the identity, because $(\tilde q\tilde q^{\tau})^{-1} = (\tilde q^{\tau})^{-1}\tilde q^{-1}$ and the middle factors cancel. Its determinant is

$$
\det \tilde u_{\mathrm r} = \frac{\det \tilde q}{\det P} = \frac{\langle\tilde q\rangle_{\natural}}{|\langle\tilde q\rangle_{\natural}|} = \operatorname{sign} \langle\tilde q\rangle_{\natural} ,
$$

so the orthogonal factor lies in $SO(2)$ when $\tilde q$ is timelike and in the other component of $O(2)$ when $\tilde q$ is spacelike. The discarded sign of the split-quaternion norm is exactly the determinant of $\tilde u_{\mathrm r}$.

### Existence and Uniqueness

**Theorem.** Every split quaternion $\tilde q$ with $\langle\tilde q\rangle_{\natural}\neq0$ has exactly one polar decomposition.

*Existence.* For such $\tilde q$, the element $\Sigma = \tilde q\tilde q^{\tau}$ is symmetric positive definite, so it has a unique symmetric positive definite square root $P$, whose determinant is $|\langle\tilde q\rangle_{\natural}| > 0$. Setting $r = \sqrt{\det P}$, $b = P/r$ and $\tilde u_{\mathrm r} = P^{-1}\tilde q$ gives $r>0$, $\det b = 1$ with $b$ symmetric positive definite, and $\tilde u_{\mathrm r}^{\tau}\tilde u_{\mathrm r} = 1$, while $rb\tilde u_{\mathrm r} = r(P/r)(P^{-1}\tilde q) = \tilde q$.

*Uniqueness.* Suppose $\tilde q = rb\tilde u_{\mathrm r} = r'b'\tilde u_{\mathrm r}'$ with both triples admissible. Then $\tilde q\tilde q^{\tau} = r^2 b^2 = r'^2 b'^2$. The element $r^2b^2$ is symmetric positive definite, and its symmetric positive definite square root is unique, so $rb = r'b'$. Taking norms gives $r^2 = r'^2$, whence $r = r'$ because both are positive, then $b = b'$, then $\tilde u_{\mathrm r} = \tilde u_{\mathrm r}'$.

The uniqueness is without sign ambiguity, as in the quaternion case, and for the same reason: the modulus is required to be positive, and that requirement pins down the square root.

### The Three Classes of Elements

The decomposition behaves differently on the two invertible classes, and the difference is entirely in the orthogonal factor.

| class of $\tilde q$ | $\langle\tilde q\rangle_{\natural}$ | $r$ | $b$ | $\tilde u_{\mathrm r}$ | $\tilde u_{\mathrm r}$ is |
|---|---|---|---|---|---|
| timelike | $>0$ | $\sqrt{\langle\tilde q\rangle_{\natural}}$ | unit boost | $\det \tilde u_{\mathrm r} = +1$ | a rotation, $\tilde u_{\mathrm r} = \cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\vec e_x$ |
| spacelike | $<0$ | $\sqrt{-\langle\tilde q\rangle_{\natural}}$ | unit boost | $\det \tilde u_{\mathrm r} = -1$ | a reflection times a rotation, $\tilde u_{\mathrm r} = (\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\vec e_x)\vec e_y$ |
| lightlike | $=0$ | not defined | not defined | not defined | no decomposition |

The lightlike class is the null cone, the zero divisors of *Split-Quaternion Zero Divisors*; on it $\Sigma = \tilde q\tilde q^{\tau}$ has rank one and determinant zero, so $P$ is only positive semidefinite and no positive modulus exists. The three classes are the exact statement of the domain of the theorem.

## The Exponential Form of the Boost

### The Boost Subspace

The boost lies in $\operatorname{span}\{1,\vec e_y,\vec e_z\}$, the fixed space of $\tau$. Removing the scalar direction, which the normalisation $\langle b\rangle_{\natural} = 1$ separates, leaves the two-dimensional subspace

$$
\mathrm{P} = \operatorname{span}\{\vec e_y, \vec e_z\},
$$

whose matrix image is the space of symmetric traceless two-by-two matrices, since $\mathsf{M}_2(\vec e_y)$ and $\mathsf{M}_2(\vec e_z)$ have vanishing trace and $\mathsf{M}_2(1)$ does not. The elements of $\mathrm{P}$ are the algebra's hyperbolic directions, and they exponentiate into the boosts.

### The Logarithm and the Closed Form

**Proposition.** Let $b$ be symmetric positive definite with $\langle b\rangle_{\natural} = 1$, and write $b = b_1 + b_2\vec e_y + b_3\vec e_z$. Then $b_1 \ge 1$ and

$$
\boxed{\;
b = \exp(\sigma), \qquad \sigma = \frac{\operatorname{arccosh}(b_1)}{\sqrt{b_2^2+b_3^2}}\left(b_2\vec e_y+b_3\vec e_z\right) \in \mathrm{P}
\;}
$$,

with the convention that $\sigma = 0$ when $b_2 = b_3 = 0$, in which case $b = 1$.

*Proof.* For $\sigma = t_2\vec e_y+t_3\vec e_z \in \mathrm{P}$, the cross terms cancel because $\vec e_y\vec e_z+\vec e_z\vec e_y = 0$ and the squares are both $+1$, so

$$
\sigma^2 = t_2^2+t_3^2 + t_2t_3\left(\vec e_y\vec e_z+\vec e_z\vec e_y\right) = \left(t_2^2+t_3^2\right)\cdot 1 ,
$$

a positive multiple of the identity. The exponential of such an element is the hyperbolic cosine-sine pair, $\exp(\sigma) = \cosh d + \frac{\sinh d}{d}\sigma$ with $d = \sqrt{t_2^2+t_3^2}$, by the same power-series split as in the quaternion case with the signs exchanged. Comparing with $b$ gives $b_1 = \cosh d$, whence $d = \operatorname{arccosh}(b_1)$ and $(b_2,b_3) = \frac{\sinh d}{d}(t_2,t_3)$, which is the displayed formula.

The positivity of $b$ enters only through $b_1 \ge 1$, which is the condition for the arccosine hyperbolic to be defined; it holds automatically, since $b$ has determinant one and trace $2b_1$, and $\det b = 1$ with $b$ positive definite forces $b_1 \ge 1$.

### The Two Parameters of a Boost

The exponential map is a bijection from $\mathrm{P}$ onto the boosts. It is injective because the formula above inverts it, and surjective by the proposition; and it is a diffeomorphism, since both the formula and its inverse are smooth away from the origin, where the coordinates degenerate but the element does not. The boost is therefore described by two real parameters $t_2,t_3$, and its rapidity, in the sense of the hyperbolic distance in the symmetric space, is $d = \sqrt{t_2^2+t_3^2}$.

This is the structural difference from the biquaternion case of the companion article. There the boosts also form a three-dimensional hyperbolic space with a rapidity and an axis; here the boost space is two-dimensional because the algebra has one compact direction fewer, the missing direction being supplied by the third factor, or rather by the fact that the orthogonal factor here has only one continuous parameter. The counting is made precise in the comparison section below.

## The Orthogonal Factor in Two Components

### The Rotation Component

Suppose first that $\tilde q$ is timelike, so $\det \tilde u_{\mathrm r} = +1$ and $\tilde u_{\mathrm r} \in SO(2)$. In the algebra the rotation component is

$$
\boxed{\;
\tilde u_{\mathrm r} = \cos\tfrac{\theta}{2} + \sin\tfrac{\theta}{2}\,\vec e_x
\;}
$$,

with $\theta$ the rotation angle and the exponent $\theta/2$ read modulo $2\pi$; $\mathsf{M}_2$ sends that element to the rotation matrix of half the angle, $\begin{pmatrix}\cos\tfrac{\theta}{2} & -\sin\tfrac{\theta}{2} \\ \sin\tfrac{\theta}{2} & \cos\tfrac{\theta}{2}\end{pmatrix}$. The rotation angle is read off by $\theta = 2\operatorname{atan2}(u_x,u_t)$. The rotation component is compact: it is the circle group of the algebra, generated by the single negative-square unit $\vec e_x$.

### The Reflection Component

Suppose now that $\tilde q$ is spacelike, so $\det \tilde u_{\mathrm r} = -1$. Every matrix of $O(2)$ with determinant $-1$ is a reflection, and every reflection is a rotation times the fixed reflection $\mathsf{M}_2(\vec e_y)$; correspondingly every element of $\mathbb{H}_{\mathrm{s}}$ with $\tilde u_{\mathrm r}^{\tau}\tilde u_{\mathrm r} = 1$ and $\det \tilde u_{\mathrm r} = -1$ is

$$
\tilde u_{\mathrm r} = (\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\,\vec e_x)\,\vec e_y ,
$$

with the same angle convention. The element $\vec e_y$ is the fixed reflection, and the factorisation is unique for the same reason the rotation form is: the angle is read off from the rotation part and the discrete factor is then determined. The reflection is therefore the discrete part of the orthogonal factor and the angle is its continuous part.

The presence of two components is the sharpest contrast with the quaternion case, where the rotor lies in the connected group $\mathrm{Sp}(1) = \{\tilde q \in \mathbb{H} : \tilde q\tilde q^{\natural} = 1\}$ of unit quaternions. The reason is the group that the rotor occupies and not the split-quaternion norm directly: here the rotor satisfies $\tilde u_{\mathrm r}^{\tau}\tilde u_{\mathrm r} = 1$, so it is an element of the full orthogonal group $O(2)$, whose two components are the rotations and the reflections and are separated by the determinant; there the rotor satisfies $\langle\tilde u_{\mathrm r}\rangle_{\natural} = 1$ and is an element of the sphere $\mathrm{Sp}(1)$ of unit quaternions, which is connected. The indefiniteness of $\langle\cdot\rangle_{\natural}$ enters in a different place, by making spacelike elements available in the first place, and it is the spacelike elements that carry the reflection.

## Worked Examples

### A Timelike Element

Take $\tilde q = 3 + \vec e_x + \vec e_y$, so $q_t = 3$, $q_x = 1$, $q_y = 1$, $q_z = 0$ and

$$
\langle\tilde q\rangle_{\natural} = 9+1-1 = 9 > 0 ,
$$

a timelike element. The matrix is $\mathsf{M}_2(\tilde q) = \begin{pmatrix} 3 & 0 \\ 2 & 3\end{pmatrix}$, and $\tilde q\tilde q^{\tau}$ has matrix $\begin{pmatrix} 9 & 6 \\ 6 & 13\end{pmatrix}$, whose determinant is $117-36 = 81 = \langle\tilde q\rangle_{\natural}^2$. The modulus is

$$
r = \sqrt{9} = 3 ,
$$

the boost is

$$
b = 1.054092553 + 0.316227766\,\vec e_y + 0.105409255\,\vec e_z , \qquad \det b = 1 ,
$$

with logarithm

$$
\sigma = \log b = 0.310646488\,\vec e_y + 0.103548829\,\vec e_z , \qquad |\sigma| = 0.327450 ,
$$

and the orthogonal factor is

$$
\tilde u_{\mathrm r} = 0.948683298 + 0.316227766\,\vec e_x , \qquad \theta = 2\operatorname{atan2}(0.316227766, 0.948683298) = 0.643501108\ \text{rad} \approx 36.870^\circ ,
$$

with $\det \tilde u_{\mathrm r} = +1$, as the timelike class requires. The reconstruction $rb\tilde u_{\mathrm r} = \tilde q$ and the identity $b = \exp\sigma$ were both checked in double precision, to $6.4\times10^{-13}$ and $1.2\times10^{-14}$ respectively in the coefficients.

### A Spacelike Element

Take $\tilde q = 1+\vec e_x+2\vec e_y$, so $\langle\tilde q\rangle_{\natural} = 1+1-4 = -2 < 0$, a spacelike element, with $\mathsf{M}_2(\tilde q) = \begin{pmatrix} 1 & 1 \\ 3 & 1\end{pmatrix}$ and $\tilde q\tilde q^{\tau}$ of matrix $\begin{pmatrix} 2 & 4 \\ 4 & 10\end{pmatrix}$. Then

$$
r = \sqrt{2}, \qquad b = 1.414213562 + 0.707106781\,\vec e_y + 0.707106781\,\vec e_z , \qquad \sigma = 0.623225240\left(\vec e_y+\vec e_z\right),
$$

and

$$
\tilde u_{\mathrm r} = \vec e_y ,
$$

which is the reflection with zero angle: the element is rational in the sense that its decomposition involves no transcendental factor beyond the boost. The determinant of $\tilde u_{\mathrm r}$ is $-1$, as the spacelike class requires, and the reconstruction was checked to $6.4\times10^{-13}$.

### A Lightlike Element

Take $\tilde q = 1+\vec e_y$. Then $\langle\tilde q\rangle_{\natural} = 1-1 = 0$, and $\tilde q$ is a zero divisor, as the identity $(1+\vec e_y)(1-\vec e_y) = 0$ shows. The matrix $\tilde q\tilde q^{\tau}$ is $\begin{pmatrix} 2 & 2 \\ 2 & 2\end{pmatrix}$, of rank one and determinant zero, so its symmetric square root is positive semidefinite and not positive definite, the modulus $\sqrt{|\langle\tilde q\rangle_{\natural}|} = 0$ is not positive, and the boost $b = P/r$ is not defined. No polar decomposition exists, and none of the three factors survives.

The failure is characteristic of the null cone and not of a particular element: every lightlike $\tilde q$ has $\det\mathsf{M}_2(\tilde q) = 0$, hence $\tilde q\tilde q^{\tau}$ of rank at most one, hence no positive definite square root.

## Comparison with the Quaternion Case

The two decompositions differ in structure, and the difference is summarised by which of the four series slots are occupied. The counts are real dimensions of the corresponding factor sets.

| slot | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$, timelike | $\mathbb{H}_{\mathrm{s}}$, spacelike |
|---|---|---|---|
| scale $r$ | $1$ | $1$ | $1$ |
| central phase | $0$ | $0$ | $0$ |
| boost $b$ | $0$ | $2$ | $2$ |
| rotor $\tilde u_{\mathrm r}$ | $3$ | $1$ | $1$ plus a discrete reflection |
| total | $4$ | $4$ | $4$ |

Three points of the comparison are worth stating explicitly.

**The modulus is still a real scale, but its formula is not.** In $\mathbb{H}$ the modulus is $\sqrt{\langle\tilde q\rangle_{\natural}}$ and needs no absolute value, because the quaternion norm is definite. In $\mathbb{H}_{\mathrm{s}}$ it is $\sqrt{|\langle\tilde q\rangle_{\natural}|}$, and the absolute value is not a cosmetic convenience: it is the statement that the split-quaternion norm takes both signs.

**A boost appears, and a rotation direction disappears.** The quaternion algebra has three compact directions, the unit sphere $\mathrm{Sp}(1)$; the split-quaternion algebra has one, the circle generated by $\vec e_x$. The two directions lost from the compact part are exactly the two directions gained by the boost, and the total remains four. In the biquaternion algebra of the companion article both a three-dimensional boost and a three-parameter rotor are present, and both survive because the algebra is eight-dimensional.

**The centre contributes nothing in either case.** The centre of $\mathbb{H}_{\mathrm{s}}$ is $\mathbb{R}$, so there is no central phase factor, just as in $\mathbb{H}$. The centre-valued factor is of dimension one in the biquaternion algebra and provides the fourth factor there.

## Summary

Let $\tilde q$ be a split quaternion with $\langle\tilde q\rangle_{\natural}\neq0$. Then $\tilde q$ has exactly one polar decomposition

$$
\tilde q = r\,b\,\tilde u_{\mathrm r} , \qquad r = \sqrt{|\langle\tilde q\rangle_{\natural}|} > 0 ,
$$

in which $b$ is the unique symmetric positive definite element with $b^{\tau} = b$ and $\langle b\rangle_{\natural} = 1$, and $\tilde u_{\mathrm r} = P^{-1}\tilde q$ is the orthogonal factor, of determinant $\operatorname{sign}\langle\tilde q\rangle_{\natural}$. The boost lies in $\operatorname{span}\{1,\vec e_y,\vec e_z\}$ and is the exponential of an element of $\operatorname{span}\{\vec e_y,\vec e_z\}$, with the closed form $\sigma = \operatorname{arccosh}(b_1)(b_2\vec e_y+b_3\vec e_z)/\sqrt{b_2^2+b_3^2}$. The orthogonal factor is a rotation $\cos\theta+\sin\theta\,\vec e_x$ when $\tilde q$ is timelike and a rotation times the reflection $\vec e_y$ when $\tilde q$ is spacelike. On the null cone, where $\langle\tilde q\rangle_{\natural} = 0$, no polar decomposition exists. Of the four series slots, two are filled here, the scale and the boost, together with a one-parameter rotor; the central phase is absent because the centre is $\mathbb{R}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, basis $1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x^2 = -1$, $\vec e_y^2 = \vec e_z^2 = +1$ |
| $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | a split quaternion |
| $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$ | the conjugation that defines the split-quaternion norm |
| $\tilde q^{\tau} = q_t e_t - q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | the transpose involution, the image of the matrix transpose |
| $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = q_t^2+q_x^2-q_y^2-q_z^2$ | the split-quaternion norm, of signature $(2,2)$ |
| $\mathsf{M}_2$ | the isomorphism $\mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ |
| $\Sigma = \tilde q\tilde q^{\tau}$, $P = \sqrt{\Sigma}$ | the positive element and its symmetric positive definite square root |
| $r = \sqrt{|\langle\tilde q\rangle_{\natural}|}$ | the modulus |
| $b = P/r$ | the unit boost, $b^{\tau} = b$, $\langle b\rangle_{\natural} = 1$ |
| $\mathrm{P} = \operatorname{span}\{\vec e_y,\vec e_z\}$ | the boost subspace, symmetric traceless images |
| $\tilde u_{\mathrm r} = P^{-1}\tilde q$ | the orthogonal factor, $\tilde u_{\mathrm r}^{\tau}\tilde u_{\mathrm r} = 1$, $\det \tilde u_{\mathrm r} = \operatorname{sign}\langle\tilde q\rangle_{\natural}$ |
| timelike, spacelike, lightlike | $N > 0$, $N < 0$, $N = 0$ |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the polar and Cartan decompositions of the classical groups and the indefinite case.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the coquaternion group, its modulus and its parametrisation.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the polar and exponential descriptions of the split-quaternion units.
- F. R. Gantmacher, *The Theory of Matrices*, Vol. 1 (Chelsea, 1959), for the polar decomposition of a real matrix and the symmetric square root of a positive semidefinite matrix.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the orthogonal group of an indefinite form, the Cayley transform and the two components of the unit set.
