
# __Complex Exponential and Lie Group Structure__

## Introduction

This article develops the Lie theory of the complex algebra $\mathbb{C}$. *Complex Algebra* defined the algebra, its single nontrivial involution and its two distinguished subspaces; *Complex Norm and Invertibility* identified the norm $N(A) = A\bar{A} = |A|^2$ and the group of units $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$; and the companion articles on the elementary and polar structure computed the exponential and the polar form by power series. Here these are assembled into the standard theory of $\mathbb{C}$ as an abelian Lie algebra, of $\mathbb{C}^\times$ as a Lie group, and of the exponential map.

The complex case is the degenerate base of the family and everything below is correspondingly simple. The algebra is commutative, so its commutator bracket vanishes identically, its Lie algebra is abelian, the Baker–Campbell–Hausdorff series terminates at the first term, the exponential is a homomorphism, and the exponential map is both surjective and locally bijective. The whole of the structure is the product of a line and a circle.

Every statement is a special case of the standard theory of the abelian Lie group $\mathbb{R}^n$ and the circle group, and the passage to the real two-dimensional algebra is the identification $\mathbb{C} \cong \mathbb{R}^2$. Throughout, a complex number is written $A = a + i a'$ with $a, a' \in \mathbb{R}$, the norm is $N(A) = a^2+a'^2$, and the imaginary unit satisfies $i^2 = -1$. The dimension statements name the field, since $\mathbb{C}$ is one-dimensional over $\mathbb{C}$ and two-dimensional over $\mathbb{R}$.

## The Algebra as the Abelian Lie Algebra

**The commutator bracket.** The algebra $\mathbb{C}$ carries the commutator bracket

$$
[A, B] = AB - BA .
$$

Because $\mathbb{C}$ is commutative, the bracket vanishes identically:

$$
[A, B] = 0 \qquad (A, B \in \mathbb{C}),
$$

so $\mathbb{C}$ is an **abelian Lie algebra**.

**Dimension.** As a real Lie algebra, $\mathbb{C} \cong \mathbb{R}^2$ has dimension $2$; as a complex Lie algebra it has dimension $1$. The two views are the realification and the $\mathbb{C}$-form of one object.

**The centre and the bracket decomposition.** Every element is central, so the centre is all of $\mathbb{C}$, and there is no nontrivial bracket decomposition. In the biquaternion algebra the corresponding space is $\mathrm{GL}(2,\mathbb{C})$ with the decomposition $\mathrm{GL}(2,\mathbb{C}) = \mathrm{SL}(2,\mathbb{C}) \oplus \mathbb{C} 1$, a three-dimensional simple part and a one-dimensional centre over $\mathbb{C}$ (six- and two-dimensional over $\mathbb{R}$); here the simple part is empty and the centre is everything, and the real Lie algebra has dimension $2$.

**The universal enveloping algebra.** Since the bracket vanishes, the universal enveloping algebra of $\mathbb{C}$ as a real Lie algebra is the symmetric algebra on the two-dimensional space $\mathbb{C}$, i.e. the polynomial algebra $\mathbb{R}[x,y]$ on two commuting variables. There is no non-commutativity to encode. In the biquaternion case the corresponding object is the universal enveloping algebra of $\mathrm{GL}(2,\mathbb{C})$, which does carry the bracket.

## The Group of Units

The **group of units** of $\mathbb{C}$ is the set of invertible elements,

$$
\mathbb{C}^\times = \{A \in \mathbb{C} : N(A) \neq 0\} = \mathbb{C} \setminus \{0\},
$$

a group under multiplication with identity $1$, abelian, and at the same time a real Lie group.

**Dimension, openness and density.** As a real manifold $\mathbb{C}^\times$ has dimension $2$; it is open in $\mathbb{C}$ (the preimage $N^{-1}((0,\infty))$ of an open set) and dense, its complement being the single point $\{0\}$, of real dimension $0$. It is connected and non-compact, and its centre is itself, since the group is abelian.

**Lie algebra.** The Lie algebra of $\mathbb{C}^\times$ is $\mathbb{C}$ itself with the zero bracket, because the units are an open subset of $\mathbb{C}$ so that the tangent space at the identity is the whole algebra. The inverse map $\iota(A) = A^{-1}$ has differential $-\operatorname{id}$ at the identity, the infinitesimal reason an abelian bracket is antisymmetric; and the bracket is zero because the group is abelian. In the biquaternion case the Lie algebra is $\mathrm{GL}(2,\mathbb{C})$ and the tangent space is the whole of $\mathbb{B}$ as well, but the bracket there does not vanish.

