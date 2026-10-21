# __The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde Q_1\star\tilde Q_2 = \mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})e_t = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$, with $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = Q_{1t}\overline{Q_{2t}} + (\vec Q_1,\overline{\vec Q_2})$ (*Introduction to the Symmetric Plain Sesqualgebra*). Its product and its form are the same data: the block is the Hermitian form of the corpus *read as a multiplication*, and every statement about the product is a statement about the form and conversely. This article develops the block from the side of the form: the identification and the rank-one structure it forces, the Gram matrix and the positivity, the Cauchy and Schwarz inequality with its equality case, the trace functional and the trace form, the failure of the invariance of the form under the product, the restriction of the form to the remarkable subspaces, and the bridge to the form of the quaternionic row.

The result that organises the article is that the form is the **definite** form of the algebra, of signature $(8,0)$ on the real space, while the product it defines is **rank one** and central: the image is the centre $\mathbb{C}_{\mathbb{B}}$, the form is recovered as the trace form $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{*}$, and the invariance that the trace form of the symmetric plain block enjoys — the invariance of a Jordan product — **fails** here. The two facts are one: a product whose values are central and whose form is definite cannot carry an associative or Jordan invariance, because the invariance is exactly the identity that forces the product to have a vector part.

**Boundaries.** The form $\langle\cdot,\cdot\rangle_{*}$, its positivity, its cone, its signature and its Gram matrix are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* and *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*; they are cited here and not restated, and this article owns only the reading of $\langle\cdot,\cdot\rangle_{*}$ as the product of the block. The trace form and the invariance of the symmetric plain block are *The Trace Form and the Invariance of the Symmetric Plain Algebra*; the quaternion form $\langle\cdot,\cdot\rangle_{\natural}$ and its comparison are *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* and *Comparison Between the Four General Products*. The remarkable subspaces are *Introduction to the Remarkable Subspaces*, and their reading under the general plain sesquilinear product is *Remarkable Subspaces under the General Plain Sesqualgebra*. Nothing topological and nothing metric appears; the form is used as an algebraic datum and no length, distance or norm of positive real values is written.

**Conventions.** As in the companion articles: $\mathbb{B}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, natural conjugation ${}^{\natural}$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$; the block product is $\tilde Q_1\star\tilde Q_2 = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ and $\langle\cdot,\cdot\rangle_{*}$ is the Hermitian form. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$.

## The Identification and the Rank-One Structure

**Theorem (the block is the form read as a product).** For all $\tilde Q_1,\tilde Q_2$,

$$
\tilde Q_1\star\tilde Q_2 = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t ,
$$

and the assignment $\tilde Q_1\star\tilde Q_2 \mapsto \langle\tilde Q_1,\tilde Q_2\rangle_{*}$ is a bijection between the products of the block and the values of the form; the block carries no information beyond the form.

**Proposition (the image is the centre, the product has rank one).** The image of the multiplication is the centre $\mathbb{C}_{\mathbb{B}}$; as a map $\mathbb{B}\otimes_{\mathbb{C}}\overline{\mathbb{B}} \to \mathbb{B}$ the product has rank one over $\mathbb{C}$, its single non-zero value direction being $e_t$. The kernel is the hyperplane of pairs with $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = 0$.

*Proof.* Every value is a complex multiple of $e_t$; the value $e_t$ is attained at $(\tilde Q_1,\tilde Q_2) = (e_t,e_t)$, and no value has a vector part; the condition for vanishing is the single scalar equation $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = 0$.

**Corollary (the product is not a multiplication with a unit).** Because the rank is one and the image is central, the block cannot have a unit and cannot reproduce an element with a vector part on either side; this is the rank-one reason for the absence of a unit proved in the companion article, and it is the reason the block's idempotents are the two central ones alone.

## The Gram Matrix and the Positivity

**Proposition (the Gram matrix is the identity).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$,

$$
\langle e_\mu,e_\nu\rangle_{*} = \delta_{\mu\nu} , \qquad e_\mu\star e_\nu = \delta_{\mu\nu}e_t ,
$$

so the Gram matrix of the form on the algebra basis is the identity matrix, and the multiplication table of the block is that matrix times $e_t$.

*Proof.* $\langle e_\mu,e_\nu\rangle_{*} = \sum_\rho (e_\mu)_\rho\overline{(e_\nu)_\rho} = \delta_{\mu\nu}$.

**Proposition (the positivity on the real basis).** On the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the form has $\langle e_\mu,e_\nu\rangle_{*} = \delta_{\mu\nu}$; on the real basis $e_\mu, ie_\mu$ of the real space $\mathbb{B}\cong\mathbb{R}^{8}$ the associated real symmetric form $\mathrm{Re}\,H$ is the identity form,

