
# __The Operators on an Algebra__

## Introduction

An algebra is a vector space carrying a product. Its symmetries are the algebra automorphisms, and their infinitesimal counterparts are the derivations. The two are usually introduced separately, and the several other classes of maps that an algebra carries — the multiplications by its own elements, the maps that commute with those multiplications, the maps that preserve a norm form — are usually introduced in yet other places.

This article takes the entry point that makes the relations between all of these visible at once: fix the ambient space of **every** linear operator on the algebra, and then ask of each candidate class what it is required to preserve. Every operator on $A$ is then a point of one space, $\operatorname{End}_k(A) \cong M_n(k)$ with $n = \dim_k A$, and the classification of the classes follows from a single observation about the conditions:

- a condition that is **linear** in the operator defines a **subspace** of $\operatorname{End}_k(A)$, and those subspaces are comparable by inclusion;
- a condition that is **nonlinear** in the operator defines a set that is not a subspace. It is a **group** when the condition is multiplicativity or form-preservation together with invertibility — the endomorphisms form only a monoid, and the automorphisms are its units;
- the exponential passes from one of the subspaces to one of the groups, so that the subspace is the Lie algebra of the group.

Two consequences are worth stating at the outset, because they are the reason the entry point is useful. First, the natural classes of operators are not a miscellaneous list: the conditions linear in the operator give subspaces of one ambient space, comparable with one another by inclusion, and the nonlinear conditions give groups acting on that same space. Second, the entry point separates cleanly the questions that a metric can answer from the questions that only the algebra can answer: an automorphism preserves the product and no metric data beyond what the product forces, while the operators preserving a norm form are a strictly larger class that the algebra alone does not determine, since a norm form is extra data.

The classes themselves are treated in *Automorphisms and Derivations of Algebras* and in *Automorphisms of Modules over an Algebra*; the biquaternion case is worked out in *Biquaternion Automorphisms and Derivations*. What is assembled here is the ambient space they share, the ladder of subspaces and groups inside it, and the worked examples that exhibit the ladder in the smallest dimensions.

Throughout, $k$ is a field, $A$ is a finite-dimensional unital associative $k$-algebra, and $n = \dim_k A$. The ground field is named at every step, because the ambient space depends on it.

## The Ambient Operator Space

**Definition.** An **operator** on $A$ is a $k$-linear map $M : A \to A$. The operators form the $k$-algebra $\operatorname{End}_k(A)$ under composition and addition, of dimension

$$
\dim_k \operatorname{End}_k(A) = n^2 .
$$

Choosing a $k$-basis of $A$ identifies $\operatorname{End}_k(A)$ with the matrix algebra $M_n(k)$. The identification depends on the basis, but the classes below do not: a derivation, an $A$-linear operator and an automorphism are each defined by an equation that never mentions a basis, and the groups preserving a form are defined by the form itself, the Gram matrix being only its coordinate record.

**The ground field is part of the data.** Two operators that look alike may inhabit ambient spaces of different size, because the field over which linearity is demanded changes both $n$ and the size of the matrices. The same set $A$ may therefore be read as an algebra over two fields and give two ambient spaces.

| $A$ | $k$ | $n = \dim_k A$ | $\operatorname{End}_k(A)$ | $\dim_k$ |
|---|---|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | 1 | $M_1(\mathbb{R}) = \mathbb{R}$ | 1 |
| $\mathbb{C}$ | $\mathbb{R}$ | 2 | $M_2(\mathbb{R})$ | 4 |
| $\mathbb{C}$ | $\mathbb{C}$ | 1 | $M_1(\mathbb{C}) = \mathbb{C}$ | 1 |
| $\mathbb{R}[\varepsilon]/\varepsilon^2$ | $\mathbb{R}$ | 2 | $M_2(\mathbb{R})$ | 4 |
| $\mathbb{H}$ | $\mathbb{R}$ | 4 | $M_4(\mathbb{R})$ | 16 |
| $\mathbb{B}$ | $\mathbb{C}$ | 4 | $M_4(\mathbb{C})$ | 16 |
| $\mathbb{B}$ | $\mathbb{R}$ | 8 | $M_8(\mathbb{R})$ | 64 |

The entry $\mathbb{C}$ over $\mathbb{C}$ is the extreme case: a one-dimensional algebra over $\mathbb{C}$ has a one-dimensional operator space, while the same set over $\mathbb{R}$ has a four-dimensional one.

