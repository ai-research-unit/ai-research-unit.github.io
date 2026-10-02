# __Hermitian Pairings on a Topological Space__

## Introduction

A pairing on the cohomology of a space is a bilinear or sesquilinear form, the archetype being the intersection pairing $\langle u \cup v, [X]\rangle$ of a closed oriented manifold, and the pairing carries the Hermitian structure of the coefficient ring. When the space carries a continuous involution, the induced operator on the cohomology acts on the pairing: if the involution preserves the fundamental class the pairing is invariant, and if it reverses the fundamental class the pairing is anti-invariant, and the two cases have opposite consequences for the fixed part. The article develops the pairing, the two cases of the action of the involution, the **orthogonal decomposition** of the cohomology into the fixed and the anti-fixed parts, and the **signature** of the form and of its restriction to the fixed part. The invariant case splits the form orthogonally over the two eigenspaces, so that the signature is the sum of the signatures of the two parts and the contribution of the fixed part is isolated; the anti-invariant case makes the fixed part totally isotropic, so that the form pairs the fixed part with the anti-fixed part and the two have the same dimension. The equivariant refinement of the signature, which computes the contribution of the fixed part from the fixed point set of the involution, is named and deferred.

The article continues *The Antipodal Map and the Adjoint*, whose pairing on the sphere is the model, and *The Involution on the Cohomology Operators*, whose fixed part it pairs. It uses the bilinear and Hermitian forms of Part I, in *Bilinear Forms* and *Indefinite Inner Product Spaces*, the signature of a symmetric form from the same place, and the cup product and Poincaré duality of *Cup and Cap Products* and *Poincaré Duality*. The equivariant signature theorem of Atiyah and Singer is named as the later refinement and is not used. Nothing analytic and nothing geometric is used: the form is an algebraic pairing on a module, the signature is the difference of two ranks, and no norm, no measure and no differentiability occurs; the manifold enters only through its fundamental class and the pairing it defines.

## Pairings and the Cup Product

### Hermitian Pairings

Throughout, $R$ is a commutative ring with identity carrying an involution $r \mapsto \bar r$ with $\bar r\bar s = \overline{rs}$ and $\bar 1 = 1$; the involution may be trivial, as for $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$, or the conjugation, as for $\mathbb{C}$. The cohomology is $H^{*}(X;R)$, and a **pairing** is a biadditive map $\beta : H^{p} \times H^{q} \to R$ for the relevant degrees.

**Definition.** A pairing $\beta$ is **sesquilinear** when it is $R$-linear in the first variable and conjugate-linear in the second,

$$
\beta(ru + sv, w) = r\beta(u,w) + s\beta(v,w), \qquad \beta(u, rv) = \bar r\,\beta(u,v),
$$

and it is **Hermitian** when it satisfies the Hermitian symmetry $\beta(v,u) = \overline{\beta(u,v)}$, or **$\varepsilon$-Hermitian** when $\beta(v,u) = \varepsilon\,\overline{\beta(u,v)}$ with $\varepsilon$ a unit of $R$ satisfying $\varepsilon\bar\varepsilon = 1$. For the trivial involution the Hermitian symmetry is the ordinary symmetry and the $\varepsilon$-Hermitian condition is the $\varepsilon$-symmetry of Part I.

**Theorem.** An $\varepsilon$-Hermitian pairing has no confusion of the two variables: the conjugate-linear and the $\varepsilon$ factors multiply as expected, the form is determined by the values $\beta(u,u)$ when two is invertible and $\varepsilon = 1$, and the adjoint operation of the form, $\beta(Tu,v) = \beta(u,T^{*}v)$, is an anti-automorphism of the algebra of operators, an involution when the form is $\varepsilon$-Hermitian. The form is **nondegenerate** when the adjoint map $u \mapsto \beta(u,\cdot)$ is a bijection onto the conjugate dual.

**Proof.** The verification is linearity in each variable and the Hermitian symmetry; the adjoint operation and its properties are those of *Equivariant Operators under a Continuous Involution* and of the bilinear forms of Part I, read with the conjugate structure.

