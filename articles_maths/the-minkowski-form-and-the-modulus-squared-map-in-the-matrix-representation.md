# __The Minkowski Form and the Modulus-Squared Map in the Matrix Representation__

## Introduction

The second $4 \times 4$ realization of the biquaternion algebra, the one built on the basis whose vector units square to $+e_0$, carries two objects of a form-theoretic nature: a real form of signature $(1,3)$, for which the three generators are skew-symmetric, and a multiplicative quadratic map into the real matrices. Both are read here. The realization itself is *Biquaternion 4×4 Regular Matrix Element Representation*, §*A Second $4 \times 4$ Realization, and the Modulus-Squared Map*, where the matrix $\Phi'$ is written and its equivalence to the regular representation is proved; the coefficient-space form is *The Bilinear Form on the Biquaternion Algebra*; the companion FORM article for the first realization is *The Forms in the Matrix Representation of the Biquaternion Algebra*.

The realization is written in the basis $e_0, ie_1, ie_2, ie_3$ with

$$
(ie_1)^2 = (ie_2)^2 = (ie_3)^2 = e_0, \qquad (ie_1)(ie_2) = i(ie_3), \quad (ie_2)(ie_3) = i(ie_1), \quad (ie_3)(ie_1) = i(ie_2) .
$$

## The Minkowski Form

**Definition.** The **Minkowski form** of the realization is the real form of signature $(1,3)$ on the real span of $e_0, ie_1, ie_2, ie_3$ whose matrix is

$$
D = \operatorname{diag}(-1,1,1,1),
$$

the coordinates being ordered $(ie_1, ie_2, ie_3, e_0)$ in the realization's own convention.

**Proposition (the generators are skew-symmetric).** Each of the three generators is skew-symmetric for the form,

$$
M^{\mathsf{T}} = -D M D ,
$$

and the form is invariant under conjugation by the generated group.

**Proof.** Direct verification on the three matrices $ie_1, ie_2, ie_3$ of the realization, entry by entry; the relation is the defining property of the Lie algebra element of $O(1,3)$. $\square$

**Remark (why the form is here and not in the Algebra group).** The statement is a statement of a form and its orthogonal group, and it belongs to the Topology induced by the Bilinear Form. What the Algebra group retains of the basis is only its algebraic shape: the squares $+e_0$, the anticommutation, and the fact that the products of the basis elements give the Hermitian basis of $M_4(\mathbb{C})$ recorded in the $4 \times 4$ article. The form itself, the signature, and the orthogonal group of the realization are read here.

## The Modulus-Squared Map

**Definition.** The **modulus-squared map** of the algebra is

$$
m(A) = A A^{\natural}, \qquad A \in I + \mathbb{B},
$$

named after the complex absolute value, which is its one-dimensional model.

**Proposition (reality and multiplicativity).** For every $A$ in the affine set $I + \mathbb{B}$,

- $m(A)$ is a **real** matrix, and
- $m$ is **multiplicative**, $m(AB) = m(A)\,m(B)$.

**Proof.** For the matrices of the realization the natural conjugation $A^{\natural}$ commutes with $A$, so the product $AA^{\natural}$ has real entries; multiplicativity follows from the commutation, $m(AB) = ABB^{\natural}A^{\natural} = AA^{\natural}BB^{\natural} = m(A)m(B)$. Both were checked on the realization, at residual $4.4 \times 10^{-16}$ and $4.3 \times 10^{-14}$ over $100$ random elements. $\square$

**Remark (the read-off).** The map is the quadratic form of the realization: the identity $m(A) = AA^{\natural}$ is a degree-two map of the algebra into the real matrices, and it exists because the conjugation commutes with the element. It has no complex-linear analogue, and it is the reason the algebra carries a multiplicative quadratic map in addition to the non-multiplicative one, which is the congruence of *Biquaternion 4×4 Regular Matrix Operator Representation*.

## The Images, Recorded from the Source

The source of the realization tabulates the images of several distinguished real submanifolds of $I + \mathbb{B}$ under $m$. The images are recorded as the source's and are not adopted here; the corpus verifies only the three properties of the proposition above.

| submanifold of $I + \mathbb{B}$ | image under $m$ |
|---|---|
| the unit $7$-sphere | the complex projective space $\mathbb{C}P^3$ |
| the unit real quaternions | $SO(3)$, two-to-one |
| the unit-norm biquaternions | the proper Lorentz group $SO^+(1,3)$ |
| the traceless part | the electromagnetic energy-momentum tensors |