**A size that must not be confused.** The biquaternion algebra satisfies $\mathbb{B} \cong M_2(\mathbb{C})$ as a $\mathbb{C}$-algebra. The ambient space of operators is nevertheless $M_4(\mathbb{C})$, not $M_2(\mathbb{C})$. The two matrix sizes are different and measure different things: $M_2(\mathbb{C})$ records the algebra structure of $\mathbb{B}$, whose dimension is $4$, while $M_4(\mathbb{C})$ records the operators on the vector space $\mathbb{B}$, whose dimension is $4$ as well and whose operator space therefore has dimension $16$. A $2 \times 2$ matrix representing an element of $\mathbb{B}$ is an element; a $4 \times 4$ matrix representing an operator on $\mathbb{B}$ is an operator.

## The Two Kinds of Condition

Each class of operators is cut out by a condition, and the shape of the class is decided by the degree of the condition in the operator.

| class | condition on the operator $M$ | kind | result |
|---|---|---|---|
| derivations | $M(xy) = M(x)y + xM(y)$ | linear in $M$ | subspace |
| $A$-linear operators | $M L(a) = L(a) M$ for all $a$ | linear in $M$ | subspace |
| infinitesimal form-preservers | $X^{\mathsf T} G + G X = 0$ | linear in $X$ | subspace |
| algebra endomorphisms | $M(xy) = M(x)M(y)$, $M(1) = 1$ | nonlinear in $M$ | not a subspace |
| algebra automorphisms | the above, with $M$ bijective | nonlinear | group |
| form-preservers | $M^{\mathsf T} G M = G$ | nonlinear | group |

The Leibniz rule is linear in $M$ because both occurrences of $M$ appear once and neither is composed with the other. The intertwining condition defining $A$-linearity is linear in $M$ for the same reason. The multiplicativity condition is quadratic, since the product $M(x)M(y)$ contains $M$ twice, and it does not close under addition: the sum of two multiplicative maps is generally not multiplicative. That is the whole difference between the two columns, and it is why one column is a vector space and the other is a group.

**Endomorphisms are not automorphisms.** Multiplicativity together with $M(1) = 1$ gives the unital algebra endomorphisms, and these need not be invertible. For the dual numbers the map $a + b\varepsilon \mapsto a$ is a unital endomorphism and is not invertible; it has determinant $0$ inside $M_2(\mathbb{R})$ and is therefore not a point of the automorphism group. A class defined by multiplicativity must be intersected with the invertible operators before it is called a group, and the automorphism group is that intersection.

**The exponential bridge.** For a nilpotent derivation $\delta$ and a field containing $\mathbb{Q}$, the series

$$
\exp(\delta) = \sum_{j \geq 0} \frac{\delta^j}{j!}
$$

terminates and is an algebra automorphism, by the binomial identity $\delta^m(xy) = \sum_j \binom{m}{j} \delta^j(x)\delta^{m-j}(y)$. This is the mechanism that makes the derivations the infinitesimal automorphisms, and it is the reason the two rows of the table are studied together.

**The dimension check.** The derivations are moreover the tangent space to the automorphism group at the identity, one curve of automorphisms for each $\delta$ and each direction in $\operatorname{Der}_k(A)$, so for a finite-dimensional algebra over $\mathbb{R}$ or $\mathbb{C}$

$$
\dim \operatorname{Aut}_k(A) = \dim_k \operatorname{Der}_k(A) .
$$

This gives a numerical check that is applied to every algebra below: the derivation subspace and the automorphism group must have the same dimension, and a computation that reports otherwise has lost something. The check is genuinely informative, because it relates two quantities computed in completely different ways — a nullspace of a linear system on the one hand, and an enumeration of maps preserving the product on the other.

## The Subspaces

### Multiplication Operators

**Definition.** For $a \in A$, the **left multiplication** by $a$ is the operator $L(a) : A \to A$ with $L(a)(x) = ax$, and the **right multiplication** is $R(a)(x) = xa$.

Both are $k$-linear, and both assignments are injective when $A$ is unital: from $L(a) = 0$ one gets $a = L(a)(1) = 0$, and from $R(a) = 0$ one gets $a = R(a)(1) = 0$. Hence $L$ and $R$ are injective linear maps

$$
L : A \longrightarrow \operatorname{End}_k(A), \qquad R : A \longrightarrow \operatorname{End}_k(A),
$$

and their images are subspaces of dimension $n$. The map $L$ is an algebra homomorphism, $L(a)L(b) = L(ab)$, while $R$ reverses the order, $R(a)R(b) = R(ba)$; the image of $L$ is the **regular representation** of $A$, and the image of $R$ is a copy of the opposite algebra $A^{\mathrm{op}}$.

The asymmetry between $L$ and $R$ is the whole difficulty of the noncommutative case. As a transformation of $A$, a left multiplication by a noncentral element is not $A$-linear; it is the action itself rather than a map commuting with the action.

**Example.** For $\mathbb{B}$ on the basis $(e_0,e_1,e_2,e_3)$,