$$
\mathrm{Re}\,\langle e_\mu,e_\nu\rangle_{*} = \delta_{\mu\nu} , \qquad \mathrm{Re}\,\langle ie_\mu,ie_\nu\rangle_{*} = \delta_{\mu\nu} , \qquad \mathrm{Re}\,\langle e_\mu,ie_\nu\rangle_{*} = 0 ,
$$

so the quadratic form $\tilde Q\mapsto \langle\tilde Q,\tilde Q\rangle_{*}$ is **positive definite** of signature $(8,0)$ on the real space and its null set is $\{0\}$ alone.

*Proof.* $\langle ie_\mu,ie_\nu\rangle_{*} = (ie_\mu)\overline{(ie_\nu)}$ summed $= (-i)(i)\,\delta_{\mu\nu} = \delta_{\mu\nu}$, a real value; and $\langle e_\mu,ie_\nu\rangle_{*} = -i\,\langle e_\mu,e_\nu\rangle_{*} = -i\delta_{\mu\nu}$ by the conjugate-linearity in the second slot, whose real part vanishes.

**Proposition (the diagonal and the absence of an isotropic vector).** For every $\tilde Q$,

$$
\langle\tilde Q,\tilde Q\rangle_{*} = \lvert Q_t\rvert^{2} + (\vec Q,\overline{\vec Q}) = \sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^{2} ,
$$

real and strictly positive for $\tilde Q \neq 0$. Hence the form has **no isotropic vector**, and its isotropic cone is $\{0\}$.

*Proof.* $\langle\tilde Q,\tilde Q\rangle_{*} = \sum_\mu Q_\mu\overline{Q_\mu} = \sum_\mu\lvert Q_\mu\rvert^{2}$, a sum of non-negative terms, zero only when every coordinate vanishes.

## The Cauchy and Schwarz Inequality

**Theorem (the inequality).** For all $\tilde Q_1,\tilde Q_2$,

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}\,\overline{\langle\tilde Q_1,\tilde Q_2\rangle_{*}} \le \langle\tilde Q_1,\tilde Q_1\rangle_{*}\,\langle\tilde Q_2,\tilde Q_2\rangle_{*} ,
$$

that is $\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2} \le \langle\tilde Q_1,\tilde Q_1\rangle_{*}\langle\tilde Q_2,\tilde Q_2\rangle_{*}$, with equality if and only if $\tilde Q_1$ and $\tilde Q_2$ are linearly dependent over $\mathbb{C}$.

*Proof.* If $\tilde Q_2 = 0$ both sides vanish. Let $\tilde Q_2 \neq 0$ and put $\lambda = \langle\tilde Q_1,\tilde Q_2\rangle_{*}/\langle\tilde Q_2,\tilde Q_2\rangle_{*}$ and $\tilde Q_3 = \tilde Q_1 - \lambda\tilde Q_2$. Developing $\langle\tilde Q_3,\tilde Q_3\rangle_{*}$ with the linearity in the first argument and the conjugate-linearity in the second gives $\langle\tilde Q_3,\tilde Q_3\rangle_{*} = \langle\tilde Q_1,\tilde Q_1\rangle_{*} - \lambda \langle\tilde Q_2,\tilde Q_1\rangle_{*} - \overline{\lambda}\langle\tilde Q_1,\tilde Q_2\rangle_{*} + \lvert\lambda\rvert^{2}\langle\tilde Q_2,\tilde Q_2\rangle_{*}$, which reduces to $\langle\tilde Q_1,\tilde Q_1\rangle_{*} - \lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2}/\langle\tilde Q_2,\tilde Q_2\rangle_{*}$. The left-hand side is non-negative by the positivity of the form, so the inequality follows; equality is $\langle\tilde Q_3,\tilde Q_3\rangle_{*} = 0$, which by the absence of isotropic vectors is $\tilde Q_3 = 0$, that is $\tilde Q_1 = \lambda\tilde Q_2$.

**Remark (an inequality of the form, not of a distance).** The statement is an inequality between values of the sesquilinear form and is algebraic: it uses the positivity of the form and the quadratic development, and no length is attached to the elements. It is the Cauchy and Schwarz inequality of any positive definite Hermitian form, read here on the biquaternion space; the companion quaternion row, whose form $\langle\cdot,\cdot\rangle_{\natural}$ is indefinite, has no such inequality.

## The Trace Functional and the Trace Form

**Proposition (the trace form is the form).** For all $\tilde Q_1,\tilde Q_2$,

