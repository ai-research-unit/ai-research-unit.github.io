
# __Real Exponential and Lie Group Structure__

## Introduction

The real algebra $\mathbb{R}$ is a one-dimensional real vector space with a commutative multiplication, and it is simultaneously a Lie algebra and, through its unit group, a Lie group. This article develops the two structures and the exponential map that joins them. The exponential $\exp(x) = e^x$ is the base case of the exponential of the family: it is an isomorphism of the additive group onto the positive reals, its kernel is trivial, and its image is exactly the identity component of the group of units.

The real case is the degenerate abelian base. The bracket vanishes identically, so $\mathbb{R}$ is the abelian Lie algebra $\mathfrak{gl}_1(\mathbb{R})$ of dimension one, and the Baker–Campbell–Hausdorff series terminates at its leading term, making the exponential an exact group homomorphism. The group of units is disconnected, and the exponential covers only its identity component; the sign group is left over as the torsion of the unit group.

The conventions are those of *Real Algebra*: basis $e_0 = 1$, a general element $x = x e_0$, the sole involution the identity, norm form $N(x) = x\,x = x^2$. The comparison throughout is with the complex algebra $\mathbb{C}$, for which $\exp : \mathbb{C} \to \mathbb{C}^\times$ is a surjective homomorphism with kernel $2\pi i\,\mathbb{Z}$, with the quaternions $\mathbb{H}$, and with the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, for which the exponential is neither injective nor a homomorphism. Every numerical value displayed below is exact.

## The Algebra as the Abelian Lie Algebra

The commutator bracket of $\mathbb{R}$ vanishes identically,

$$
[x, y] = xy - yx = 0 \qquad (x, y \in \mathbb{R}),
$$

because the algebra is commutative. Hence $\mathbb{R}$ is an **abelian Lie algebra** of real dimension $1$. It is in fact the general linear Lie algebra of the one-dimensional real vector space,

$$
\mathfrak{gl}_1(\mathbb{R}) = M_1(\mathbb{R}) \cong \mathbb{R},
$$

the Lie algebra of $1\times1$ real matrices with the commutator bracket, which is zero because $1\times1$ matrices commute.

**Theorem.** $\mathbb{R}$ is the Lie algebra of the additive group $(\mathbb{R}, +)$ and of the positive multiplicative group $(\mathbb{R}_{>0}, \cdot)$; it is abelian of dimension $1$, and the two groups share it as their Lie algebra.

**Proof.** Both groups are real Lie groups of dimension $1$ and are abelian, so their Lie algebras are one-dimensional with zero bracket, hence isomorphic to $\mathbb{R}$ with the zero bracket, which is $\mathfrak{gl}_1(\mathbb{R})$ above. The tangent space at the identity of each is the same line $\mathbb{R}$. $\square$

The universal enveloping algebra of this abelian Lie algebra is the polynomial algebra $\mathbb{R}[X]$ on one generator, the base case of the Poincaré–Birkhoff–Witt theorem. The centre of the Lie algebra is the whole algebra, and every subspace is an abelian ideal; the algebra is the simplest possible Lie algebra, and every bracket identity of the family reduces to $0 = 0$ here.

## The Group of Units

The **group of units** is

$$
\mathbb{R}^\times = \{x : N(x) \neq 0\} = \mathbb{R} \setminus \{0\},
$$

the real line with the origin removed. It is a real Lie group of dimension $1$, open and dense in $\mathbb{R}$ by *Real Norm and Invertibility*, and it **decomposes into two components**,

$$
\mathbb{R}^\times = \mathbb{R}_{>0} \sqcup \mathbb{R}_{<0}, \qquad \pi_0(\mathbb{R}^\times) \cong \{\pm1\}.
$$

The identity component is the positive ray $\mathbb{R}_{>0}$, a connected, contractible, non-compact group; the other component is the negative ray $-\mathbb{R}_{>0}$. The group is abelian, so its Lie algebra is $\mathbb{R}$ itself with the zero bracket, and the group of units splits as