$$
L(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}, \qquad
R(e_1) = \begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix}.
$$

The two agree on their first two rows and differ in the sign of the last two, and both are skew, $L(e_1)^{\mathsf T} = -L(e_1)$ and likewise for $R(e_1)$.

### The $A$-Linear Operators

**Definition.** An operator $M$ is **$A$-linear**, or $A$-module endomorphism of the regular module, when $M L(a) = L(a) M$ for every $a \in A$.

This is an intertwining condition, hence linear in $M$, and the $A$-linear operators are exactly the **centralizer** of $L(A)$ in $\operatorname{End}_k(A)$.

**Theorem.** $\operatorname{End}_A(A) = R(A) \cong A^{\mathrm{op}}$, of dimension $n$.

The theorem is proved in *Automorphisms of Modules over an Algebra*, where it is the base case of the theory of endomorphism rings. It says that requiring an operator to commute with all left multiplications forces it to be a right multiplication, and no more: the centralizer is exactly $R(A)$ and not merely of the same dimension.

The contrast with the previous subsection is worth recording, since the two spaces live in the same ambient space and have very different sizes:

| class | condition | dimension |
|---|---|---|
| all $k$-linear operators | none | $n^2$ |
| $A$-linear operators | $M L(a) = L(a)M$ for all $a$ | $n$ |

An operator is $A$-linear only in the restrictive sense; the merely $k$-linear maps are $n^2$ in number, and $A$-linearity cuts that down by a factor of $n$. For $A = \mathbb{B}$ over $\mathbb{C}$, $n = 4$ and the reduction is from $16$ to $4$.

### The Derivations

**Definition.** A **$k$-derivation** of $A$ is a $k$-linear map $\delta : A \to A$ with

$$
\delta(xy) = \delta(x)y + x\delta(y)
$$

for all $x, y \in A$. The derivations form the subspace $\operatorname{Der}_k(A)$.

The condition is linear in $\delta$, and the derivations form a Lie algebra under the commutator, with $[\delta,\varepsilon] = \delta\varepsilon - \varepsilon\delta$. The **inner derivations** are those of the form $\mathrm{ad}_a(x) = [a,x]$ for $a \in A$, and the assignment $a \mapsto \mathrm{ad}_a$ has kernel $Z(A)$, so the inner derivations form a subspace of dimension $n - \dim_k Z(A)$, in fact the quotient $A/Z(A)$.

For a separable algebra over a field every derivation is inner, so that

$$
\dim_k \operatorname{Der}_k(A) = n - \dim_k Z(A) .
$$

This is the case for the matrix algebras, the quaternion algebra and the biquaternion algebra, and it is recorded in *Automorphisms and Derivations of Algebras*. It is a conditional statement, not a general one, and the dual numbers of the next sections are the counterexample. The obstruction is specific: over a perfect field a **commutative** finite-dimensional algebra is separable exactly when it is reduced, that is, when it has no nonzero nilpotent, and $\mathbb{R}[\varepsilon]/\varepsilon^2$ is not reduced. The hypothesis cannot be weakened to the absence of nilpotents, since a matrix algebra has plenty of them and is separable all the same. When the hypothesis fails a derivation may be outer, and then the formula is false because it computes only the inner derivations, so the true derivation space is *larger* than the formula predicts. The formula is therefore used below as a check where its hypothesis holds and as a diagnostic where it does not.

## The Groups

### Algebra Automorphisms

**Definition.** A **$k$-algebra automorphism** of $A$ is a bijective $k$-linear operator with $M(xy) = M(x)M(y)$.

The automorphisms form the group $\operatorname{Aut}_k(A)$. The condition is nonlinear, so this is a group and not a subspace, and it is a closed subgroup of the units of $\operatorname{End}_k(A)$; when $k$ is $\mathbb{R}$ or $\mathbb{C}$ it is a Lie group, and its Lie algebra is $\operatorname{Der}_k(A)$, as the dimension check of the previous section records. An automorphism preserves the centre, the idempotents, the units, the zero divisors and the lattice of two-sided ideals. It preserves no metric data beyond what the product already forces: a general form on $A$ is extra structure that an automorphism has no reason to respect, but a form determined by the product, such as the norm form, is carried along automatically.

### The Operators Preserving a Form

**Definition.** Let $G$ be the Gram matrix of a nondegenerate bilinear form on $A$ in a fixed basis. The operators preserving the form are those with $M^{\mathsf T} G M = G$, and they form the group $O(G)$.

This condition is nonlinear in $M$, so $O(G)$ is a group, and its Lie algebra is the linear condition $X^{\mathsf T}G + GX = 0$ obtained by differentiating at the identity. The form is extra data: the algebra alone does not provide it, and different choices of $G$ on the same $A$ give different groups.