**The norm-one group.** Because $N$ is multiplicative and $N(1) = 1$, the level set

$$
\mathbb{C}^\times_1 = \{A \in \mathbb{C} : N(A) = 1\} = U(1) = \{A : |A| = 1\}
$$

is a subgroup of $\mathbb{C}^\times$: the **unit circle group** $U(1)$. It is compact, connected, of real dimension $1$, and it is the maximal compact subgroup of $\mathbb{C}^\times$. Unlike the biquaternion norm-one group $\mathbb{B}^\times_1 \cong SL(2,\mathbb{C})$, which is non-compact, the complex norm-one group is compact; the reason is the definiteness of the norm.

## The Exponential: Series and Closed Form

The **exponential** of a complex number is defined by the power series

$$
\exp(A) = \sum_{n=0}^{\infty} \frac{A^n}{n!}.
$$

Convergence is absolute and locally uniform in the Euclidean norm, so $\exp$ is an entire function on $\mathbb{C} \cong \mathbb{R}^2$.

**Closure of the formula.** Splitting $A = a + i a'$ and using the absolute convergence of the series to rearrange the terms,

$$
\exp(a+i a') = \exp(a)\exp(i a') = e^{a}\bigl(\cos a' + i \sin a'\bigr) = e^{a}e^{i a'},
$$

the **Euler formula** $e^{a'i} = \cos a' + i \sin a'$ being the closed form of the series with purely imaginary argument. There is only one regime: the algebra has no nilpotent directions of the kind that truncate the biquaternion series, because the form $N$ is definite and the only nilpotent element is $0$.

**Basic properties.** The exponential never vanishes, so it takes values in $\mathbb{C}^\times$:

$$
\exp(A) \neq 0 \qquad \text{for all} \ A \in \mathbb{C}, \qquad \exp(-A) = \exp(A)^{-1}.
$$

Its norm is

$$
N(\exp A) = e^{2a} = e^{\operatorname{Tr}(A)},
$$

where $\operatorname{Tr}(A) = 2a$ is the algebra trace; and $d\exp_0 = \operatorname{id}$, so $\exp$ is a local diffeomorphism near $0$ and supplies exponential coordinates near the identity. In particular $\exp$ is a local bijection but, as the kernel computation below shows, not a global one.

## The Group Law

The exponential is a **homomorphism** from the additive group of the Lie algebra to the multiplicative group of the units:

**Theorem.** For all $A, B \in \mathbb{C}$,

$$
\exp(A+B) = \exp(A)\exp(B).
$$

**Proof.** The complex numbers commute, so $A$ and $B$ generate a commutative subalgebra, and the binomial theorem reorders the product of the two absolutely convergent series term by term into the series of $\exp(A+B)$; explicitly, the coefficient of the $n$-th power of the combined series is $\sum_{k} \frac{1}{k!(n-k)!} A^k B^{n-k} = \frac{(A+B)^n}{n!}$.

This is the sharp difference from the biquaternion algebra, where the exponential is not a homomorphism and the failure is measured by the Baker–Campbell–Hausdorff series $\exp(a)\exp(b) = \exp(a+b+\tfrac12[a,b]+\cdots)$. Here every bracket in that series vanishes, so the series terminates at the leading term and the identity is exact without any smallness hypothesis. The general form reduces to the commuting case, which for $\mathbb{B}$ is the special case $[a,b] = 0$; for $\mathbb{C}$ the commuting case is the only case.

## Surjectivity, Kernel and the Logarithm

**Theorem (surjectivity).** The exponential maps $\mathbb{C}$ onto $\mathbb{C}^\times$:

$$
\exp(\mathbb{C}) = \mathbb{C}^\times, \qquad \mathbb{C}^\times = \{\exp(A) : A \in \mathbb{C}\}.
$$

**Proof.** Every nonzero complex number has a polar form $A = re^{i\theta}$ with $r = |A| > 0$ and $\theta \in \mathbb{R}$, so with $L = \ln r + i\theta$ one has $\exp(L) = e^{\ln r}e^{i\theta} = re^{i\theta} = A$.

The element $L$ is a **complex logarithm** of $A$. The construction is unique up to the kernel of $\exp$.

**Theorem (kernel).** For $A \in \mathbb{C}$ one has $\exp(A) = 1$ if and only if $A \in 2\pi i\,\mathbb{Z}$.

**Proof.** Write $A = a+i a'$; then $\exp(A) = e^{a}e^{i a'} = 1$ forces $e^{a} = 1$, hence $a = 0$, and $e^{i a'} = 1$, hence $a' \in 2\pi\mathbb{Z}$. Thus $A = 2\pi i k$ for some integer $k$.

The kernel is therefore the discrete infinite cyclic subgroup

$$
\ker\exp = 2\pi i\,\mathbb{Z} \cong \mathbb{Z},
$$

of real dimension $0$. The biquaternion kernel is very much larger: it is not discrete, it is not an additive subgroup, and in its coordinates the conditions $Q_0 = \pi i k$, $B = \pi j$ with $k \equiv j \pmod 2$ appear. Here the kernel is a lattice of points on the imaginary axis, and the ambiguity of the logarithm is the addition of $2\pi i k$. The **principal logarithm**, $\operatorname{Log} A = \ln|A| + i \operatorname{Arg} A$ with $\operatorname{Arg} A \in (-\pi,\pi]$, selects one representative and is holomorphic on the cut plane, as developed in *Complex Analysis*.

## Polar and Exponential Parametrisation

Both parametrisations apply to an element of $\mathbb{C}^\times$, i.e. to a nonzero complex number; the only element with no parametrisation is $0$.

**Polar form.** Every $A \neq 0$ is

$$
A = r\,u, \qquad r = |A| = \sqrt{N(A)} \in \mathbb{R}_{>0}, \qquad u = \frac{A}{|A|} \in U(1),
$$

with $r$ the modulus and $u$ the phase, and the decomposition is unique. Writing $u = e^{i\theta}$ gives $A = re^{i\theta}$. This is the splitting $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1)$ of the group of units, developed in *Complex Norm and Invertibility*.

**Exponential parametrisation.** By surjectivity, every $A \in \mathbb{C}^\times$ is $A = \exp(L)$ for some $L \in \mathbb{C}$, with $L = \ln r + i\theta$ and the ambiguity of the kernel. In the two factors the logarithm splits as

$$
A = \underbrace{\exp(\ln r)}_{r \in \mathbb{R}_{>0}} \underbrace{\exp(i\theta)}_{u \in U(1)},
$$

the product of a positive real scale, obtained from the real part of $L$, and a phase, obtained from the imaginary part. The splitting is the polar decomposition written in exponential coordinates, and it is exact, not a local statement, because the exponential is a homomorphism.

**The exponential is not one-to-one.** It restricts to a bijection on the strip $|\operatorname{Im} A| \le \pi$ with the identification $\operatorname{Im} A = \pm\pi$, and to a bijection on a real line $\mathbb{R} 1$ of scales; the many-to-one character is entirely the kernel $2\pi i \mathbb{Z}$ along the imaginary axis.

## One-Parameter Subgroups and the Circle Group

**Definition.** A **one-parameter subgroup** of a Lie group $G$ is a continuous homomorphism $\gamma : \mathbb{R} \to G$, the group $\mathbb{R}$ being additive. For a real algebra it is written $\gamma(t) = \exp(tX)$ for a fixed $X$ in the Lie algebra.

**Proposition.** The one-parameter subgroups of $\mathbb{C}^\times$ are exactly the maps

$$
\gamma_X(t) = \exp(tX), \qquad X \in \mathbb{C}, \quad t \in \mathbb{R},
$$

and $\gamma_X$ determines $X$ through its derivative at $t = 0$.

**Proof.** Each $\gamma_X$ is a homomorphism by the exponential identity $\exp((s+t)X) = \exp(sX)\exp(tX)$, and it is smooth. Conversely a one-parameter subgroup is determined by its derivative at $0$, which lies in the Lie algebra $\mathbb{C}$, since the group is abelian and exponential coordinates are available near the identity.

**The circle as a one-parameter group.** The subgroup generated by $X = i$ is

$$
\gamma_i(t) = e^{it} = \cos t + i\sin t \in U(1),
$$

and this map $\gamma_i : \mathbb{R} \to U(1)$ is a surjective Lie group homomorphism with kernel $2\pi\mathbb{Z}$. Hence

$$
U(1) \cong \mathbb{R}/2\pi\mathbb{Z} = \mathbb{R}/\mathbb{Z}\cdot 2\pi,
$$

a bijection of topological groups. The circle $U(1)$ is the compact connected one-dimensional Lie group, and it is isomorphic to the rotation group of the plane,

$$
U(1) \cong SO(2).
$$

**The identification with $SO(2)$.** The rotation of the plane through the angle $\theta$ is the multiplication map $A \mapsto e^{i\theta}A$, so the map $U(1) \to SO(2)$ sending $e^{i\theta}$ to the rotation through $\theta$ is an isomorphism of Lie groups; it is an isomorphism and not a covering, because the rotation group of the plane is itself a circle. This is the elementary base case of the double covers of the higher-dimensional rotation groups: the unit quaternions double-cover $SO(3)$ and the unit-norm biquaternions double-cover the proper orthochronous Lorentz group $SO^+(1,3)$, but the circle covers $SO(2)$ once.

**The scale subgroup.** The subgroup generated by $X = 1$ is $\gamma_1(t) = e^{t} \in \mathbb{R}_{>0}$, and $t \mapsto e^{t}$ is an isomorphism $\mathbb{R} \cong \mathbb{R}_{>0}$ of Lie groups. Together,

$$
\mathbb{C}^\times \cong \mathbb{R} \times (\mathbb{R}/2\pi\mathbb{Z}) \cong \mathbb{R}_{>0} \times U(1),
$$

the product of the scale line and the phase circle, and the exponential $\exp : \mathbb{C} \to \mathbb{C}^\times$ is the product of the two isomorphisms $\mathbb{R} \cong \mathbb{R}_{>0}$ and $\mathbb{R} \to U(1)$, with the second many-to-one.

## Connectedness and the Compact Subgroup

**Theorem.** $\mathbb{C}^\times$ is connected but not simply connected; its maximal compact subgroup is $U(1)$, and $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1)$ deformation retracts onto $U(1)$.