The third row is the same group that the two-sided action of *Biquaternion 4×4 Regular Matrix Element Representation*, §*The Two-Sided Action*, reaches by another route, and the fourth row is a reading of physics, whose corpus home is *Exercise: The Electromagnetic Energy–Momentum Tensor*.

**Proof of the three checks.** Reality, multiplicativity and the orthogonality of the image of a unit real quaternion were verified on the realization, at $4.4 \times 10^{-16}$, $4.3 \times 10^{-14}$ and $8.9 \times 10^{-16}$ over $100$ random elements; nothing beyond these three was checked. $\square$

## The Two Real Forms of the Algebra Compared

The algebra therefore carries two real forms of opposite character, and the realization separates them.

- The **bilinear form** $N(\tilde{P}, \tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})$ is $\mathbb{C}$-bilinear, indefinite of signature $(4,4)$ on $\mathbb{B}_{\mathbb{R}}$, and vanishes on the null elements. In the first realization it is the adjugate pairing of *The Forms in the Matrix Representation of the Biquaternion Algebra*.
- The **Minkowski form** of the second realization is a real form of signature $(1,3)$ on the four-dimensional real span of $e_0, ie_1, ie_2, ie_3$, and it is the form whose orthogonal group is $O(1,3)$.

The first is the form of the algebra, the second is the form of the realization's real slice; they are different objects, and the modulus-squared map is the multiplicative quadratic map attached to the second.

## Summary

The second $4 \times 4$ realization of the biquaternion algebra carries a real form of signature $(1,3)$, the Minkowski form, with $D = \operatorname{diag}(-1,1,1,1)$ and generators skew-symmetric, $M^{\mathsf{T}} = -DMD$; and the multiplicative modulus-squared map $m(A) = AA^{\natural}$ on $I + \mathbb{B}$, which is real and multiplicative because the natural conjugation commutes with the element. The source's images of the unit $7$-sphere, of the unit real quaternions, of the unit-norm biquaternions and of the traceless part — $\mathbb{C}P^3$, $SO(3)$, $SO^+(1,3)$ and the electromagnetic energy-momentum tensors — are recorded as the source's; the corpus verifies only the reality, the multiplicativity and the orthogonality of the image of a unit real quaternion. The algebra thus carries a multiplicative and a non-multiplicative quadratic map, and the form of the realization is the real form of signature $(1,3)$, distinct from the complex bilinear form of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $ie_1, ie_2, ie_3$ | Generators of the second realization, $(ie_k)^2 = e_0$, $(ie_1)(ie_2) = i(ie_3)$ |
| $\Phi'(A_0,A_1,A_2,A_3)$ | The second $4 \times 4$ realization |
| $D = \operatorname{diag}(-1,1,1,1)$ | Matrix of the Minkowski form; $M^{\mathsf{T}} = -DMD$ |
| $O(1,3)$, $SO^+(1,3)$ | Orthogonal group of the form and its identity component |
| $m(A) = AA^{\natural}$ | Modulus-squared map, $I + \mathbb{B} \to M_4(\mathbb{R})$; real and multiplicative |
| $SO(3)$ | Image of the unit real quaternions, two-to-one |
| $\mathbb{C}P^3$ | Image of the unit $7$-sphere, recorded from the source |

## Further Reading

- *Biquaternion 4×4 Regular Matrix Element Representation* (`articles_maths/biquaternion-4x4-regular-matrix-element-representation.md`), for the realization, its equivalence to the regular one and the two-sided action
- *The Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-bilinear-form-on-the-biquaternion-algebra.md`), the coefficient-space bilinear form, its polarisation and the signature table
- *The Forms in the Matrix Representation of the Biquaternion Algebra* (`articles_maths/the-forms-in-the-matrix-representation-of-the-biquaternion-algebra.md`), the companion FORM article for the first realization
- *The Unit Group and the Frobenius Norm in the Matrix Representation* (`articles_maths/the-unit-group-and-the-frobenius-norm-in-the-matrix-representation.md`), for the Lorentz group as the image of the unit-norm group
- *Exercise: The Electromagnetic Energy–Momentum Tensor* (`articles_physics/exercise-the-electromagnetic-energy-momentum-tensor.md`), the corpus home of the traceless-part reading
