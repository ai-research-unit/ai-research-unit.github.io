# __The Biquaternion Krein Form and Its Signature__

## Introduction

The biquaternion algebra carries two Hermitian pairings and one bilinear pairing. The dagger gives the positive definite form $\tilde{Q}\tilde{Q}^{*}$ (*The Hermitian Form on the Biquaternion Algebra*), the plain product gives the symmetric bilinear form $N(\tilde{Q})=\tilde{Q}\tilde{Q}^{\natural}$ (*The Bilinear Form on the Biquaternion Algebra*), and the **natural conjugation** ${}^{\natural}$, which negates the vector units and fixes the centre, gives a third pairing of the middle kind: a Hermitian form that is **indefinite**, of signature $(2,6)$ on $\mathbb{B}$ and $(1,3)$ on the anti-Hermitian subspace.

That form is the **Krein form** of the algebra. It is Hermitian like the dagger form but indefinite, and it is symmetric-like the bilinear form but conjugate-linear in one argument; it is the form of the Minkowski interval read on the whole algebra, and it makes $\mathbb{B}$ a Krein space of finite negativity. This article defines the form, computes its signature, identifies its definite parts with the centre and the vector subspace, and locates its totally isotropic subspaces.

The general theory is in *Indefinite Inner Product Spaces*, *Krein Spaces* and *Pontryagin Spaces*; the operator $J$ that turns the Krein form into the Hermitian one is *The Fundamental Symmetry of the Biquaternion Algebra*; the operators that the form makes available are *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*; and the skew-scalar companion on the same conjugation is *Association and the Transpose on the Biquaternion Algebra*. The comparison with the two other forms is *Biquaternion Norm and Invertibility*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$, units $e_k$ with $e_k^{2}=-e_0$, central $i$. The natural conjugation is $\tilde{Q}^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3$, and the sign vector is $\varepsilon=(1,-1,-1,-1)$.

## The Krein Form

**Definition.** The **Krein form** is

$$
[\tilde{Q},\tilde{Q}']=\mathrm{Sc}\bigl(\tilde{Q}^{\natural*}\,\tilde{Q}'\bigr)
=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^{*}Q'_\mu
=|Q_0|^{2}-|Q_1|^{2}-|Q_2|^{2}-|Q_3|^{2}
$$

on the diagonal, where ${}^{\natural*}={}^{\natural}\circ\bar{\cdot}$ and $Q_\mu^{*}=\bar Q_\mu$.

