# __The Six Subspaces under the Antisymmetric Quaternionic Algebra of Biquaternions__

## Introduction

The antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ is a $\mathbb{C}$-bilinear alternating operation with a zero scalar part, its image is the vector subspace, and it fails the Jacobi identity, with the failure carried by the scalar-vector interaction (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*, *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*). This article reads the operation on the six distinguished subspaces of the algebra, one subspace to a section: the centre, the vector subspace, the quaternion and anti-quaternion subspaces, and the Hermitian and anti-Hermitian subspaces (*Introduction to the Six Subspaces*). The pattern is the one of *The Six Subspaces under the General Quaternionic Algebra of Biquaternions*, whose table of restrictions is read here for the product rather than for the form.

The outcome is a short and asymmetric table. The operation **vanishes identically on the centre**, which is therefore a subalgebra on which the identity holds. It is the **negative of the cross product on the vector subspace**, which is closed, is the image of the whole operation, and is the one subspace other than the centre on which the Jacobi identity holds. It is a **real cross-product operation on the quaternion subspace**, which is closed and whose image is the triple of imaginary quaternions. And it **fails to close** on the anti-quaternion, Hermitian and anti-Hermitian subspaces, each with a smallest witness: the anti-quaternion subspace squares into the quaternion subspace, the Hermitian subspace produces a real cross term, and the anti-Hermitian subspace produces an imaginary mixed term. The failure of the Jacobi identity follows the same cut: the identity holds on the centre and on the vector subspace and fails on the other four. The article closes with the elements whose bracket vanishes and with the isotropic elements of the block, which are the elements of the vector subspace itself.

## The Centre

**Proposition.** The centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ is closed under the operation, and the operation vanishes identically on it: $Ae_0\diamond Be_0=0$ for all $A,B\in\mathbb{C}$. A nonzero central element is not an annihilator of the operation: $Ae_0\diamond\tilde Q=A\mathbf Q$ and $\tilde Q\diamond Ae_0=-A\mathbf Q$.

*Proof.* A central element has zero vector part, so both mixed terms and the cross term vanish in $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$. A central element in one slot is not an annihilator: $Ae_0\diamond\tilde Q=A\mathbf Q$ and $\tilde Q\diamond Ae_0=-A\mathbf Q$, which vanish for all $\tilde Q$ only when $A=0$, since the vector subspace is not zero. $\square$

The centre is thus an abelian subalgebra of the block, of complex dimension one, and it is not the centre of the operation: the alternating centre of the block is zero (*The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*). A central element acts on the vector part of every element and is acted on by it, so the centre of the algebra has ceased to be central for the operation, and the two notions of centre separate at the first subspace.

## The Vector Subspace

**Proposition.** The vector subspace $\mathrm{Vect}(\mathbb{B})=\{\tilde Q:\tilde Q^{\natural}=-\tilde Q\}$ is closed under the operation; on it the operation is the negative of the cross product,

$$
\tilde P\diamond\tilde Q = -\,\mathbf P\times\mathbf Q \qquad (\mathbf P,\mathbf Q \text{ pure}) ,
$$

it is a Lie algebra, and it is the image of the operation on the whole algebra. Its complex dimension is three and its real dimension six.

*Proof.* On pure vectors the two scalar parts vanish, so the explicit form is the cross term alone, $-\mathbf P\times\mathbf Q$, which is a pure vector again; the closure follows, and the cross product satisfies the Jacobi identity, so the restriction is a Lie algebra. For the image, every value of the operation is a pure vector, and every pure vector is a value, $\mathbf V=e_0\diamond\mathbf V$; the dimensions are those of the subspace. $\square$

The vector subspace and the quaternion subspace are the two closed ones of positive dimension, and the vector subspace is the only one of the six on which the operation is a Lie bracket, the closed quaternion subspace failing the Jacobi identity. It is the derived subalgebra of the block, and the identification of the cross product on $\mathbb{C}^3$ with $\mathfrak{sl}(2,\mathbb{C})$ is *The Six Subspaces and the Four Complex Products*.

## The Quaternion Subspace

**Proposition.** The quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$ is closed under the operation and its image is the real span of $e_1,e_2,e_3$, of real dimension three. On it the operation is the real mixed term with the real cross term subtracted,

$$
\tilde P\diamond\tilde Q = p_0\mathbf Q-q_0\mathbf P-\mathbf P\times\mathbf Q , \qquad p_0,q_0\in\mathbb{R},\ \mathbf P,\mathbf Q\in\mathbb{R}^3 ,
$$

and the Jacobi identity fails on it, at the triple $(e_0,e_1,e_2)$ with cyclic sum $-e_3$.