### The Intersection Pairing

**Theorem.** Let $X$ be a closed $R$-oriented topological $n$-manifold with fundamental class $[X] \in H_{n}(X;R)$. Then the **intersection pairing**

$$
\beta(u,v) = \langle u \cup v, [X]\rangle \qquad (u \in H^{p}(X;R),\ v \in H^{n-p}(X;R)),
$$

is a nondegenerate $R$-sesquilinear pairing, the content of Poincaré duality; it is $\varepsilon$-Hermitian with the graded coefficient $\varepsilon_{p} = (-1)^{p(n-p)}$ on $H^{p}$, and in particular the middle pairing on $H^{n/2}$ is symmetric when $n \equiv 0 \pmod 4$ and alternating when $n \equiv 2 \pmod 4$. For $R = \mathbb{R}$ and $n = 4k$ the middle pairing is a nondegenerate symmetric bilinear form, and its **signature** is the integer

$$
\operatorname{sign}(X) = b_{+} - b_{-},
$$

where $b_{+}$ and $b_{-}$ are the numbers of positive and negative eigenvalues of the form on $H^{2k}(X;\mathbb{R})$.

**Proof.** The nondegeneracy is Poincaré duality, *Poincaré Duality*; the symmetry coefficient is the graded-commutativity of the cup product, $u\cup v = (-1)^{pq}v\cup u$ for $|u| = p$ and $|v| = q$; the middle case is $p = q = n/2$, giving $(-1)^{n/2}$, which is $+1$ for $n \equiv 0 \pmod 4$ and $-1$ for $n \equiv 2 \pmod 4$. The signature is defined for a nondegenerate symmetric form over the reals by the spectral theorem for symmetric forms of Part I.

## The Involution on the Pairing

### Invariance and Anti-Invariance

**Definition.** Let $\sigma$ be a continuous involution of $X$ and $\sigma^{*}$ the induced operator on the cohomology. The pairing $\beta$ is **$\sigma$-invariant** when

$$
\beta(\sigma^{*}u, \sigma^{*}v) = \beta(u,v) \qquad (u, v),
$$

and **$\sigma$-anti-invariant** when $\beta(\sigma^{*}u,\sigma^{*}v) = -\beta(u,v)$; more generally it **scales** by a unit $c$ when $\beta(\sigma^{*}u,\sigma^{*}v) = c\,\beta(u,v)$.

**Theorem.** If the involution preserves the fundamental class, $\sigma_{*}[X] = [X]$, then the intersection pairing is $\sigma$-invariant; if it reverses the fundamental class, $\sigma_{*}[X] = -[X]$, then the pairing is $\sigma$-anti-invariant. In general the pairing scales by the degree $\deg(\sigma) = \pm 1$ of the involution, and this is the scalar by which the antipodal operator scales the cup-product pairing on the sphere in *The Antipodal Map and the Adjoint*.

**Proof.** The invariance and the scaling are the computation

$$
\beta(\sigma^{*}u,\sigma^{*}v) = \langle \sigma^{*}(u\cup v), [X]\rangle = \langle u \cup v, \sigma_{*}[X]\rangle = \deg(\sigma)\,\beta(u,v),
$$

using that $\sigma^{*}$ is a ring homomorphism and the naturality of the evaluation; the sphere is the case computed in the previous article.

### The Orthogonal Decomposition

**Theorem.** Let two be invertible in $R$ and let the form scale by the unit $c$. Then the eigenspaces of $\sigma^{*}$ are **orthogonal** when $c = 1$:

$$
\beta(u,v) = 0 \qquad (u \in H^{*}(X)^{\sigma^{*}},\ v \in H^{*}(X)^{-\sigma^{*}}),
$$

and the form splits as the orthogonal sum of its restrictions to the two eigenspaces. When $c = -1$ each eigenspace is **totally isotropic**, $\beta$ vanishes on the fixed part and on the anti-fixed part separately, and the form pairs the two parts dually, so that they have the same rank and the form is a hyperbolic form on their sum.