$$
\mathbb{R}^\times \cong \mathbb{R}_{>0} \times \{\pm1\},
$$

the product of the identity component and the component group. In the complex and quaternion cases the unit group has one component, the second factor being the connected circle $U(1)$ or sphere $S^3$; here the second factor is the discrete sign group, and the disconnectedness is the distinctive feature of the real base.

## The Exponential: Series and Closed Form

**Definition.** The **exponential** of a real number $x$ is the sum of the convergent series

$$
\exp(x) = \sum_{n \geq 0} \frac{x^n}{n!} .
$$

Since $|x^n/n!| \leq |x|^n/n!$, the series converges absolutely for every real $x$; the exponential is thus defined on all of $\mathbb{R}$. Its closed form is the classical one,

$$
\exp(x) = e^{x}, \qquad e = \exp(1) = \sum_{n\ge0} \frac{1}{n!} .
$$

**Basic properties.** The exponential never vanishes, so it takes values in $\mathbb{R}^\times$:

$$
\exp(x) > 0 \qquad \text{for all} \ x \in \mathbb{R}, \qquad \exp(-x) = \exp(x)^{-1}.
$$

Its norm form is positive and satisfies

$$
N(\exp x) = e^{2x} = \exp(2x),
$$

the square of the exponential itself. The differential at the origin is the identity, $d\exp_0 = \operatorname{id}$, so $\exp$ is a local diffeomorphism near $0$ and supplies exponential coordinates near the identity; as the kernel computation below shows, it is in fact a global homeomorphism onto its image.

## The Group Law

The exponential is a **homomorphism** from the additive group of the Lie algebra to the multiplicative group of the units:

**Theorem.** For all $x, y \in \mathbb{R}$,

$$
\exp(x+y) = \exp(x)\exp(y).
$$

**Proof.** The real numbers commute, so $x$ and $y$ generate a commutative subalgebra, and the binomial theorem reorders the product of the two absolutely convergent series term by term into the series of $\exp(x+y)$; explicitly, the coefficient of the $n$-th power of the combined series is $\sum_{k} \frac{1}{k!(n-k)!} x^k y^{n-k} = \frac{(x+y)^n}{n!}$. $\square$

This is the sharp difference from the biquaternion algebra, where the exponential is not a homomorphism and the failure is measured by the Baker–Campbell–Hausdorff series $\exp(a)\exp(b) = \exp(a+b+\tfrac12[a,b]+\cdots)$. Here every bracket in that series vanishes, so the series terminates at the leading term and the identity is exact without any smallness hypothesis. The general form reduces to the commuting case, which for $\mathbb{B}$ is the special case $[a,b] = 0$; for $\mathbb{R}$ the commuting case is the only case. The complex case is the same, one dimension up.

## Surjectivity, Kernel and the Logarithm

**Theorem (the image).** The exponential maps $\mathbb{R}$ bijectively onto the positive reals:

$$
\exp(\mathbb{R}) = \mathbb{R}_{>0}, \qquad \exp : (\mathbb{R}, +) \longrightarrow (\mathbb{R}_{>0}, \cdot) \ \text{is an isomorphism of Lie groups.}
$$

**Proof.** The exponential is a strictly increasing continuous function with $\lim_{x\to-\infty}e^x = 0$ and $\lim_{x\to+\infty}e^x = +\infty$, so its image is exactly $(0,\infty)$ and it is injective. It is a group homomorphism by the group law, and a bijective homomorphism of groups is an isomorphism; it is smooth with smooth inverse $\ln$, so it is an isomorphism of Lie groups. $\square$

The inverse is the **natural logarithm**,

$$
\ln : \mathbb{R}_{>0} \longrightarrow \mathbb{R}, \qquad \ln x = \int_1^x \frac{dt}{t},
$$