When the form is the norm form of the algebra and the algebra is unital, the automorphism group is contained in the orthogonal group, since an automorphism preserves the product and therefore the norm. For $\mathbb{B}$ with the norm $N(\tilde Q) = \sum_\mu Q_\mu^2$, whose Gram matrix is the identity in the basis $(e_0,e_1,e_2,e_3)$, this gives

$$
\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) \subset O(4,\mathbb{C}),
$$

so that the automorphisms are a subgroup of the norm-preserving group. The containment is in general **strict**, and not merely because of operators that move the identity, even after the identity is fixed. For $\mathbb{B}$ represented as $M_2(\mathbb{C})$, the norm is the determinant and the transpose

$$
T(Q) = Q^{\mathsf T}
$$

fixes $I$ and preserves $\det$, hence is a unital norm-preserving operator; but $T(Q Q') = T(Q')T(Q)$ reverses the order, so $T$ is an anti-automorphism rather than an automorphism, and $T(ij) = k$ while $T(i)T(j) = -k$. The unital norm-preserving operators therefore contain the automorphisms properly, and the extra elements are the anti-automorphisms and their relatives. An automorphism preserves the product and no metric data beyond what the product forces; a norm-preserving operator preserves the metric and no product data beyond what the metric forces, and the two requirements are independent.

## The Ladder

Collecting the classes, and reading the containments off the dimensions, gives one ambient space with a ladder inside it. The entries in the table are subspaces except where marked as groups.

| class | dimension over $\mathbb{C}$ | defined by |
|---|---|---|
| all $\mathbb{C}$-linear operators | 16 | none |
| $\mathfrak{so}(4,\mathbb{C})$ | 6 | $X^{\mathsf T} + X = 0$ |
| $L(\mathbb{B})$, the left multiplications | 4 | $M = L(a)$ |
| $R(\mathbb{B})$, the $A$-linear maps | 4 | centralizer of $L(\mathbb{B})$ |
| $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})$ | 3 | Leibniz |
| $\mathbb{C}\cdot I$, the scalar operators | 1 | $M = \lambda I$ |

| group | dimension over $\mathbb{C}$ | defined by |
|---|---|---|
| $GL_4(\mathbb{C})$ | 16 | invertibility |
| $O(4,\mathbb{C})$ | 6 | $M^{\mathsf T}GM = G$ |
| $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) = PSL_2(\mathbb{C})$ | 3 | multiplicativity |

The containments that hold, all of them dimension checks that have been verified by recomputation, are

$$
\mathbb{C}\cdot I \subset L(\mathbb{B}) \subset M_4(\mathbb{C}), \qquad
\operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \subset \mathfrak{so}(4,\mathbb{C}) \subset M_4(\mathbb{C}).
$$

Both inclusions on the right have been checked on explicit bases: the three derivation matrices are skew, as are $L(e_1)$, $L(e_2)$ and $L(e_3)$, while $L(e_0) = I$ is not.

Two finer statements sharpen the picture. First, the element $L(e_0) = I$ is the identity operator and is not skew, while $L(e_1)$, $L(e_2)$, $L(e_3)$ are skew, so that

$$
L(\mathbb{B}) = \mathbb{C}\cdot I \ \oplus\ L(\text{pure}),
$$

with $L(\text{pure})$ of dimension $3$. Second, the two three-dimensional pieces add up to the whole orthogonal Lie algebra:

$$
\mathfrak{so}(4,\mathbb{C}) = L(\text{pure}) \ \oplus\ \operatorname{Der}_{\mathbb{C}}(\mathbb{B}), \qquad 3 + 3 = 6 .
$$

The identity has been verified by exhibiting both spaces as subspaces of the sixteen-dimensional operator space and computing their intersection and their sum. It says that an infinitesimal norm-preserving operator splits uniquely into the part that is a left multiplication by a vector of $\mathbb{B}$ and the part that is a derivation, and that the two parts have nothing else in common.

## Worked Example: The Complex Numbers as a Real Algebra

The smallest case with a nontrivial automorphism is $A = \mathbb{C}$ over $k = \mathbb{R}$. Here $n = 2$ and the ambient space is

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{C}) = M_2(\mathbb{R}), \qquad \dim_{\mathbb{R}} = 4 ,
$$

in the basis $(1, i)$.

**The multiplication operators.** Left multiplication by $z = a + bi$ sends $x + yi$ to $(ax - by) + (ay + bx)i$, so

$$
L(a+bi) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}, \qquad \det L(a+bi) = a^2 + b^2 = N(z).
$$

The image is the two-dimensional subspace $L(\mathbb{C}) \subset M_2(\mathbb{R})$, the regular representation, and $L$ is an algebra isomorphism $\mathbb{C} \to L(\mathbb{C})$, so that the complex numbers are realised as the operators of the form above. In particular

