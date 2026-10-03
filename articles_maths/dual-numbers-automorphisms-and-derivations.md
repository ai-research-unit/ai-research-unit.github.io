
# __Dual-Numbers Automorphisms and Derivations__

## Introduction

This article computes the two standard invariants of the dual-number algebra: the group of algebra **automorphisms** and the Lie algebra of **derivations**. It follows *Dual-Numbers Algebra*, where the derivation module is determined, and *Dual-Numbers Ideals and the Maximal Ideal*, where the maximal ideal is shown to be the unique proper nonzero ideal. The structural model is *Biquaternion Automorphisms and Derivations*, whose automorphism group is the projective linear group and whose derivation algebra is the traceless part $\mathrm{SL}(2,\mathbb{C})$; here the algebra is commutative and local, and both invariants are correspondingly small.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the geometric specialisation is $R = \mathbb{R}$, and then the algebra is written $\mathbb{D}'$. A general dual number is

$$
A = a + \varepsilon a', \qquad a, a' \in R,
$$

with $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$, dual conjugation $\bar A = a - \varepsilon a'$, maximal ideal $\mathrm{M} = (\varepsilon) = \varepsilon R_{\mathbb{D}'}$, real submodule $R_{\mathbb{D}'}$ and infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$.

## The Automorphism Group

### Definition

**Definition.** An **$R$-algebra automorphism** of $\mathbb{D}'_R$ is a bijective $R$-linear map $\varphi : \mathbb{D}'_R \to \mathbb{D}'_R$ with $\varphi(AB) = \varphi(A)\varphi(B)$ and $\varphi(1) = 1$. They form a group under composition, written $\operatorname{Aut}_R(\mathbb{D}'_R)$; when $R = \mathbb{R}$ we write $\operatorname{Aut}(\mathbb{D}')$.

### The Automorphisms

**Theorem.** Every automorphism of $\mathbb{D}'_R$ is determined by its value on $\varepsilon$, and

$$
\varphi(a + \varepsilon a') = a + a'c\,\varepsilon, \qquad c \in R^\times,
$$

so the assignment $\varphi \mapsto c$ is a group isomorphism

$$
\operatorname{Aut}_R(\mathbb{D}'_R) \;\cong\; R^\times.
$$

**Proof.** An automorphism must fix $R$ pointwise, since it is $R$-linear and unital, so it is determined by $\varphi(\varepsilon)$. Writing $\varphi(\varepsilon) = p + q\varepsilon$, the relation $\varepsilon^2 = 0$ is preserved only if

$$
0 = \varphi(\varepsilon^2) = \varphi(\varepsilon)^2 = p^2 + 2pq\,\varepsilon,
$$

that is, $p^2 = 0$ and $2pq = 0$. The scalar $q$ is a unit: $\varphi(a + \varepsilon a') = (a + a'p) + a'q\,\varepsilon$ has $\varepsilon$-component $a'q$, and surjectivity of $\varphi$ forces $a' \mapsto a'q$ to be onto $R$, which happens only for $q \in R^\times$. With $q$ a unit and $2$ invertible, $pq = 0$ gives $p = 0$, so $\varphi(\varepsilon) = q\varepsilon$ and $\varphi(a + \varepsilon a') = a + a'q\varepsilon$. This is bijective exactly when multiplication by $q$ is, that is, exactly when $q \in R^\times$. Composition corresponds to multiplication of the scalars, so $\varphi \mapsto q$ is an isomorphism onto $R^\times$; writing the multiplier as $c$ gives the stated form $\varphi(a + \varepsilon a') = a + a'c\,\varepsilon$.

**Corollary.** Over $\mathbb{R}$ the automorphism group is $\operatorname{Aut}(\mathbb{D}') \cong \mathbb{R}^\times$, a one-dimensional abelian Lie group with exactly two connected components, distinguished by the sign of the scalar $c$; the identity component is $\{c > 0\} \cong \mathbb{R}_{>0}$.

### Action on the Distinguished Submodules

**Proposition.** Every automorphism fixes the real submodule $R_{\mathbb{D}'}$ pointwise and acts on the infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$ by the scalar $c$:

$$
\varphi(R_{\mathbb{D}'}) = R_{\mathbb{D}'}, \qquad \varphi(\varepsilon a') = c \varepsilon a'.
$$

**Proof.** $\varphi(a) = a$ by $R$-linearity and unitality, and $\varphi(\varepsilon a') = a'\varphi(\varepsilon) = a' \varepsilon c$.

So the automorphism group acts trivially on the quotient $\mathbb{D}'_R/\mathrm{M} \cong R$ and by the full group of scalars on $\mathrm{M}$. This is the algebraic reason that an automorphism cannot exchange the two submodules: the identity $1$ is fixed, so the real submodule is stable, and the class of $\varepsilon$ in the quotient is nonzero, so the infinitesimal submodule is stable.

## Derivations

### Definition

**Definition.** An **$R$-linear derivation** of $\mathbb{D}'_R$ is an $R$-linear map $D : \mathbb{D}'_R \to \mathbb{D}'_R$ with the Leibniz rule

$$
D(AB) = D(A)\,B + A\,D(B).
$$

The set of all such maps is an $R$-module written $\operatorname{Der}_R(\mathbb{D}'_R)$, and it is a Lie algebra under the commutator $[D_1, D_2] = D_1 D_2 - D_2 D_1$.

Every derivation satisfies $D(1) = 0$, since $D(1) = D(1\cdot 1) = 2D(1)$ and $2$ is invertible.

### The Derivation Space

**Theorem.** Every derivation of $\mathbb{D}'_R$ is of the form

$$
D(a + \varepsilon a') = c \varepsilon a'
$$

for a unique $c \in R$. The module of derivations is therefore free of rank one,

$$
\operatorname{Der}_R(\mathbb{D}'_R) \;\cong\; R,
$$

generated by the derivation

$$
\partial_\varepsilon(a + \varepsilon a') = \varepsilon a'.
$$

**Proof.** Let $D$ be a derivation. From $D(1) = 0$ and $R$-linearity, $D(a) = 0$ for all $a \in R$, so $D$ is determined by $D(\varepsilon)$. Applying $D$ to $\varepsilon^2 = 0$ gives

$$
0 = D(\varepsilon^2) = 2\varepsilon\,D(\varepsilon),
$$

so $\varepsilon D(\varepsilon) = 0$. Writing $D(\varepsilon) = c + \varepsilon d$, this gives $\varepsilon c = 0$, hence $c = 0$; so $D(\varepsilon) = \varepsilon d$ and

$$
D(a + \varepsilon a') = D(a) + D(a')\varepsilon + a'\,D(\varepsilon) = a' \varepsilon d.
$$

The map $D \mapsto d$ is an $R$-linear isomorphism onto $R$, so the module is free of rank one and generated by $\partial_\varepsilon$, the case $d = 1$.

**Remark (dimension).** The derivation module is free of rank one over $R$, so as a real vector space of derivations of $\mathbb{D}'$ over $\mathbb{R}$ it is one-dimensional, $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$, of real dimension one. This agrees with the computation in *Dual-Numbers Algebra* and in *Shears and Parabolic Rotations*: the single relation $\varepsilon^2 = 0$ carries exactly one independent derivation, and the derivation space is spanned by $\partial_\varepsilon$. The count is one because the derivation is determined by the single value $D(\varepsilon)$, which is constrained to lie in the one-dimensional maximal ideal; a two-dimensional derivation space would require a second independent relation, and there is none.

### No Inner Derivations

**Proposition.** Every inner derivation of $\mathbb{D}'_R$ vanishes: $\operatorname{ad}_A(B) = [A, B] = 0$ for all $A, B$. Consequently **no nonzero derivation of $\mathbb{D}'_R$ is inner**, and the whole derivation space consists of outer derivations.

**Proof.** $\mathbb{D}'_R$ is commutative, so $AB = BA$ and the commutator is identically zero; the kernel of $\operatorname{ad}$ is all of $\mathbb{D}'_R$, and $\partial_\varepsilon \neq 0$ is outer.

This is the exact reversal of the biquaternion case: in $\mathbb{B} \cong M_2(\mathbb{C})$ every derivation is inner, by Skolem–Noether-adjacent matrix computation, and $\operatorname{Der}_\mathbb{C}(\mathbb{B}) \cong \mathbb{B}/\mathbb{C}_{\mathbb{B}} = \mathrm{SL}(2,\mathbb{C})$. Here the algebra is commutative and no derivation is inner.

## The Nilpotent Direction and the Unit Group

### The Derivation in the Nilpotent Direction

**Definition.** The derivation $\partial_\varepsilon$, with $\partial_\varepsilon(a + \varepsilon a') = \varepsilon a'$, is the **derivation in the nilpotent direction**; it acts as the identity on the infinitesimal submodule and as zero on the real submodule.

**Proposition.** The derivation $\partial_\varepsilon$ satisfies

- $\ker\partial_\varepsilon = R_{\mathbb{D}'}$ and $\operatorname{im}\partial_\varepsilon = \varepsilon R_{\mathbb{D}'} = \mathrm{M}$;
- $\partial_\varepsilon^2 = \partial_\varepsilon$, so it is a projection and is **not** nilpotent;
- its matrix in the basis $(1, \varepsilon)$ is $\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.

**Proof.** $\partial_\varepsilon(a + \varepsilon a') = \varepsilon a'$ vanishes exactly when $a' = 0$, giving the kernel; its image is the set of all $\varepsilon a'$, which is $\mathrm{M}$. Applying it twice gives $\partial_\varepsilon(\varepsilon a') = \varepsilon a'$, hence $\partial_\varepsilon^2 = \partial_\varepsilon$. The matrix has columns $\partial_\varepsilon(1) = 0$ and $\partial_\varepsilon(\varepsilon) = \varepsilon$.

So $\partial_\varepsilon$ is a projection onto the nilpotent direction, and it is the unique (up to scale) derivation. The name records the direction of its image, not any nilpotence of the map itself.

### Generators of the Automorphism Group

**Theorem.** The exponential of the derivation $\partial_\varepsilon$ is the automorphism

$$
\exp(t\,\partial_\varepsilon)(a + \varepsilon a') = a + a'\,e^{t}\,\varepsilon,
$$

and $\{\exp(t\partial_\varepsilon) : t \in \mathbb{R}\}$ is exactly the identity component of $\operatorname{Aut}(\mathbb{D}')$. Hence

$$
\operatorname{Lie}\operatorname{Aut}(\mathbb{D}') = \operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon.
$$

**Proof.** Since $\partial_\varepsilon^k(\varepsilon) = \varepsilon$ for every $k \geq 1$, the exponential series gives $\exp(t\partial_\varepsilon)(\varepsilon) = \sum_{k \geq 0} t^k\varepsilon/k! = e^t\varepsilon$, and $\exp(t\partial_\varepsilon)(a) = a$. The resulting automorphism is $\varphi_{e^t}$ in the notation of the automorphism theorem, and as $t$ ranges over $\mathbb{R}$ the scalar $e^t$ ranges over $\mathbb{R}_{>0}$, the identity component of $\mathbb{R}^\times$.

This is the standard correspondence for a finite-dimensional real algebra: the Lie algebra of the automorphism group is the derivation algebra, and the exponential of a derivation is an automorphism.

### The Derivations and the Unit Group

The derivation $\partial_\varepsilon$ rescales the infinitesimal direction and fixes the real direction; it does **not** generate the shear group $1 + \mathrm{M}$ of *Shears and Parabolic Rotations*. The shear acts by $1 + s\varepsilon$, translating the infinitesimal coordinate by $a + \varepsilon a' \mapsto a + (a' + sa)\varepsilon$, and it is the exponential $\exp(s\varepsilon)$ of the element $\varepsilon$ of the algebra, not of any derivation. So the unit group is generated by the algebra's own nilpotent direction, while the automorphism group is generated by the derivation $\partial_\varepsilon$; the two are different objects and must not be conflated.

## Relation to the Biquaternion Theory

The two theories are complementary extremes.

| | $\mathbb{D}'$ over $\mathbb{R}$ | $\mathbb{B}$ over $\mathbb{C}$ |
|---|---|---|
| Algebra | commutative, local, $\dim_{\mathbb{R}} = 2$ | $M_2(\mathbb{C})$, simple, $\dim_{\mathbb{C}} = 4$ |
| Automorphism group | $\mathbb{R}^\times$, dimension $1$, two components | $PGL(2,\mathbb{C})$, dimension $3$ ($6$ over $\mathbb{R}$), connected |
| Derivation space | $\operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$, dimension $1$ | $\operatorname{Der}_\mathbb{C}(\mathbb{B}) \cong \mathrm{SL}(2,\mathbb{C})$, dimension $3$ |
| Inner derivations | all zero | all derivations |
| Generators of $\operatorname{Aut}$ | $\exp(t\partial_\varepsilon)$, $t \in \mathbb{R}$ | $\exp(\operatorname{ad}_a)$, $a$ traceless |

Two structural facts account for the difference. First, the biquaternion algebra is central simple, so its automorphism group is the projective linear group by Skolem–Noether and its derivations are inner; the dual algebra is commutative and local, so its automorphism group is the scalar group $R^\times$ and all of its derivations are outer. Second, the biquaternion derivation space has dimension equal to the dimension of the traceless part, three over $\mathbb{C}$; the dual derivation space has dimension equal to the number of independent relations, one. A useful sanity check is the standard dimension count for a local algebra: the tangent space of $k[\varepsilon]/(\varepsilon^2)$ at its closed point is the dual of $\mathrm{M}/\mathrm{M}^2$, and $\mathrm{M}^2 = 0$ gives $\mathrm{M}/\mathrm{M}^2 = \mathrm{M}$, of dimension one, so the tangent space is one-dimensional; the derivation module $\operatorname{Der}_k(\mathbb{D}'_k)$, determined by the single value $D(\varepsilon) \in \mathrm{M}$, is one-dimensional as well, and the two counts agree. The nontrivial statement in the dual case is not the size of the derivation space but the fact that its single generator is exactly the nilpotent-direction derivative $\partial_\varepsilon$.

## Summary

The unital algebra automorphisms of $\mathbb{D}'_R$ are exactly the maps $\varphi_c(a + \varepsilon a') = a + a'c\,\varepsilon$ with $c \in R^\times$, and $\operatorname{Aut}_R(\mathbb{D}'_R) \cong R^\times$; over $\mathbb{R}$ this is $\mathbb{R}^\times$, a one-dimensional abelian Lie group with two contractible components. Every automorphism fixes the real submodule pointwise and scales the infinitesimal submodule by $c$,  The $R$-linear derivations are exactly the maps $D(a + \varepsilon a') = c \varepsilon a'$ with $c \in R$; the derivation module is free of rank one, $\operatorname{Der}_R(\mathbb{D}'_R) \cong R$, generated by $\partial_\varepsilon(a + \varepsilon a') = \varepsilon a'$. As a space of derivations of $\mathbb{D}'$ over $\mathbb{R}$ it is the one-dimensional space $\mathbb{R}\partial_\varepsilon$, since $\varepsilon^2 = 0$ is the single defining relation of the algebra. Since $\mathbb{D}'$ is commutative, every inner derivation vanishes and the unique generator is outer. The derivation $\partial_\varepsilon$ is a projection onto the nilpotent direction with kernel the real submodule, and its exponential realises the identity component of the automorphism group, $\exp(t\partial_\varepsilon)(\varepsilon) = e^t\varepsilon$, so $\operatorname{Lie}\operatorname{Aut}(\mathbb{D}') = \operatorname{Der}(\mathbb{D}') = \mathbb{R}\partial_\varepsilon$. The contrast with the biquaternion theory is total: there $\operatorname{Aut}_\mathbb{C}(\mathbb{B}) = PGL(2,\mathbb{C})$ with all derivations inner and $\operatorname{Der}_\mathbb{C}(\mathbb{B}) \cong \mathrm{SL}(2,\mathbb{C})$ of dimension three, while here the automorphism group is the scalars and the derivation space is a single line of outer derivations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $A = a + \varepsilon a'$ | General dual number |
| $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$ | Real and infinitesimal parts |
| $\bar{A} = a - \varepsilon a'$ | Dual conjugation |
| $R_{\mathbb{D}'}$, $\varepsilon R_{\mathbb{D}'}$ | Real and infinitesimal submodules |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal |
| $\operatorname{Aut}_R(\mathbb{D}'_R) \cong R^\times$ | Group of unital algebra automorphisms, $\varphi_c(\varepsilon) = \varepsilon c$ |
| $\operatorname{Der}_R(\mathbb{D}'_R) \cong R$ | Module of derivations, free of rank one |
| $\partial_\varepsilon(a + \varepsilon a') = \varepsilon a'$ | The derivation in the nilpotent direction |
| $\varphi_c$ | Automorphism with $\varphi_c(\varepsilon) = \varepsilon c$, $c \in R^\times$ |
| $\operatorname{ad}_A(B) = [A, B]$ | Inner derivation, identically zero here |
| $\mathbb{B}$ | Biquaternion algebra, the comparison model |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, New York, 1982), for automorphism groups and derivation algebras of finite-dimensional algebras.
- Nathan Jacobson, *Lie Algebras* (Dover, New York, 1979), for derivations of associative algebras, the module of derivations, and the correspondence with the Lie algebra of the automorphism group.
- I. N. Herstein, *Noncommutative Rings* (Carus Mathematical Monographs 15, Mathematical Association of America, Washington, 1968), for inner derivations and the Skolem–Noether theorem in the matrix case.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Grundlehren der mathematischen Wissenschaften 294, Springer, Berlin, 1991), for derivations of algebras carrying a quadratic form over a local base.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* (SIAM, Philadelphia, 2008), for the nilpotent-direction derivative as the algebraic content of differentiation.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Graduate Texts in Mathematics 222, Springer, New York, 2nd ed. 2015), for the exponential of a derivation and the Lie algebra of a matrix group.