**Proof.** The product $\mathbb{R}_{>0} \times U(1)$ of the connected groups $\mathbb{R}_{>0}$ and $U(1)$ is connected, and the two factors are connected, so $\mathbb{C}^\times$ is connected. The map $(r, u) \mapsto u$ is a continuous retraction onto the compact subgroup $U(1)$, and the homotopy $((r,u),t) \mapsto ((1-t)r + t, u)$ deforms the identity to it, so $\mathbb{C}^\times$ deformation retracts onto $U(1)$. The circle is not simply connected, so neither is $\mathbb{C}^\times$.

The fundamental group is computed in *Complex Topology*: $\pi_1(\mathbb{C}^\times) \cong \pi_1(U(1)) \cong \mathbb{Z}$, generated by the loop $t \mapsto e^{it}$, and $\pi_n(\mathbb{C}^\times) = 0$ for $n \ge 2$. In the biquaternion case the corresponding maximal compact subgroup is $U(2) \cong S^1 \times S^3$, of real dimension $4$, with $\pi_1 \cong \mathbb{Z}$ and $\pi_3 \cong \mathbb{Z}$; here the compact factor is the single circle, and only the first homotopy group survives.

## Comparison with the Biquaternion Lie Theory

The two cases are tabulated; the field is named in the entries that depend on it.