*Proof.* A real quaternion has real scalar and vector parts, so the value has a real vector part and zero scalar part and lies in $\mathbb{R}\{e_1,e_2,e_3\}\subset\mathbb{H}_{\mathbb{B}}$; the image is reached by the cross product of the real vectors, which fills $\mathbb{R}^3$. The witness is the one of the block, and its three elements are real. $\square$

The quaternion subspace is the largest of the six on which the operation is a real operation with the same shape as the complex one: the formula reads with the real scalars $p_0,q_0$ and the real cross product, and the operation is closed. It is not a Lie algebra, because the mixed terms survive.

## The Anti-Quaternion Subspace

**Proposition.** The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{ie_0,ie_1,ie_2,ie_3\}$ is **not** closed under the operation. It maps into the quaternion subspace,

$$
(i\mathbb{H}_{\mathbb{B}})\diamond(i\mathbb{H}_{\mathbb{B}}) \subseteq \mathbb{H}_{\mathbb{B}} , \qquad (i\mathbb{H}_{\mathbb{B}})\diamond\mathbb{H}_{\mathbb{B}} \subseteq i\mathbb{H}_{\mathbb{B}} ,
$$

its image is the real span of $e_1,e_2,e_3$, and the smallest witness of the failure of closure is $ie_1\diamond ie_2=e_3$.