$$
\mathrm{Sc}(\tilde Q_1\star\tilde Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{*} ,
$$

so the block has **no second form**: the trace form of the multiplication and the form that defines it are one object.

*Proof.* $\tilde Q_1\star\tilde Q_2 = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ and $\mathrm{Sc}(e_t) = 1$.

**Remark (the trace functional).** The linear functional attached to the block is the scalar part $\mathrm{Sc}: \tilde Q_2 \mapsto Q_{2t}$, and in the $2\times2$ matrix model it is one half of the matrix trace, $\mathrm{Sc}(\tilde Q_2) = \tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde Q_2)$ (*The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*). On a value of the product it reads $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{*}$, and the matrix trace of a value is twice the form,

$$
\operatorname{Tr}\mathsf{M}_2(\tilde Q_1\star\tilde Q_2) = 2\,\langle\tilde Q_1,\tilde Q_2\rangle_{*} ,
$$

the trace identity of the model. There is no fourth form to compare with: the block has only $\langle\cdot,\cdot\rangle_{*}$.

## The Invariance under the Product

**Theorem (the invariance fails).** The form $\langle\cdot,\cdot\rangle_{*}$ is **not** invariant under the product: there are $\tilde Q_1,\tilde Q_2,\tilde Q_3$ with

$$
\langle\tilde Q_1\star\tilde Q_2,\tilde Q_3\rangle_{*} \neq \langle\tilde Q_1,\tilde Q_2\star\tilde Q_3\rangle_{*} .
$$

The witness is $\tilde Q_1 = \tilde Q_2 = \vec e_x$, $\tilde Q_3 = e_t$, where

$$
\langle \vec e_x\star \vec e_x,e_t\rangle_{*} = \langle e_t,e_t\rangle_{*} = 1 , \qquad \langle \vec e_x,\vec e_x\star e_t\rangle_{*} = \langle \vec e_x,0\rangle_{*} = 0 .
$$

*Proof.* $\vec e_x\star \vec e_x = \langle \vec e_x,\vec e_x\rangle_{*}e_t = e_t$, so the first quantity is $\langle e_t,e_t\rangle_{*} = 1$; and $\vec e_x\star e_t = \langle \vec e_x,e_t\rangle_{*}e_t = 0$, so the second vanishes.

**Remark (the comparison with the symmetric plain block).** The trace form of the symmetric plain block, $\tau(\tilde Q_1,\tilde Q_2) = \mathrm{Sc}(\tilde Q_1\bullet\tilde Q_2) = Q_{1t}Q_{2t} - (\vec Q_1,\vec Q_2)$, **is** invariant, $\tau(\tilde Q_1\bullet\tilde Q_2,\tilde Q_3) = \tau(\tilde Q_1,\tilde Q_2\bullet\tilde Q_3)$, and the invariance is the associativity of the plain product read on the Jordan product (*The Trace Form and the Invariance of the Symmetric Plain Algebra*). The block of this article fails the same test, and the reason is the rank-one central image: the invariance $\mathrm{Sc}((\tilde Q_1\star\tilde Q_2)\star\tilde Q_3) = \mathrm{Sc}(\tilde Q_1\star(\tilde Q_2\star\tilde Q_3))$ reads $\langle\tilde Q_1,\tilde Q_2\rangle_{*}\overline{Q_{3t}} = \overline{\langle\tilde Q_2,\tilde Q_3\rangle_{*}}\,Q_{1t} = \langle\tilde Q_3,\tilde Q_2\rangle_{*}Q_{1t}$ for all $\tilde Q_1,\tilde Q_2,\tilde Q_3$, and taking $\tilde Q_1 = \tilde Q_2 = \vec e_x$, $\tilde Q_3 = e_t$ gives $1$ on the left and $0$ on the right, so the identity fails. The product is conjugate-commutative and central, and its trace form cannot be associative.

## The Restriction to the Remarkable Subspaces

The form $\langle\cdot,\cdot\rangle_{*}$ restricts to each of the remarkable subspaces, and on each restriction it is again positive definite; the rank is the real dimension of the subspace and the positivity is inherited from the definite form of the whole space.