**Proof.** For $c = 1$ and $u$ fixed, $v$ anti-fixed, the invariance gives $\beta(u,v) = \beta(\sigma^{*}u,\sigma^{*}v) = \beta(u,-v) = -\beta(u,v)$, so $2\beta(u,v) = 0$ and the invertibility of two gives $\beta(u,v) = 0$. For $c = -1$ and $u, v$ both fixed, $\beta(u,v) = \beta(\sigma^{*}u,\sigma^{*}v) = -\beta(u,v)$, so $2\beta(u,v) = 0$ and $\beta$ vanishes on the fixed part; the same for the anti-fixed part, and the nondegeneracy of $\beta$ then makes the pairing between the two parts perfect, whence equal ranks.

## The Signature and the Fixed Part

### The Signature of an Invariant Form

**Theorem.** Let $R = \mathbb{R}$, let the form $\beta$ be symmetric, nondegenerate and $\sigma$-invariant on a finite-dimensional space $V$, and let $V = V^{+} \oplus V^{-}$ be the eigenspace decomposition. Then the form splits orthogonally and the signature is additive:

$$
\operatorname{sign}(V,\beta) = \operatorname{sign}(V^{+},\beta^{+}) + \operatorname{sign}(V^{-},\beta^{-}),
$$

where $\beta^{\pm}$ are the restrictions. The **fixed-part signature** is $\operatorname{sign}(V^{+},\beta^{+})$, and the **equivariant signature** is the difference

$$
\operatorname{sign}^{\sigma}(V,\beta) = \operatorname{sign}(V^{+},\beta^{+}) - \operatorname{sign}(V^{-},\beta^{-}),
$$

which is the trace of the involution on the formal difference of the positive and negative cones of the form; the signature is the sum and the equivariant signature the difference, so the two determine the two summands.

**Proof.** The orthogonality of the eigenspaces is the theorem above for $c = 1$; the additivity of the signature over an orthogonal sum is the standard property of the signature of a symmetric form, from Part I; the two equations determine $\operatorname{sign}(V^{\pm},\beta^{\pm})$ from the signature and the equivariant signature.

### The Fixed Part

**Theorem.** The contribution of the fixed part to the cohomology of the space with involution is the space $H^{*}(X;\mathbb{R})^{\sigma^{*}}$, and its signature is the signature of the restriction of the intersection form; in the invariant case it is the $V^{+}$ summand above, and in the anti-invariant case it is a totally isotropic subspace paired with the anti-fixed part. For the antipodal involution of the sphere in *The Antipodal Map and the Adjoint* the only nonzero part of the form is the top pairing on $H^{n}(S^{n};\mathbb{R}) = \mathbb{R}$. In the odd dimensions the involution has degree $+1$, so the form is invariant and the fixed part is the whole top group, while the top form is alternating because the top degree is odd, whence its symmetric signature is zero; in the even dimensions the involution has degree $-1$, so the form is anti-invariant, the top form is symmetric, and the top class is anti-invariant, so the fixed part is zero there. For a sphere of positive dimension the middle cohomology vanishes, since the cohomology is concentrated in degrees $0$ and $n$ and $n/2$ is neither, so the symmetric middle form of a positive-dimensional sphere is the zero form and its signature is zero.

**Proof.** The description of the fixed part is the definition and the orthogonality theorem. For the sphere the cohomology is concentrated in degrees $0$ and $n$; the form is nonzero only on the top group; the scaling of the form is by the degree $(-1)^{n+1}$, so the form is invariant in the odd dimensions and anti-invariant in the even dimensions; the top form is symmetric when $n$ is even and alternating when $n$ is odd, by the graded commutativity of the cup product; the fixed part of the top group is the whole group when $n$ is odd, by the computation of the previous article, and zero when $n$ is even; and the middle cohomology $H^{n/2}(S^{n})$ vanishes for $n > 0$, so the symmetric middle form has signature zero.