$$
L(1) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad L(i) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.
$$

**The conjugate-linear operators.** The remainder of $M_2(\mathbb{R})$ is not of this form. An operator $\varphi$ is **conjugate-linear** when it is additive and $\varphi(\lambda z) = \bar\lambda\,\varphi(z)$ for every $\lambda \in \mathbb{C}$; such an operator is $\mathbb{R}$-linear, is not $\mathbb{C}$-linear unless it is zero, and is determined by the single value $u = \varphi(1)$, since

$$
\varphi(z) = \varphi(z \cdot 1) = \bar z\,\varphi(1) = \bar z u .
$$

Writing $u = p + qi$ and using $\bar i = -i$, the operator is

$$
\varphi(p + qi): \quad 1 \mapsto p + qi, \qquad i \mapsto -i(p+qi) = q - pi,
$$

so in the basis $(1,i)$ its matrix and its action are

$$
\varphi = \begin{pmatrix} p & q \\ q & -p \end{pmatrix}, \qquad \varphi(x + yi) = (px + qy) + (qx - py)i .
$$

These operators form a subspace of dimension $2$. The composite of two of them is $\mathbb{C}$-linear rather than conjugate-linear, since

$$
\varphi_u(\varphi_v(z)) = \overline{\varphi_v(z)}\,u = \overline{\bar z v}\,u = \overline{v}\,u\,z = L(\overline{v}u)(z),
$$

so the conjugate-linear operators are not closed under composition; the composite lands back in $L(\mathbb{C})$, as it must, since the product of two conjugations is a linear map. The two subspaces together exhaust the ambient space:

$$
M_2(\mathbb{R}) = L(\mathbb{C}) \ \oplus\ \text{(conjugate-linear operators)}, \qquad 4 = 2 + 2 .
$$

The decomposition is direct, since a matrix of the form $\begin{pmatrix} a & -b \\ b & a\end{pmatrix}$ can equal one of the form $\begin{pmatrix} p & q \\ q & -p\end{pmatrix}$ only when all four entries vanish. So every $\mathbb{R}$-linear operator on $\mathbb{C}$ is uniquely the sum of a $\mathbb{C}$-linear one and a conjugate-linear one.

**The derivations.** There are none beyond zero. If $\delta$ is an $\mathbb{R}$-derivation then

$$
0 = \delta(1) = \delta(i \cdot i) = \delta(i)i + i\delta(i) = 2i\,\delta(i),
$$

so $\delta(i) = 0$, and since $\delta$ kills $\mathbb{R}$ and $\mathbb{C}$ is generated over $\mathbb{R}$ by $1$ and $i$, the derivation is zero:

$$
\operatorname{Der}_{\mathbb{R}}(\mathbb{C}) = 0 .
$$

The vanishing says that the automorphism group of $\mathbb{C}$ over $\mathbb{R}$ is discrete: a one-parameter family of automorphisms would differentiate to a nonzero derivation, and there is none. The field has no infinitesimal symmetry, only the single reflection $\kappa$, and it is rigid over its prime field in this sense.

**The automorphisms.** A unital $\mathbb{R}$-algebra automorphism fixes $\mathbb{R}$ and sends $i$ to an element with square $-1$, so $i \mapsto \pm i$:

$$
\operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) = \{\mathrm{id},\ \kappa\} \cong \mathbb{Z}/2, \qquad \kappa(z) = \bar z .
$$

As operators the two are

$$
\mathrm{id} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \kappa = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

so the nontrivial automorphism is a **reflection** of the plane, of determinant $-1$. It is not inner, since it is not of the form $L(z)(\cdot)L(z)^{-1}$ with $z$ invertible: conjugation by a complex number fixes $i$, whereas $\kappa$ negates it.

**The consistency check.** The two structures agree in dimension, as the tangent-space argument requires:

$$
\dim \operatorname{Aut}_{\mathbb{R}}(\mathbb{C}) = 0 = \dim \operatorname{Der}_{\mathbb{R}}(\mathbb{C}).
$$

The automorphism group is finite, so it is a zero-dimensional Lie group, and its Lie algebra is zero. The check is not vacuous, and it is what would fail if a derivation or an automorphism had been missed.

**The norm-preserving operators.** With the norm $N(x+yi) = x^2+y^2$ of Gram matrix $I$, the infinitesimal form-preservers are the skew matrices, and the condition $X^{\mathsf T} + X = 0$ cuts out

$$
\mathfrak{so}(2) = \operatorname{span}_{\mathbb{R}} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \operatorname{span}_{\mathbb{R}} L(i),
$$