and the reconstruction $\exp(\ln r) = r$ is exact for every $r > 0$. The exponential is therefore **not surjective onto $\mathbb{R}^\times$**: the negative reals are not in its image, because $e^x > 0$ always, so the image is exactly the identity component of the unit group. This is the base case of the restriction of the image to the identity component; the complex, quaternion and biquaternion exponentials all reach their whole unit group, so a two-component unit group with a one-component exponential image is the distinctive feature of the real base, and its obstruction is exactly the sign.

**Theorem (the kernel).** For $x \in \mathbb{R}$ one has $\exp(x) = 1$ if and only if $x = 0$; hence

$$
\ker\exp = \{0\}.
$$

**Proof.** $e^x = 1$ with $x \neq 0$ is impossible, since $e^x > 1$ for $x > 0$ and $0 < e^x < 1$ for $x < 0$. $\square$

The kernel is trivial, so the exponential is injective and the real logarithm has no ambiguity. The biquaternion kernel is very much larger: it is not discrete, it is not a subgroup, and in its coordinates the conditions $Q_0 \in \pi i\mathbb{Z}$, $B \in \pi\mathbb{Z}$ with $Q_0$ and $B$ congruent modulo one another appear; the complex kernel is the discrete lattice $2\pi i\,\mathbb{Z}$. The real kernel is the smallest possible, the trivial subgroup, and every positive real has exactly one real logarithm.

## One-Parameter Subgroups and the Sign Group

**Definition.** A **one-parameter subgroup** of a Lie group $G$ is a continuous homomorphism $\gamma : \mathbb{R} \to G$, the group $\mathbb{R}$ being additive. For a real algebra it is written $\gamma(t) = \exp(tX)$ for a fixed $X$ in the Lie algebra.

**Proposition.** The one-parameter subgroups of $\mathbb{R}^\times$ are exactly the maps

$$
\gamma_X(t) = \exp(tX), \qquad X \in \mathbb{R}, \quad t \in \mathbb{R},
$$

and $\gamma_X$ determines $X$ through its derivative at $t = 0$. Every one-parameter subgroup takes values in the identity component $\mathbb{R}_{>0}$.

**Proof.** Each $\gamma_X$ is a homomorphism by the exponential identity $\exp((s+t)X) = \exp(sX)\exp(tX)$, and it is smooth. Conversely a one-parameter subgroup is determined by its derivative at $0$, which lies in the Lie algebra $\mathbb{R}$, since the group is abelian and exponential coordinates are available near the identity. A one-parameter subgroup is the image of the connected group $\mathbb{R}$, hence connected, so it lies in the identity component. $\square$

**The scale as the one-parameter group.** The subgroup generated by $X = 1$ is

$$
\gamma_1(t) = e^{t} \in \mathbb{R}_{>0},
$$

and this map $\gamma_1 : \mathbb{R} \to \mathbb{R}_{>0}$ is a bijective Lie group homomorphism. Hence

$$
\mathbb{R}_{>0} \cong \mathbb{R},
$$

a bijection of topological groups. The two one-parameter subgroups for $X$ and $-X$ are inverse to each other, and the whole family $\gamma_X$, $X \neq 0$, is obtained from $\gamma_1$ by the reparametrisation $t \mapsto Xt$.

**The sign group is not generated by the exponential.** The sign group $\{\pm1\}$ is **not** in the image of any one-parameter subgroup: every $\gamma_X(t)$ is positive. It is instead the **torsion subgroup** of $\mathbb{R}^\times$,

$$
\{x \in \mathbb{R}^\times : x^n = 1 \ \text{for some} \ n \geq 1\} = \{\pm1\},
$$

the elements of finite order. The sign group is thus the group of components $\pi_0(\mathbb{R}^\times)$, the maximal compact subgroup of $\mathbb{R}^\times$, and the two-element group $O(1)$, all at once. In the complex case the corresponding group of components is trivial, its compact subgroup $U(1)$ is nontrivial and connected, and the torsion of $\mathbb{C}^\times$ is the group of all roots of unity, $\mu_\infty \cong \mathbb{Q}/\mathbb{Z}$, a countable dense subgroup of $U(1)$; here the torsion is the two-element sign group and nothing else.