**Remark.** The two cases of the scaling are the two behaviours of the involution on the pairing, and they are distinguished by the fixed part: an invariant form restricts to a nondegenerate form on the fixed part in the favourable cases, while an anti-invariant form makes the fixed part isotropic and forces it to be paired with the anti-fixed part. The equivariant refinement, the **equivariant signature theorem** of Atiyah and Singer, computes the equivariant signature of a closed oriented even-dimensional manifold with an involution in terms of the fixed point set of the involution; it belongs to the analysis of the index theory and is named here as the refinement of the algebraic statement and not used.

## Summary

A Hermitian pairing on the cohomology of a space is a sesquilinear form with the Hermitian symmetry of the coefficient ring, and the intersection pairing $\langle u\cup v,[X]\rangle$ of a closed oriented manifold is the archetype; it is nondegenerate by Poincaré duality and $\varepsilon$-Hermitian with the graded sign, symmetric on the middle cohomology of a $4k$-manifold, where its signature is defined. A continuous involution acts on the pairing by the degree of its action on the fundamental class: the pairing is invariant when the fundamental class is preserved and anti-invariant when it is reversed, and in general it scales by the degree. Over a ring in which two is invertible the eigenspaces of the induced operator on the cohomology are orthogonal for an invariant form, so the form splits as the orthogonal sum of the fixed and the anti-fixed parts and the signature is additive, while for an anti-invariant form each eigenspace is totally isotropic and the two parts are paired dually with equal rank. The signature of the restriction to the fixed part and the equivariant signature, the difference of the two summands, are the invariants of the involution on the form; the equivariant signature theorem of Atiyah and Singer computes the equivariant signature from the fixed point set and is deferred as the analytic refinement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $r \mapsto \bar r$ | Coefficient ring with an involution (trivial or conjugation) |
| sesquilinear $\beta$ | Linear in the first variable, conjugate-linear in the second |
| Hermitian, $\varepsilon$-Hermitian | $\beta(v,u) = \overline{\beta(u,v)}$, respectively $\varepsilon\overline{\beta(u,v)}$ |
| nondegenerate | $u \mapsto \beta(u,\cdot)$ is a bijection onto the conjugate dual |
| $[X]$, intersection pairing | Fundamental class and $\beta(u,v) = \langle u\cup v,[X]\rangle$ |
| $\varepsilon_{p} = (-1)^{p(n-p)}$ | The symmetry coefficient of the intersection pairing |
| $\operatorname{sign}(X) = b_{+}-b_{-}$ | Signature of the middle form of a $4k$-manifold |
| $\sigma$-invariant, $\sigma$-anti-invariant | $\beta(\sigma^{*}u,\sigma^{*}v) = \pm\beta(u,v)$ |
| $\deg(\sigma)$ scaling | The pairing scales by the degree of the involution |
| $V = V^{+}\oplus V^{-}$ | Eigenspaces of the induced operator |
| orthogonal / isotropic | The eigenspaces orthogonal ($c=1$) / totally isotropic ($c=-1$) |
| $\operatorname{sign}(V^{+},\beta^{+})$ | Signature of the fixed part |
| $\operatorname{sign}^{\sigma}$ | Equivariant signature, the difference of the two summands |

## Further Reading

- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for sesquilinear and Hermitian forms, the adjoint anti-automorphism and the nondegeneracy conditions.
- Serge Lang, *Algebra* (Springer, revised 3rd ed. 2002), for symmetric and Hermitian forms, the spectral theorem over the reals and the signature.
- W. Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for $\varepsilon$-Hermitian forms, hyperbolic forms and the orthogonal decomposition of a form under an isometry of order two.
- William S. Massey, *A Basic Course in Algebraic Topology* (Springer, 1991), for Poincaré duality, the intersection pairing and its symmetry.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators III", *Annals of Mathematics* 87 (1968), 546–604, for the equivariant signature theorem and the computation from the fixed point set.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the action of a group on a pairing and the fixed part of an equivariant form.