a one-dimensional subspace of the four-dimensional ambient space. This is the sharpest of the statements for this example: the generator of the norm-preserving rotation flow is exactly multiplication by $i$. Exponentiating gives

$$
\exp(t L(i)) = \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix} = L(\cos t + i\sin t),
$$

so the one-parameter group of rotations is the image under $L$ of the norm-one elements of $\mathbb{C}$, and the isomorphism $U(1) \to SO(2)$ of the companion article on the two-dimensional algebras is the restriction of $L$ to the norm-one group. The rotation is algebraic in origin, and the metric is what makes it visible.

## The Three Two-Dimensional Algebras

The pattern that decides the derivation space is visible by running the same computation over the three commutative unital two-dimensional algebras $\mathbb{C}$, $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ and $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$. All three have the same ambient space $M_2(\mathbb{R})$, and the classes separate as follows.

| $A$ | $Z(A)$, dimension | $n - \dim Z$ | inner derivations | $\operatorname{Der}_{\mathbb{R}}(A)$ | $\operatorname{Aut}_{\mathbb{R}}(A)$ |
|---|---|---|---|---|---|
| $\mathbb{C}$ | $\mathbb{C}$, 2 | 0 | 0 | 0 | $\mathbb{Z}/2$ |
| $\mathbb{D}$ | $\mathbb{D}$, 2 | 0 | 0 | 0 | $\mathbb{Z}/2$ |
| $\mathbb{D}'$ | $\mathbb{D}'$, 2 | 0 | 0 | **1** | $\mathbb{R}^{\times}$ |

All three algebras are commutative, so each equals its own centre and $\dim Z(A) = 2$ in every row; equivalently, every inner derivation vanishes in all three rows, since $\mathrm{ad}_a = 0$ when the algebra is commutative.

The formula $\dim \operatorname{Der} = n - \dim Z(A)$ therefore holds in the first two rows but **fails in the third**: it predicts $0$ for $\mathbb{D}'$, where the derivation space is one-dimensional. The failure is exactly the statement that the single derivation of $\mathbb{D}'$ is **outer**. So the formula is not a consequence of dimension counting alone; it holds precisely when every derivation is inner, which is a property of the algebra and not of its dimension. The automorphism group is finite in the first two rows and one-dimensional in the third, matching the dimension of the derivation space in every row, so the exponential link between the two rungs is unaffected by the failure of the formula.

This also separates the two quantities that the notation invites one to confuse. The centre $Z(A)$ is a subspace of $A$, of dimension $2$ for each of these commutative algebras. The centralizer of $L(A)$ inside $\operatorname{End}_{\mathbb{R}}(A)$ is the *right multiplications* $R(A)$, also of dimension $2$, and the two are different objects that happen to share a dimension here. Only the centre enters the derivation dimension.

**What the derivations detect.** The distinction between the rows is the presence of a nilpotent. For $\mathbb{D}$ the generator satisfies $j^2 = 1$, and $0 = \delta(j^2) = 2j\,\delta(j)$ with $j$ invertible forces $\delta(j) = 0$, so $\delta$ vanishes. For $\mathbb{D}'$ the generator satisfies $\varepsilon^2 = 0$, and the Leibniz rule imposes no such obstruction; the space is one-dimensional, spanned by the derivation with

$$
\delta(\varepsilon) = \varepsilon, \qquad \delta(a + b\varepsilon) = b\varepsilon .
$$

This derivation rescales the infinitesimal direction. It is worth noting that the naive derivative is not the derivation here: the map sending $\varepsilon$ to $1$ fails the Leibniz rule at $\varepsilon^2$, since it would send $0$ to $\varepsilon \cdot 1 + 1 \cdot \varepsilon = 2\varepsilon$. The derivation space is one-dimensional and is spanned by $\delta$ above, not by the difference quotient.

The two-dimensional algebras therefore show the ladder in two dimensions with the derivation rung and the automorphism rung changing height together, and they show the nilpotent as the source of the change. The rotations implemented by these three algebras, and the norm forms that make them rotations, are treated in *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*.

## The Four-Dimensional Cases

The quaternions and the biquaternions show the ladder at $n = 4$ over two different ground fields.

**The quaternions over $\mathbb{R}$.** Here $n = 4$ and the ambient space is $M_4(\mathbb{R})$, of dimension $16$. The centre is $\mathbb{R}$, so $\dim \operatorname{Der}_{\mathbb{R}}(\mathbb{H}) = 4 - 1 = 3$, and the derivations are the inner ones $\mathrm{ad}_p$ with $p$ pure imaginary. On the three-dimensional space of pure imaginary quaternions the bracket is twice the cross product, so