| subspace | real dimension | $\langle\cdot,\cdot\rangle_{*}$ restricted | rank over $\mathbb{R}$ | positivity |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $\lambda\overline{\mu}$ on the coordinate | $2$ | positive definite |
| $\mathrm{Vect}(\mathbb{B})$ | $6$ | $\sum_{k} Q_{1,k}\overline{Q_{2,k}}$ | $6$ | positive definite |
| $\mathbb{H}_{\mathbb{B}}$ | $4$ | $\sum_\mu Q_{1,\mu} Q_{2,\mu}$ on real coordinates | $4$ | positive definite |
| $i\mathbb{H}_{\mathbb{B}}$ | $4$ | $\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$ on imaginary coordinates | $4$ | positive definite |
| $\mathbb{M}_+$ | $4$ | $\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$, real-valued | $4$ | positive definite |
| $\mathbb{M}_-$ | $4$ | $\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$, real-valued | $4$ | positive definite |

**Proposition (the restrictions).** On each of the remarkable subspaces the restriction of $\langle\cdot,\cdot\rangle_{*}$ is positive definite, of rank equal to the real dimension of the subspace, and it is real-valued with the identity form in the natural real basis on $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$.

*Proof.* $\langle\cdot,\cdot\rangle_{*}$ is positive definite on the whole real space, so its restriction to every real subspace is positive definite, hence non-degenerate of rank the real dimension; on the four real subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ the natural real bases give the identity form, and on the two complex subspaces $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ the real bases $e_t,ie_t$ and $\vec e_k,i\vec e_k$ do the same.

**Corollary (the block and the remarkable subspaces).** Because the values of the product are central, the product of two elements of any one of the remarkable subspaces is a scalar multiple of $e_t$, real precisely on the four subspaces on which $\langle\cdot,\cdot\rangle_{*}$ is real-valued; and the subspace is closed under the product exactly when it contains the idempotent $e_t$: the centre, the quaternion subspace and the Hermitian subspace are closed, and the vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace are not. The restriction of the form is positive definite in every case; only the closure of the product separates the remarkable subspaces. This is the reading of the remarkable subspaces of *Remarkable Subspaces under the Symmetric Plain Sesqualgebra*, and the flatness of the table — every restriction positive, only the closure differing — is the mark of the central image.

## The Bridge to the Quaternion Form

**Theorem (the coincidence on the real subspace).** On the real elements, $\tilde Q_1,\tilde Q_2 \in \mathbb{H}_{\mathbb{B}}$,

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2) ,
$$

the quaternion form of the symmetric quaternionic block; off the real subspace the two forms part company.

*Proof.* For real coordinates $\overline{Q_{2,\mu}} = Q_{2,\mu}$, so $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \sum_\mu Q_{1,\mu} Q_{2,\mu} = Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$; the form $\langle\cdot,\cdot\rangle_{\natural}$ is *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*. For $\tilde Q_1 = \tilde Q_2 = ie_t$ one has $H = 1$ and $N = -1$, so the two differ off the real subspace.

**Corollary (the shared real part).** The two central blocks, the symmetric quaternionic and the symmetric plain sesquilinear, agree on the real elements and differ on the imaginary ones; in the table of the twelve the coincidence is recorded as $\mathrm{SQA} = \mathrm{SPS}$ on the real part. The bridge is the visible form of the two forms being the real and the complex reading of one pairing, the bilinear $\langle\cdot,\cdot\rangle_{\natural}$ and the sesquilinear $\langle\cdot,\cdot\rangle_{*}$.

## Worked Examples

**The basis and the Gram matrix.** $\langle e_\mu,e_\nu\rangle_{*} = \delta_{\mu\nu}$, so the Gram matrix is the identity and the table of the block is the identity times $e_t$. On $e_t + i\vec e_x$ the diagonal is $H = 2$ and the value of the square is $2e_t$.

**A non-real pairing.** $\langle e_t,ie_t\rangle_{*} = \overline{i} = -i$, while $\langle ie_t,e_t\rangle_{*} = i$; the two are conjugate, the Hermitian symmetry of the form.

**The invariance witness.** $\langle \vec e_x\star \vec e_x,e_t\rangle_{*} = 1$ and $\langle \vec e_x,\vec e_x\star e_t\rangle_{*} = 0$; the failure of the invariance is measured by the element $e_t$, on which the product vanishes.

**A Cauchy and Schwarz equality.** For $\tilde Q_1 = \lambda\tilde Q_2$ the two sides of the inequality are equal; for $\tilde Q_1 = e_t$, $\tilde Q_2 = \vec e_x$ they are $0 \le 1$.

## Summary