## Connectedness and the Compact Subgroup

**Theorem.** $\mathbb{R}^\times$ is disconnected, with two components; its identity component is $\mathbb{R}_{>0}$, it has no compact connected subgroup of positive dimension, and its maximal compact subgroup is the finite group $\{\pm1\}$.

**Proof.** The decomposition $\mathbb{R}^\times = \mathbb{R}_{>0} \sqcup \mathbb{R}_{<0}$ is a separation into two non-empty open sets, so $\mathbb{R}^\times$ is disconnected; each piece is an open interval, hence connected, so there are exactly two components and the identity component is $\mathbb{R}_{>0}$. A compact connected subgroup of positive dimension would contain a one-parameter subgroup with nontrivial compact image, but every one-parameter subgroup of $\mathbb{R}^\times$ is the non-compact positive ray or all of the line, so none is compact. The maximal compact subgroup is therefore the finite group $\{\pm1\}$. $\square$

The fundamental group of the unit group is the fundamental group of its components, each a contractible line:

$$
\pi_1(\mathbb{R}^\times) = 0, \qquad \pi_n(\mathbb{R}^\times) = 0 \ \ (n \geq 1).
$$

The complex unit group has $\pi_1 \cong \mathbb{Z}$ generated by the loop around the origin, the quaternion unit group has $\pi_1 = 0$ and $\pi_3 \cong \mathbb{Z}$, and the biquaternion unit group has $\pi_1 \cong \mathbb{Z}$ and $\pi_3 \cong \mathbb{Z}$; the real unit group is the case in which every homotopy group vanishes, because there is no compact connected factor to wind around.

## Comparison with the Complex, Quaternion and Biquaternion Lie Algebra and Lie Group Structure

The cases are tabulated; the field is named in the entries that depend on it.

| Structure | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{B}$ |
|---|---|---|---|
| Algebra as Lie algebra | abelian, real dimension $1$; bracket $0$ | abelian, real dimension $2$; bracket $0$ | $\mathfrak{gl}(2,\mathbb{C})$, real dimension $8$; bracket $\neq 0$ |
| Group of units | $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$, two components, abelian | $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$, connected, abelian | $\mathbb{B}^\times \cong GL(2,\mathbb{C})$, connected, non-abelian |
| Exponential | entire, homomorphism, injective | entire, homomorphism, not injective | entire, not a homomorphism |
| Image of $\exp$ | $\mathbb{R}_{>0}$, the identity component | $\mathbb{C}^\times$, the whole group | $GL(2,\mathbb{C})$, the whole group |
| Kernel of $\exp$ | $\{0\}$ | $2\pi i\,\mathbb{Z} \cong \mathbb{Z}$ | non-discrete subset of $\mathfrak{gl}(2,\mathbb{C})$, not a subgroup |
| Torsion of the unit group | $\{\pm1\}$, the sign group | the roots of unity $\mu_\infty \cong \mathbb{Q}/\mathbb{Z}$ | the finite-order elements of $GL(2,\mathbb{C})$ |
| Norm-one group | $\{\pm1\} = O(1)$, finite | $U(1) \cong SO(2)$, compact, dimension $1$ | $SL(2,\mathbb{C})$, non-compact |
| Maximal compact subgroup | $\{\pm 1\}$, dimension $0$ | $U(1) \cong S^1$ | $U(2) \cong S^1 \times S^3$ |
| Homotopy | all $\pi_n = 0$ | $\pi_1 \cong \mathbb{Z}$, $\pi_n = 0$ ($n \ge 2$) | $\pi_1 \cong \mathbb{Z}$, $\pi_3 \cong \mathbb{Z}$ |