$$
\operatorname{Der}_{\mathbb{R}}(\mathbb{H}) \cong \mathbb{R}^3 \cong \mathfrak{so}(3), \qquad \operatorname{Aut}_{\mathbb{R}}(\mathbb{H}) \cong SO(3),
$$

and the automorphism group is realised by the inner automorphisms, giving the double cover $S^3 \to SO(3)$. The two dimensions agree, 3 and 3.

**The biquaternions over $\mathbb{C}$.** Here $n = 4$ and the ambient space is $M_4(\mathbb{C})$, again of dimension $16$, but the scalars are $\mathbb{C}$ rather than $\mathbb{R}$. The centre is $\mathbb{C}$, so $\dim_{\mathbb{C}} \operatorname{Der}_{\mathbb{C}}(\mathbb{B}) = 4 - 1 = 3$, and every derivation is inner:

$$
\operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathfrak{sl}_2(\mathbb{C}), \qquad \operatorname{Aut}_{\mathbb{C}}(\mathbb{B}) \cong PSL_2(\mathbb{C}),
$$

the automorphism group being the inner automorphisms modulo the scalars by Skolem–Noether.

**The biquaternions over $\mathbb{R}$.** Reading the same set over $\mathbb{R}$ changes the ambient space to $M_8(\mathbb{R})$, of dimension $64$, while the centre becomes the two-dimensional $\mathbb{C}_{\mathbb{B}}$, so the formula gives $8 - 2 = 6$ and

$$
\operatorname{Der}_{\mathbb{R}}(\mathbb{B}) = \operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathfrak{sl}_2(\mathbb{C})_{\mathbb{R}} \cong \mathfrak{so}(3,1),
$$

of real dimension $6$. The automorphism group acquires a second coset from complex conjugation, $\operatorname{Aut}_{\mathbb{R}}(\mathbb{B}) \cong PSL_2(\mathbb{C}) \rtimes \mathbb{Z}/2$, again of dimension $6$.

**The rotations and the boosts.** The six real derivations of $\mathbb{B}$ split into two three-dimensional pieces. Writing $r_k = \mathrm{ad}_{e_k}$ and $b_k = \mathrm{ad}_{i e_k}$ for $k = 1,2,3$, the brackets are

$$
[r_i, r_j] = 2\varepsilon_{ijk} r_k, \qquad [r_i, b_j] = 2\varepsilon_{ijk} b_k, \qquad [b_i, b_j] = -2\varepsilon_{ijk} r_k .
$$

The $r_k$ span a three-dimensional subalgebra isomorphic to $\mathfrak{su}(2) \cong \mathfrak{so}(3)$, the compact rotations. The $b_k$ span a complementary three-dimensional subspace, the non-compact boosts, which is not a subalgebra: the third relation returns a rotation rather than a boost. The minus sign there is what makes the algebra $\mathfrak{so}(3,1)$ rather than $\mathfrak{so}(4)$; for $\mathfrak{so}(4)$ the two pieces would be two copies of $\mathfrak{su}(2)$ closing separately with the same sign. Scaling by $J_k = \tfrac{1}{2}r_k$ and $K_k = \tfrac{1}{2}b_k$ exhibits the standard Lorentz relations. The full details, with the automorphism and derivation computations for both ground fields, are in *Biquaternion Automorphisms and Derivations*.

## Summary

Fixing a $k$-algebra $A$ with $n = \dim_k A$ places every linear operator on $A$ in the one ambient space $\operatorname{End}_k(A) \cong M_n(k)$, of dimension $n^2$, and the classes of operators worth naming are subspaces and groups inside it. A condition linear in the operator defines a subspace: the derivations by the Leibniz rule, the $A$-linear operators as the centralizer of the left multiplications, and the infinitesimal form-preservers. A condition nonlinear in the operator defines a set that is not a subspace, and a group once invertibility is added: the algebra automorphisms, which are the units of the endomorphism monoid, and the groups preserving a form. The derivations are the tangent space of the automorphism group at the identity, so the dimension of the one equals the dimension of the other.

The ladder for the biquaternion algebra inside $M_4(\mathbb{C})$ has the all-operators rung of dimension $16$, the orthogonal rung $\mathfrak{so}(4,\mathbb{C})$ of dimension $6$, the derivations and the pure left multiplications of dimension $3$ each, the left and right multiplication spaces of dimension $4$ each, and the scalars of dimension $1$. The two three-dimensional pieces satisfy $\mathfrak{so}(4,\mathbb{C}) = L(\text{pure}) \oplus \operatorname{Der}_{\mathbb{C}}(\mathbb{B})$, and the left multiplication space is $\mathbb{C}\cdot I$ plus the pure part. The automorphism group $PSL_2(\mathbb{C})$ and the orthogonal group $O(4,\mathbb{C})$ sit inside the ambient space as groups, with the first contained in the second because an automorphism preserves the norm.