| Structure | $\mathbb{C}$ | $\mathbb{B}$ |
|---|---|---|
| Algebra as Lie algebra | abelian, real dimension $2$; bracket $0$ | $\mathrm{GL}(2,\mathbb{C})$, real dimension $8$; bracket $\neq 0$ |
| Group of units | $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$, real dimension $2$, abelian | $\mathbb{B}^\times \cong GL(2,\mathbb{C})$, real dimension $8$, non-abelian |
| Exponential | entire, homomorphism $\mathbb{C} \to \mathbb{C}^\times$ | entire, not a homomorphism |
| Group law | $\exp(A+B) = \exp A \exp B$ exactly | BCH series with $[a,b] \neq 0$ |
| Kernel of $\exp$ | $2\pi i\,\mathbb{Z}$, discrete, $\cong \mathbb{Z}$ | non-discrete subset of $\mathrm{GL}(2,\mathbb{C})$, not a subgroup |
| Surjectivity | onto $\mathbb{C}^\times$ | onto $GL(2,\mathbb{C})$ |
| Norm-one group | $U(1) \cong SO(2)$, compact, dimension $1$ | $SL(2,\mathbb{C})$, non-compact, real dimension $6$ |
| Maximal compact subgroup | $U(1) \cong S^1$ | $U(2) \cong S^1 \times S^3$ |
| Homotopy | $\pi_1 \cong \mathbb{Z}$, $\pi_n = 0$ ($n \ge 2$) | $\pi_1 \cong \mathbb{Z}$, $\pi_3 \cong \mathbb{Z}$ |