Every exponential is entire and satisfies a group law; the differences are that the real exponential is injective with trivial kernel, that its image is only the identity component of the unit group rather than the whole group, and that its maximal compact subgroup is finite rather than a positive-dimensional torus. The real case is the completely reducible abelian base of the family, and its exponential is the base case of the isomorphism between an additive Lie algebra and a multiplicative Lie group.

## Summary

The commutator bracket of $\mathbb{R}$ vanishes identically, so $\mathbb{R} \cong \mathfrak{gl}_1(\mathbb{R})$ is an abelian Lie algebra of real dimension $1$, with the universal enveloping algebra the polynomial algebra on one generator, and it is the Lie algebra both of the additive group $(\mathbb{R},+)$ and of the positive multiplicative group $(\mathbb{R}_{>0},\cdot)$.

The exponential $\exp(x) = \sum x^n/n!$ is entire, never zero, and a group homomorphism, $\exp(x+y) = \exp x \exp y$ exactly, because the Baker–Campbell–Hausdorff series terminates at the leading term. Its closed form is $e^x$, its norm form is $N(\exp x) = e^{2x}$, it is injective with kernel $\{0\}$, and it maps $(\mathbb{R},+)$ isomorphically onto $(\mathbb{R}_{>0},\cdot)$ with inverse the natural logarithm. It is not surjective onto $\mathbb{R}^\times$, its image being exactly the identity component.

The group of units is $\mathbb{R}^\times = \mathbb{R}_{>0}\sqcup\mathbb{R}_{<0}$, with two components and the splitting $\mathbb{R}^\times \cong \mathbb{R}_{>0}\times\{\pm1\}$. Every one-parameter subgroup is $t \mapsto \exp(tX)$ and takes values in $\mathbb{R}_{>0}$, so it never reaches the sign group; the sign group is the torsion subgroup of $\mathbb{R}^\times$, its group of components, and its maximal compact subgroup, and it is the compact factor $O(1)$ of the family. The real case is the abelian base of the family: the whole structure is a line, its exponential, and a two-element sign.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, basis $e_0 = 1$ |
| $[x,y] = xy - yx = 0$ | the commutator bracket, identically zero |
| $\mathfrak{gl}_1(\mathbb{R}) \cong \mathbb{R}$ | the abelian Lie algebra of the $1\times1$ matrices |
| $\mathbb{R}^\times = \mathbb{R}\setminus\{0\}$ | the group of units, two components |
| $\exp(x) = \sum_n x^n/n! = e^x$ | the exponential, entire and a homomorphism |
| $N(\exp x) = e^{2x}$ | the norm form of an exponential |
| $\exp : (\mathbb{R},+)\to(\mathbb{R}_{>0},\cdot)$ | the isomorphism onto the positive reals |
| $\ln = \exp^{-1}$ | the natural logarithm |
| $\ker\exp = \{0\}$ | the kernel, trivial |
| $\{\pm1\} = O(1)$ | the sign group, the torsion subgroup of $\mathbb{R}^\times$ |
| $\mathbb{R}^\times \cong \mathbb{R}_{>0}\times\{\pm1\}$ | the splitting of the unit group |
| $\gamma_X(t) = \exp(tX)$ | a one-parameter subgroup, $X$ in the Lie algebra |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd edition (Springer, 2015), for the exponential map, its kernel and its surjectivity on the classical groups.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential as an isomorphism $\mathbb{R} \cong \mathbb{R}_{>0}$ and the one-parameter subgroups of the line.
- Walter Rudin, *Principles of Mathematical Analysis*, 3rd edition (McGraw-Hill, 1976), for the exponential and the logarithm as inverse functions.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Springer, Lecture Notes in Mathematics 1500, 1992), for the Baker–Campbell–Hausdorff series and the abelian case in which it terminates.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the exponentials of the normed division algebras and the failure of surjectivity.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the exponential of the higher-dimensional algebras.