*Proof.* For $\tilde P=i\tilde h$, $\tilde Q=i\tilde h'$ with $\tilde h,\tilde h'$ real, the explicit form gives $i\tilde h\diamond i\tilde h' = -h_0\mathbf h'+h'_0\mathbf h+\mathbf h\times\mathbf h'$, which has zero scalar part and a real vector part, so it lies in $\mathbb{R}\{e_1,e_2,e_3\}\subset\mathbb{H}_{\mathbb{B}}$; at $\tilde h=e_1$, $\tilde h'=e_2$ it is $e_3$, which is not in $i\mathbb{H}_{\mathbb{B}}$, since its coefficients are real and it is nonzero. The second inclusion is the graded statement: $i\tilde h\diamond\tilde h' = i(h_0\mathbf h'-h'_0\mathbf h-\mathbf h\times\mathbf h')\in i\mathbb{H}_{\mathbb{B}}$. $\square$

The anti-quaternion subspace is the odd part of a $\mathbb{Z}/2$-grading of the algebra, $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$, and the operation respects the grading: the even part is a subalgebra, the mixed products go to the odd part, and the square of the odd part lands back in the even part. The failure of closure is exactly the statement that the odd part is not a subalgebra, and the failure is total, not marginal: every pair of non-parallel imaginary vectors produces a real vector outside the subspace.

## The Hermitian Subspace

**Proposition.** The Hermitian subspace $\mathbb{M}_{+}=\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ is **not** closed under the operation. Its image is the whole vector subspace $\mathrm{Vect}(\mathbb{B})$, and the smallest witness of the failure of closure is $ie_1\diamond ie_2=e_3$, whose product has a real vector part.

*Proof.* For $\tilde P=a_0e_0+i\mathbf p$, $\tilde Q=b_0e_0+i\mathbf q$ with $a_0,b_0$ real and $\mathbf p,\mathbf q$ real, the explicit form gives $i(a_0\mathbf q-b_0\mathbf p)+\mathbf p\times\mathbf q$. The first term is a purely imaginary vector, which lies in $\mathbb{M}_{+}$, and the second is a real vector, which does not; the value lies in $\mathbb{M}_{+}$ exactly when $\mathbf p\times\mathbf q=0$, that is when the two vector parts are parallel. At $\mathbf p=e_1$, $\mathbf q=e_2$ the cross term is $e_3\notin\mathbb{M}_{+}$. The image is the whole vector subspace, the imaginary part ranging over $\mathbb{R}^3$ through $a_0\mathbf q-b_0\mathbf p$ and the real part over $\mathbb{R}^3$ through the cross product. $\square$

The failure of the Hermitian subspace is the failure of the real cross term to stay in the subspace. Its elements carry a real scalar and a purely imaginary vector, and the operation produces a real vector, which is exactly the direction the subspace lacks. The failure is not symmetric in the two slots beyond the antisymmetry of the operation, but it is present for every pair of non-parallel vector parts, so the subspace is as far from closed as the pair of non-parallel imaginary vectors allows.

## The Anti-Hermitian Subspace

**Proposition.** The anti-Hermitian subspace $\mathbb{M}_{-}=\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ is **not** closed under the operation. Its image is the whole vector subspace $\mathrm{Vect}(\mathbb{B})$, and the smallest witness of the failure of closure is $ie_0\diamond e_1=ie_1$, whose product has a purely imaginary vector part.

*Proof.* For $\tilde P=ia_0e_0+\mathbf p$, $\tilde Q=ib_0e_0+\mathbf q$ with $a_0,b_0$ real and $\mathbf p,\mathbf q$ real, the explicit form gives $-\mathbf p\times\mathbf q+i(a_0\mathbf q-b_0\mathbf p)$. The first term is a real vector, which lies in $\mathbb{M}_{-}$, and the second is a purely imaginary vector, which does not; the value lies in $\mathbb{M}_{-}$ exactly when $a_0\mathbf q=b_0\mathbf p$. At $\mathbf p=0$, $\mathbf q=e_1$, $a_0=1$ the value is $ie_1\notin\mathbb{M}_{-}$. The image is the whole vector subspace, the real part ranging over $\mathbb{R}^3$ through the cross product and the imaginary part over $\mathbb{R}^3$ through $a_0\mathbf q-b_0\mathbf p$. $\square$

The two Hermitian subspaces fail by the two complementary mixed terms, the real cross term for $\mathbb{M}_{+}$ and the imaginary mixed term for $\mathbb{M}_{-}$, and they are exchanged by multiplication by the central unit $i$; the operation is not central-linear in the required way, and the exchange reverses the sign of the two mixed terms. The pair of failures is the mirror image of the pair of the quaternion and anti-quaternion subspaces, where the even part is closed and the odd part is not.

## The Elements Whose Bracket Vanishes

**Proposition (the vanishing condition).** For $\tilde P=P_0e_0+\mathbf P$ and $\tilde Q=Q_0e_0+\mathbf Q$, the value $\tilde P\diamond\tilde Q$ vanishes exactly when

$$
\mathbf P\times\mathbf Q = P_0\mathbf Q - Q_0\mathbf P .
$$

Proportional elements always vanish, $\tilde P\diamond(\lambda\tilde P)=0$; among the sixteen pairs of basis elements the value vanishes exactly on the four diagonal pairs, $e_\mu\diamond e_\mu=0$; and if the vector parts are linearly independent and span a non-degenerate plane, then no pair of elements with those vector parts vanishes.

*Proof.* The condition is the explicit form set to zero. Proportionality gives $\tilde P\diamond(\lambda\tilde P)=\lambda\,\tilde P\diamond\tilde P=0$ by alternation. On the basis, the mixed pairs give $\pm e_k$ and the pairs of distinct pure vectors give $\mp e_l$, all nonzero, so only the diagonal vanishes. For the last clause, the cross product $\mathbf P\times\mathbf Q$ is orthogonal to the plane spanned by $\mathbf P$ and $\mathbf Q$, while the right side $P_0\mathbf Q-Q_0\mathbf P$ lies in that plane; if the plane is non-degenerate its intersection with its orthogonal complement is zero, so both sides vanish, the cross product forcing $\mathbf P,\mathbf Q$ to be dependent, in contradiction with the hypothesis. The exceptional pairs therefore occur only when the plane of the two vector parts is degenerate. $\square$

**Remark.** The block therefore has no nontrivial annihilating pairs beyond the proportional ones and the degenerate-plane exceptions. This is the sharp difference from the plain row, whose bracket $\tilde P\wedge\tilde Q=\mathbf P\times\mathbf Q$ vanishes whenever either argument is central or the two vector parts are parallel; here a central argument does not annihilate, and the two mixed terms are what prevent it. The alternating centre and the annihilator of the block are both zero (*The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra*).

## The Isotropic Elements

**Proposition.** Every element satisfies $\tilde Q\diamond\tilde Q=0$, the operation being alternating. For the unique invariant form of the block, $\varphi(\tilde P,\tilde Q)=P_0Q_0$, the isotropic elements, those with $\varphi(\tilde Q,\tilde Q)=0$, are exactly the elements of the vector subspace.

*Proof.* The diagonal vanishes by alternation. $\varphi(\tilde Q,\tilde Q)=Q_0^2$ vanishes exactly when $Q_0=0$, which is the defining equation of the vector subspace. $\square$

The two notions of isotropy separate. The block's own square vanishes on every element, so the diagonal carries no information, and the only non-trivial isotropy is the isotropy of the invariant form, which singles out the vector subspace. It is the same subspace that is the image of the operation and the radical of the form (*The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*); the vector subspace is thus at once the image, the radical, the isotropic cone and one of the two subspaces on which the Jacobi identity holds.

## The Table of the Six

| subspace | $\dim_{\mathbb{C}}/\dim_{\mathbb{R}}$ | $\diamond$ on the subspace | image | closed | Jacobi |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $1/2$ | identically $0$ | $0$ | yes | holds |
| $\mathrm{Vect}(\mathbb{B})$ | $3/6$ | $-\mathbf P\times\mathbf Q$ | $\mathrm{Vect}(\mathbb{B})$ | yes | holds |
| $\mathbb{H}_{\mathbb{B}}$ | $-/4$ | $p_0\mathbf Q-q_0\mathbf P-\mathbf P\times\mathbf Q$ | $\mathbb{R}\{e_1,e_2,e_3\}$ | yes | fails |
| $i\mathbb{H}_{\mathbb{B}}$ | $-/4$ | $-h_0\mathbf h'+h'_0\mathbf h+\mathbf h\times\mathbf h'$ | $\mathbb{R}\{e_1,e_2,e_3\}$ | no | fails |
| $\mathbb{M}_{+}$ | $-/4$ | $i(a_0\mathbf q-b_0\mathbf p)+\mathbf p\times\mathbf q$ | $\mathrm{Vect}(\mathbb{B})$ | no | fails |
| $\mathbb{M}_{-}$ | $-/4$ | $-\mathbf p\times\mathbf q+i(a_0\mathbf q-b_0\mathbf p)$ | $\mathrm{Vect}(\mathbb{B})$ | no | fails |

**Remark.** Three of the six are closed — the centre, the vector subspace and the quaternion subspace — and three are not. Of the three closed ones the centre carries the zero operation, the vector subspace the negative of the cross product and the quaternion subspace the real instance of the block; all three are subspaces on which the operation is again a $\mathbb{C}$- or $\mathbb{R}$-bilinear alternating operation with the same shape, and only the vector subspace carries the Jacobi identity. Of the three that fail, the anti-quaternion subspace fails into the quaternion subspace and the two Hermitian subspaces fail into the vector subspace, so no failure leaves the algebra and every failure is a failure of the subspace to contain a value it produces.

## Summary

The six distinguished subspaces read the antisymmetric quaternionic multiplication as follows. On the centre the operation vanishes identically, and the centre is an abelian subalgebra but not the centre of the operation. On the vector subspace the operation is the negative of the cross product, it is closed and a Lie algebra, and it is the image of the whole operation and the radical and isotropic cone of the invariant form. On the quaternion subspace the operation is the real instance of itself, closed, with the imaginary quaternions as image, and the Jacobi identity already fails there. On the anti-quaternion subspace the operation is not closed, its square landing in the quaternion subspace, and the mixed products land in the anti-quaternion subspace, so the subspace is the odd part of a $\mathbb{Z}/2$-grading whose even part is the quaternion subspace. On the Hermitian subspace the operation fails to close through the real cross term and on the anti-Hermitian subspace through the imaginary mixed term, both with image the whole vector subspace. Of the six, three are closed and three are not, and the Jacobi identity holds on the centre and on the vector subspace and fails on the other four. The elements whose bracket vanishes are the proportional pairs and the degenerate-plane exceptions, with only the diagonal basis pairs vanishing; the elements isotropic for the invariant form are exactly the elements of the vector subspace, the same subspace that is the image and the radical.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, on which the operation vanishes |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, closed, the image, the isotropic cone of the form |
| $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$ | the quaternion subspace, closed, the even part of the grading |
| $i\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{ie_0,ie_1,ie_2,ie_3\}$ | the anti-quaternion subspace, the odd part, not closed |
| $\mathbb{M}_{+}=\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ | the Hermitian subspace, not closed |
| $\mathbb{M}_{-}=\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ | the anti-Hermitian subspace, not closed |
| $(e_0,e_1,e_2)$ | the witness of the Jacobi failure, cyclic sum $-e_3$ |
| $(ie_1,ie_2)$ | the witness of the failure of closure of $i\mathbb{H}_{\mathbb{B}}$ and of $\mathbb{M}_{+}$, value $e_3$ |
| $(ie_0,e_1)$ | the witness of the failure of closure of $\mathbb{M}_{-}$, value $ie_1$ |
| $\varphi(\tilde P,\tilde Q)=P_0Q_0$ | the invariant form, whose isotropic elements are $\mathrm{Vect}(\mathbb{B})$ |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces, their bases and their dimensions
- *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the companion reading of the same six subspaces under the parent product
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its table and its image
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`), for the failure read on the subspaces and for the vanishing of the alternating centre
- *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-invariant-bilinear-forms-of-the-antisymmetric-quaternionic-algebra.md`), for the radical and the isotropic cone of the form, and for the restrictions to the six subspaces
- *The Six Subspaces and the Four Complex Products* (`articles_maths/the-six-subspaces-and-the-four-complex-products.md`), for the cross product on the vector subspace and its identification with $\mathfrak{sl}(2,\mathbb{C})$