Expanding the coefficients, for $\tilde{Q}=\sum_\mu(q_\mu+iq'_\mu)e_\mu$ and $\tilde{Q}'=\sum_\mu(q'_\mu+ip'_\mu)e_\mu$,

$$
[\tilde{Q},\tilde{Q}']=\sum_{\mu=0}^{3}\varepsilon_\mu\bigl(q_\mu q'_\mu+p_\mu p'_\mu\bigr)
+i\sum_{\mu=0}^{3}\varepsilon_\mu\bigl(p_\mu q'_\mu-q_\mu p'_\mu\bigr).
$$

**Proposition (Hermitian and non-degenerate).** The Krein form is $\mathbb{C}$-sesquilinear, conjugate-linear in the first argument and linear in the second, Hermitian in the sense $[\tilde{Q}',\tilde{Q}]=\overline{[\tilde{Q},\tilde{Q}']}$, real-valued on the diagonal, and non-degenerate: $[\tilde{Q},\tilde{Q}']=0$ for every $\tilde{Q}'$ forces $\tilde{Q}=0$.

**Proof.** Sesquilinearity is immediate from the definition and the coefficient formula; the conjugation symmetry is $\overline{\varepsilon_\mu Q_\mu^{*}Q'_\mu}=\varepsilon_\mu Q'^{*}_\mu Q_\mu$ summed; and non-degeneracy follows by testing against the eight basis vectors $e_\mu,ie_\mu$, which gives $Q_\mu=0$ for each $\mu$.

**Remark (three pairings on one algebra).** The three pairings are distinguished by the conjugation they use: the bilinear form uses ${}^{\natural}$ and is symmetric, the Hermitian form uses ${}^{*}$ and is positive definite, and the Krein form uses ${}^{\natural*}$ and is indefinite Hermitian. In the matrix model, the first is the pairing with the adjugate, the second with the conjugate transpose, and the third with the conjugate transpose of the adjugate (*The Forms in the Matrix Representation of the Biquaternion Algebra*).

## The Signature

The form is diagonal in the coefficient basis with signs $\varepsilon=(1,-1,-1,-1)$, but each coefficient is a complex number, hence two real dimensions.

**Theorem (the signature).** The inertia of the Krein form is

$$
\text{(real signature)}\ (2,6)\ \text{on}\ \mathbb{B}=\mathbb{R}^{8},
\qquad
\text{(complex signature)}\ (1,3)\ \text{on}\ \mathbb{B}=\mathbb{C}^{4}.
$$

The positive part is the **centre** $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{C}}\{e_0\}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ and the negative part is the **vector subspace** $\mathbb{V}_{\mathbb{B}}=\{Q_0=0\}$; the two are orthogonal and

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{V}_{\mathbb{B}}
$$

is a fundamental decomposition.

**Proof.** The diagonal value $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}$ is $|Q_0|^{2}$ on the centre and $-\sum_{k}|\tilde Q_k|^{2}$ on the vector subspace, hence positive on $\mathbb{C}_{\mathbb{B}}\setminus\{0\}$ and negative on $\mathbb{V}_{\mathbb{B}}\setminus\{0\}$; the two subspaces are complex lines (respectively the hyperplane $Q_0=0$) so their real dimensions are $2$ and $6$, giving $(2,6)$ over $\mathbb{R}$ and $(1,3)$ over $\mathbb{C}$; orthogonality is $\varepsilon_\mu$-weighted: a centre vector has only the $\mu=0$ coefficient and a vector vector only $\mu\neq0$, so $[\tilde{C},\tilde{V}]=0$.

**Remark (the two Lagrange identities).** On the vector subspace the Krein form is nothing but the bilinear form with the opposite sign, and on the Hermitian subspace it is the bilinear form itself:

$$
[\tilde V,\tilde V]=-N(\tilde V)\ \ \text{for}\ \tilde V\in\mathbb{V}_{\mathbb{B}},\qquad
[\tilde H,\tilde H]=N(\tilde H)\ \ \text{for}\ \tilde H\in\mathbb{M}_{+}.
$$

**Proof.** Substituting $Q_k$ imaginary... precisely, on $\mathbb{V}_{\mathbb{B}}$ the diagonal of the Krein form is $-\sum_k|Q_k|^{2}$ while $N(\tilde V)=\sum_k Q_k^{2}$; the two agree with opposite sign on the anti-Hermitian subspace, where $Q_k$ is real so $|Q_k|^{2}=Q_k^{2}$ and $N(\tilde V)=\sum_k Q_k^{2}=-\sum_k|Q_k|^{2}$; on the Hermitian subspace $Q_k=iq'_k$ is purely imaginary, so $N(\tilde H)=\sum_k(iq'_k)^{2}=-\sum_k(q'_k)^{2}$, while the Krein diagonal is $|Q_0|^{2}-\sum_k|q'_k|^{2}=q_0^{2}-\sum_k(q'_k)^{2}$, which is the same expression. This is the restriction table of *Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*, read on the Krein form.

**Corollary (the Lorentzian slices).** On the real quaternion subalgebra $\mathbb{B}_{\mathbb{R}}=\mathbb{H}$ and on the purely imaginary subalgebra $i\mathbb{B}_{\mathbb{R}}$, each of real dimension four, the Krein form has signature $(1,3)$: the two together are the real and the imaginary coefficient halves of the fundamental decomposition, and each is a copy of Minkowski space.

**Proof.** On $\mathbb{B}_{\mathbb{R}}$ all coefficients are real, so the Krein diagonal is $q_0^{2}-q_1^{2}-q_2^{2}-q_3^{2}$, of signature $(1,3)$; on $i\mathbb{B}_{\mathbb{R}}$ the coefficients are $ir_\mu$ with $r_\mu$ real, so the diagonal is $r_0^{2}-r_1^{2}-r_2^{2}-r_3^{2}$ again, and the two subspaces are $\varepsilon$-orthogonal complements.

## The Krein Space Structure

**Theorem.** $(\mathbb{B},[\cdot,\cdot])$ is a Krein space of complex dimension four and negative index three; over $\mathbb{R}$ it is a Pontryagin space $\Pi_6$; it is complete in the norm induced by any fundamental symmetry, every choice of which makes it a Hilbert space.

**Proof.** The form is non-degenerate, Hermitian and of finite index; the space is finite-dimensional, hence complete in every norm, so it is a Krein space by the definition of *Krein Spaces*; the negative part is $\mathbb{V}_{\mathbb{B}}$, of complex dimension three and real dimension six, so the negative index is $3$ over $\mathbb{C}$ and $6$ over $\mathbb{R}$, and a Pontryagin space is a Krein space of finite negative index (*Pontryagin Spaces*).

**Remark.** The name is the corpus's: the form is the indefinite companion of the two forms above, and the space is the biquaternion instance of the general theory. The natural conjugation ${}^{\natural}$ plays the role of the fundamental symmetry, and that is the subject of the next article.

## The Isotropic and Totally Isotropic Subspaces

**Theorem (Witt index).** The **Krein null set** $\{[\tilde{Q},\tilde{Q}]=0\}$ is a real algebraic cone of real dimension $7$ with no singular point except the origin; the maximal totally isotropic subspace has real dimension $2$ (complex dimension $1$), so the Witt index is $2$ over $\mathbb{R}$ and $1$ over $\mathbb{C}$.

**Proof.** The form is non-degenerate, so its zero set is a quadric cone of dimension $8-1=7$ with the origin as its only singular point; the maximal totally isotropic dimension of a non-degenerate Hermitian form of signature $(p,q)$ is $\min(p,q)$ (*Witt's Theorems*, and *Krein Spaces* for the indefinite case), which is $2$ over $\mathbb{R}$ and $1$ over $\mathbb{C}$.

**Proposition (a totally isotropic plane).** The real plane

$$
\mathcal{I}=\mathrm{span}_{\mathbb{R}}\{e_0+e_1,\ i(e_0+e_1)\}=\mathbb{C}\cdot(e_0+e_1)
$$

is totally isotropic of real dimension two: every element $\tilde{Q}=z(e_0+e_1)$ has $[\tilde{Q},\tilde{Q}]=|z|^{2}-|z|^{2}=0$, and $[\cdot,\cdot]$ vanishes on the pair.

**Proof.** For $\tilde{Q}=z(e_0+e_1)$ the coefficients are $Q_0=Q_1=z$, $Q_2=Q_3=0$, so $[Q,Q]=|z|^{2}-|z|^{2}=0$; for the pair $\tilde{Q}=z(e_0+e_1)$, $\tilde{Q}'=w(e_0+e_1)$ one has $[\tilde{Q},\tilde{Q}']=\bar zw-\bar zw=0$. Maximality is the theorem.

**Remark (the Krein null set is not the null cone).** The two null sets are different objects of the algebra and neither contains the other. The null cone $\mathcal{N}=\{N=0\}$ of *Biquaternion Topology* is the zero-divisor set, a **complex** cone of real dimension $6$; the Krein null set $\{[\tilde{Q},\tilde{Q}]=0\}$ is a **real** cone of real dimension $7$, its defining polynomial $\sum_\mu\varepsilon_\mu|Q_\mu|^{2}$ not being holomorphic. The two exclusions are witnessed on the generators:

- $\tilde{Q}=e_0+e_1$ is Krein-null, $[\tilde{Q},\tilde{Q}]=1-1=0$, while $N(\tilde{Q})=1+1=2\neq0$; it is isotropic but not a zero divisor.
- $\tilde{Q}=e_1+ie_2$ is null for $N$, $N(\tilde{Q})=1+i^{2}=0$, while $[\tilde{Q},\tilde{Q}]=0-1-1-0=-2\neq0$; it is a zero divisor but not Krein-isotropic.

Their intersection is not empty: $\tilde{Q}=e_0+ie_1$ satisfies both, $N(\tilde{Q})=1+i^{2}=0$ and $[\tilde{Q},\tilde{Q}]=1-1=0$, and so is a zero divisor that is also Krein-null — indeed $(e_0+ie_1)(e_0-ie_1)=0$. The two cones therefore cross, and the algebra's "null" ambiguity — which conjugation one polarises — is visible already in these three generators.

**Proof.** A complex hypersurface in $\mathbb{B}\cong\mathbb{C}^{4}$ has real dimension $6$ and a real equation has real dimension $7$; the examples are direct evaluations of $N$ and of the diagonal of $[\cdot,\cdot]$.

## Worked Examples

**A centre element.** $\tilde{Q}=e_0$: $[\tilde{Q},\tilde{Q}]=1$, positive; the centre is the positive line.

**A vector element.** $\tilde{Q}=e_1$: $[\tilde{Q},\tilde{Q}]=-1$; the vector subspace is the negative part.

**An isotropic element.** $\tilde{Q}=e_0+e_1$: $[\tilde{Q},\tilde{Q}]=1-1=0$; it is Krein-isotropic but not a zero divisor, since $N(\tilde{Q})=2\neq0$. This is the sharpest contrast with the bilinear form: Krein-null is not norm-null.

**A mixed element.** $\tilde{Q}=e_0+ie_1$: the coefficients are $1,i,0,0$, so $[\tilde{Q},\tilde{Q}]=1-1=0$ **and** $N(\tilde{Q})=1^{2}+i^{2}=0$; it lies in both null sets, and $(e_0+ie_1)(e_0-ie_1)=0$ exhibits it as a zero divisor. This is the case where the two notions of nullity coincide.

**A zero divisor that is not isotropic.** $\tilde{Q}=e_1+ie_2$: $N(\tilde{Q})=1+i^{2}=0$, while $[\tilde{Q},\tilde{Q}]=0-1-1-0=-2$; the two null sets are genuinely different.

## Summary

The **Krein form** of the biquaternion algebra is $[\tilde{Q},\tilde{Q}']=\mathrm{Sc}(\tilde{Q}^{\natural*}\tilde{Q}')=\sum_\mu\varepsilon_\mu Q_\mu^{*}Q'_\mu$, a Hermitian sesquilinear form built on the natural conjugation ${}^{\natural*}$, conjugate-linear in the first argument, non-degenerate and real on the diagonal. It has signature $(2,6)$ over $\mathbb{R}$ and $(1,3)$ over $\mathbb{C}$, with positive part the centre $\mathbb{C}_{\mathbb{B}}$ and negative part the vector subspace $\mathbb{V}_{\mathbb{B}}$, which are $\varepsilon$-orthogonal; this is the fundamental decomposition. On the vector subspace the form is $-N$ and on the Hermitian subspace it is $+N$, so the two Lorentzian real quaternion slices carry signature $(1,3)$. The algebra is thereby a Krein space of complex dimension four and negative index three, a Pontryagin space over $\mathbb{R}$; its null set is a real cone of dimension $7$, distinct from the complex null cone of $N$, and its maximal totally isotropic subspace has dimension $2$ over $\mathbb{R}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $[\tilde{Q},\tilde{Q}']=\mathrm{Sc}(\tilde{Q}^{\natural*}\tilde{Q}')$ | The Krein form; Hermitian, indefinite |
| $\varepsilon=(1,-1,-1,-1)$ | The sign vector; the diagonal signs |
| $(2,6)$ over $\mathbb{R}$, $(1,3)$ over $\mathbb{C}$ | The signature |
| $\mathbb{C}_{\mathbb{B}},\ \mathbb{V}_{\mathbb{B}}$ | Positive part (centre) and negative part (vector subspace) |
| $[\tilde V,\tilde V]=-N(\tilde V)$, $[\tilde H,\tilde H]=N(\tilde H)$ | The Lagrange identities |
| $\{[\tilde{Q},\tilde{Q}]=0\}$ | Krein null set; real cone, dimension $7$ |
| $\mathbb{C}\cdot(e_0+e_1)$ | A maximal totally isotropic subspace |
| $\Pi_6$ (over $\mathbb{R}$), $\Pi_3$ (over $\mathbb{C}$) | Pontryagin type of the Krein space |

## Further Reading

- *Indefinite Inner Product Spaces* (`articles_maths/indefinite-inner-product-spaces.md`), for the general theory of an indefinite inner product
- *Krein Spaces* (`articles_maths/krein-spaces.md`) and *Pontryagin Spaces* (`articles_maths/pontryagin-spaces.md`), for the complete and the finite-index cases
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the symmetry ${}^{\natural}$ that turns the Krein form into the Hermitian one
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`) and *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), for the two companion forms
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the real forms and their signatures
- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the signature theory of indefinite inner products