Both exponentials are surjective onto the units and both have a locally bijective character; the differences are that the complex exponential is a global homomorphism, that its kernel is a discrete lattice rather than a non-discrete subset, and that its norm-one group and maximal compact subgroup are one-dimensional rather than three- and four-dimensional. The complex case is the completely reducible abelian base of the family.

## Summary

The commutator bracket of $\mathbb{C}$ vanishes identically, so $\mathbb{C} \cong \mathbb{R}^2$ is an abelian Lie algebra of real dimension $2$, with the universal enveloping algebra a polynomial algebra on two variables, and the group of units is the abelian Lie group $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$ of real dimension $2$, open and dense, with Lie algebra $\mathbb{C}$.

The exponential $\exp(A) = \sum A^n/n!$ is entire, never zero, and a group homomorphism, $\exp(A+B) = \exp A \exp B$ exactly, because the Baker–Campbell–Hausdorff series terminates at the leading term. Its closed form is $e^{a+i a'} = e^a(\cos a' + i\sin a')$, its norm is $N(\exp A) = e^{\operatorname{Tr} A}$, it is surjective onto $\mathbb{C}^\times$ with the polar logarithm $\ln|A| + i\arg A$, and its kernel is the discrete lattice $2\pi i\,\mathbb{Z} \cong \mathbb{Z}$.

Every nonzero complex number has the polar parametrisation $A = re^{i\theta} = \exp(\ln r + i\theta)$ with $r \in \mathbb{R}_{>0}$ and $\theta \in \mathbb{R}$, the group of units splitting as $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1)$. The one-parameter subgroups are $t \mapsto \exp(tX)$, the one generated by $i$ is the circle $U(1) \cong \mathbb{R}/2\pi\mathbb{Z} \cong SO(2)$, and $U(1)$ is the maximal compact subgroup, onto which $\mathbb{C}^\times$ deformation retracts. The complex case is the abelian base of the family: the whole structure is the product of a line and a circle.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $A = a+i a'$ | a complex number, $a$ the real part, $a'$ the imaginary part |
| $[A,B] = AB - BA = 0$ | the commutator bracket, identically zero |
| $\mathbb{C}^\times = \mathbb{C}\setminus\{0\}$ | the group of units |
| $\exp(A) = \sum_n A^n/n!$ | the exponential, entire and a homomorphism |
| $e^{a+i a'} = e^{a}(\cos a' + i\sin a')$ | the Euler closed form |
| $N(\exp A) = e^{\operatorname{Tr} A} = e^{2a}$ | the norm of an exponential |
| $\ker\exp = 2\pi i\,\mathbb{Z}$ | the kernel, a discrete infinite cyclic group |
| $U(1) = \{A : N(A) = 1\}$ | the norm-one group, the unit circle, $\cong SO(2)$ |
| $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times U(1)$ | the polar splitting, the product of scale and phase |
| $A = re^{i\theta}$ | the polar/exponential parametrisation, $r=|A|$, $\theta = \arg A$ |
| $\gamma_X(t) = \exp(tX)$ | a one-parameter subgroup, $X$ in the Lie algebra |
| $\operatorname{Tr}(A) = 2a$ | the algebra trace |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd edition 2015), for the exponential map, its surjectivity on $GL(n,\mathbb{C})$ and the matrix logarithm.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for an elementary treatment of $U(1)$, $SO(2)$ and the circle group as the base case of the rotation groups.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the exponential, the logarithm and the polar form.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the exponential as a map of the plane and the circle as a one-parameter group.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the exponential and polar forms in the higher-dimensional cases.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the biquaternion exponential and polar forms.