The symmetric plain sesqualgebra is the Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = Q_{1t}\overline{Q_{2t}} + (\vec Q_1,\overline{\vec Q_2})$ read as a multiplication, $\tilde Q_1\star\tilde Q_2 = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$; the product and the form are the same data, the image of the product is the centre and its rank is one. The Gram matrix of $\langle\cdot,\cdot\rangle_{*}$ on the algebra basis is the **identity**, the sixteen products are $e_\mu\star e_\nu = \delta_{\mu\nu}e_t$, and the form is **positive definite** of signature $(8,0)$ on the real space, with diagonal $\langle\tilde Q_2,\tilde Q_2\rangle_{*} = \sum_\mu\lvert Q_{2,\mu}\rvert^{2}$ strictly positive off the origin and no isotropic vector. The **Cauchy and Schwarz inequality** $\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2} \le \langle\tilde Q_1,\tilde Q_1\rangle_{*}\langle\tilde Q_2,\tilde Q_2\rangle_{*}$ holds, with equality exactly for linearly dependent $\tilde Q_1,\tilde Q_2$; it is an inequality of the form and not of a distance. The **trace form is the form itself**, $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{*}$, and the trace functional is the scalar part; in the $2\times2$ model $\operatorname{Tr}\mathsf{M}_2(\tilde Q_1\star\tilde Q_2) = 2\langle\tilde Q_1,\tilde Q_2\rangle_{*}$. The **invariance under the product fails**, with the witness $\langle \vec e_x\star \vec e_x,e_t\rangle_{*} = 1$ against $\langle \vec e_x,\vec e_x\star e_t\rangle_{*} = 0$, in contrast with the symmetric plain block whose trace form is invariant; the failure is the rank-one central image. On each of the **remarkable subspaces** the restriction is positive definite of rank the real dimension, and only the closure of the product separates the remarkable subspaces, the centre, the quaternion subspace and the Hermitian subspace being the closed ones. Finally $\langle\cdot,\cdot\rangle_{*}$ coincides with the quaternion form $\langle\cdot,\cdot\rangle_{\natural}$ on the real subspace, so the two central blocks agree there and differ on the imaginary elements.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2 = \langle\tilde Q_1,\tilde Q_2\rangle_{*}e_t$ | the block, the form read as a product |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*} = \sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$ | the Hermitian form of the block |
| $\langle e_\mu,e_\nu\rangle_{*} = \delta_{\mu\nu}$ | the Gram matrix is the identity |
| $\langle\tilde Q,\tilde Q\rangle_{*} = \sum_\mu\lvert Q_\mu\rvert^{2} > 0$ | the diagonal; no isotropic vector |
| $\lvert \langle\tilde Q_1,\tilde Q_2\rangle_{*}\rvert^{2} \le \langle\tilde Q_1,\tilde Q_1\rangle_{*}\langle\tilde Q_2,\tilde Q_2\rangle_{*}$ | the Cauchy and Schwarz inequality; equality iff dependent |
| $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2) = \langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | the trace form is the form |
| $\operatorname{Tr}\mathsf{M}_2(\tilde Q_1\star\tilde Q_2) = 2\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | the matrix trace of a value |
| $\langle \vec e_x\star \vec e_x,e_t\rangle_{*} = 1 \neq 0 = \langle \vec e_x,\vec e_x\star e_t\rangle_{*}$ | the failure of the invariance |
| $H = N$ on $\mathbb{H}_{\mathbb{B}}$ | the bridge to the quaternion form |

## Further Reading

- [Introduction to the Symmetric Plain Sesqualgebra](introduction-to-the-symmetric-plain-sesqualgebra.html), for the product, its central image and its table.
- [The Conjugate-Commutative Law and the Idempotents of the Symmetric Plain Sesqualgebra](the-conjugate-commutative-law-and-the-idempotents-of-the-symmetric-plain-sesqualgebra.html), for the law, the idempotents and the vanishing annihilator.
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the form $\langle\cdot,\cdot\rangle_{*}$, its positivity and its signature on the six real forms.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the cone generated by the form at the two equal arguments.
- [The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra](the-canonical-hermitian-form-on-the-regular-module-of-the-biquaternion-algebra.html), for the module-theoretic reading of the same form.
- [The Trace Form and the Invariance of the Symmetric Plain Algebra](the-trace-form-and-the-invariance-of-the-symmetric-plain-algebra.html), the sibling whose trace form is invariant, for the comparison.
- [The Quaternion Form as a Product on the Symmetric Quaternionic Algebra](the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.html), for the form $\langle\cdot,\cdot\rangle_{\natural}$ and the bridge.
- [Comparison Between the Four General Products](comparison-between-the-four-general-products.html), for the four forms of the space and the coincidence $\mathrm{SQA} = \mathrm{SPS}$ on the real part.
- [Remarkable Subspaces under the Symmetric Plain Sesqualgebra](remarkable-subspaces-under-the-symmetric-plain-sesqualgebra.html), for the remarkable subspaces under the product.