The worked case of $\mathbb{C}$ over $\mathbb{R}$ exhibits the whole scheme in the smallest nontrivial dimension. The ambient space $M_2(\mathbb{R})$ has dimension $4$ and splits as $L(\mathbb{C}) \oplus \{\text{conjugate-linear maps}\}$, of dimensions $2 + 2$; the derivations are zero, because $0 = \delta(i^2) = 2i\,\delta(i)$ kills the generator; the automorphisms are $\mathbb{Z}/2$, generated by a reflection; and the Lie algebra $\mathfrak{so}(2)$ of the norm-preserving rotations is spanned by $L(i)$ itself, so that the rotation is generated by multiplication by the imaginary unit and the metric only makes it visible.

Running the same computation over the three two-dimensional algebras shows the derivation dimension to be the invariant that separates them: it is $0$ for $\mathbb{C}$ and $\mathbb{D}$ and $1$ for $\mathbb{D}'$, and the asymmetry is caused by the nilpotent generator of $\mathbb{D}'$, which the Leibniz rule does not obstruct. These three algebras are commutative, so all their inner derivations vanish and $\dim Z(A) = n$ for each; the one-dimensional derivation space of $\mathbb{D}'$ is therefore entirely outer, and it is the case in which the formula $\dim \operatorname{Der} = n - \dim Z(A)$ fails, since it predicts $0$. The formula holds for $\mathbb{H}$ over $\mathbb{R}$ and for $\mathbb{B}$ over $\mathbb{C}$, where it gives $\dim \operatorname{Der} = 3$ with automorphism groups $SO(3)$ and $PSL_2(\mathbb{C})$ respectively, and over $\mathbb{R}$ the biquaternion derivation space is the six-dimensional $\mathfrak{so}(3,1)$, whose split into rotations and boosts is the origin of the Lorentz algebra in this setting.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | Ground field |
| $A$ | Finite-dimensional unital associative $k$-algebra |
| $n = \dim_k A$ | Dimension of $A$ over $k$ |
| $\operatorname{End}_k(A) \cong M_n(k)$ | Ambient space of all $k$-linear operators on $A$ |
| $L(a)$, $L(a)(x) = ax$ | Left multiplication by $a$ |
| $R(a)$, $R(a)(x) = xa$ | Right multiplication by $a$ |
| $L(A)$, $R(A)$ | Subspaces of left and right multiplications, dimension $n$ |
| $\operatorname{Der}_k(A)$ | Lie algebra of $k$-derivations of $A$ |
| $\mathrm{ad}_a(x) = [a,x]$ | Inner derivation by $a$ |
| $\operatorname{InnDer}_k(A) \cong A/Z(A)$ | Inner derivations; all derivations when $A$ is separable |
| $\operatorname{Aut}_k(A)$ | Group of $k$-algebra automorphisms of $A$ |
| $Z(A)$ | Centre of $A$, a subspace of $A$ |
| $\exp(\delta)$ | Exponential of a nilpotent derivation, an automorphism |
| $O(G)$ | Operators preserving the form with Gram matrix $G$ |
| $T(Q) = Q^{\mathsf T}$ | Transpose, a unital norm-preserving anti-automorphism of $\mathbb{B}$ |
| $\mathfrak{so}(n,\mathbb{C})$, $\mathfrak{so}(n)$ | Lie algebras of skew operators |
| $r_k = \mathrm{ad}_{e_k}$, $b_k = \mathrm{ad}_{ie_k}$ | Rotations and boosts in $\operatorname{Der}_{\mathbb{R}}(\mathbb{B})$ |
| $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{B}$ | Real, complex, quaternion and biquaternion algebras |
| $\mathbb{D}$, $\mathbb{D}'$ | Split complex numbers and dual numbers |
| $N$ | Norm form of the algebra and determinant of the multiplication matrix |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for derivations, their Lie algebra structure and the exponential.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for automorphisms, derivations and the centralizer of the regular representation.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for endomorphism rings, the centralizer description and the regular module.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the centralizer and the double centralizer theorems.
- I. N. Herstein, *Noncommutative Rings* (Carus Mathematical Monographs 15, MAA, 1968), for the Skolem–Noether theorem and central simple algebras.
- Gerhard Hochschild, *On the cohomology groups of an associative algebra* (Annals of Mathematics 46, 1945), for the identification of the first cohomology with the derivations and the vanishing for separable algebras.
- Murray Gerstenhaber, *On the deformation of rings and algebras* (Annals of Mathematics 79, 1964), for the reading of the higher cohomology as deformations.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the groups preserving a form on an algebra.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the quaternion and biquaternion computations used in the examples.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the relation of the biquaternion derivations to the Lorentz algebra.
