
# __The General Quaternionic Algebra in the $2\times2$ Matrix Representation__

## Introduction

The reading group *Topology on the Introduction to the General Quaternionic Algebra of Biquaternions* reads the algebra through the **general quaternionic bilinear form** $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})=\sum_\mu P_\mu Q_\mu$ and through the **quaternionic product** $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}$ that form polarises, whose algebra is *Introduction to the General Quaternionic Algebra of Biquaternions*. This article reads that group through the $2\times2$ matrix realization $\Phi$ of *Introduction to the $2\times2$ Matrix Representation of Biquaternions*, and it is the first of the two representation articles of the group; the companion *The General Quaternionic Algebra in the $4\times4$ Matrix Representation* repeats the reading on the left regular representation.

The natural conjugation is the characteristic operation of the group, and in the model it is the **adjugate**: $\Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q})$. The quaternionic product is therefore the ordinary matrix product with the adjugate inserted in the first slot, $\Phi(\tilde{P}\star\tilde{Q})=\operatorname{adj}\Phi(\tilde{P})\,\Phi(\tilde{Q})$, and the general quaternionic bilinear form is the adjugated trace pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$. The determinant is the norm, so the whole element theory of the group is read off the determinant of the matrix.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; the quaternionic product is $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}$ and its norm is $N(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$. All matrix claims are recomputed in the verification script of the pass.

## The Representation

**Definition.** The **matrix realization** is the $\mathbb{C}$-linear isomorphism

$$
\Phi:\mathbb{B}\longrightarrow M_2(\mathbb{C}),\qquad \Phi(e_0)=I,\qquad \Phi(e_k)=-i\sigma_k ,
$$

so that $\Phi(\tilde{Q})=\begin{pmatrix} Q_0-iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & Q_0+iQ_3\end{pmatrix}$. Its two invariants and its two conjugations are

$$
\operatorname{Tr}\Phi(\tilde{Q})=2Q_0,\qquad \det\Phi(\tilde{Q})=N(\tilde{Q})=\sum_\mu Q_\mu^2,\qquad \Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q}),\qquad \Phi(\tilde{Q}^{*})=\Phi(\tilde{Q})^{\dagger} .
$$

The adjugate is also the conjugate of the transpose by a fixed matrix, $\operatorname{adj}\Phi(\tilde{Q})=\Phi(-e_2)\,\Phi(\tilde{Q})^{\mathsf{T}}\,\Phi(-e_2)^{-1}$, so the natural conjugation is a transposition and not a Hermitian transposition.

## The Quaternionic Product in the Model

**Theorem (the product is the adjugated matrix product).** For all biquaternions,

$$
\Phi(\tilde{P}\star\tilde{Q})=\operatorname{adj}\Phi(\tilde{P})\,\Phi(\tilde{Q}),
$$

the ordinary matrix product with the adjugate in the first slot.

*Proof.* $\tilde{P}\star\tilde{Q}=\tilde{P}^{\natural}\tilde{Q}$ and $\Phi$ is multiplicative, so $\Phi(\tilde{P}\star\tilde{Q})=\Phi(\tilde{P}^{\natural})\Phi(\tilde{Q})=\operatorname{adj}\Phi(\tilde{P})\,\Phi(\tilde{Q})$.

**The adjugate reverses the order.** The mechanism of the whole reading is the reversal of the order under transposition. For all $A,B\in M_2(\mathbb{C})$,

$$
\operatorname{adj}(AB)=\operatorname{adj}(B)\operatorname{adj}(A),\qquad \operatorname{adj}(AB)\neq\operatorname{adj}(A)\operatorname{adj}(B)\ \text{in general},
$$

since $\operatorname{adj}(X)=\varepsilon X^{\mathsf{T}}\varepsilon^{-1}$ and $(AB)^{\mathsf{T}}=B^{\mathsf{T}}A^{\mathsf{T}}$. The inequality is seen on the images of the basis: $\operatorname{adj}\Phi(e_1)\operatorname{adj}\Phi(e_2)=\Phi(e_1)\Phi(e_2)=\Phi(e_3)$, against $\operatorname{adj}\Phi(e_1e_2)=\operatorname{adj}\Phi(e_3)=-\Phi(e_3)$. Associativity of the product would require the adjugate inserted in the first slot to move across the other factors, and it does not, because a transpose does not commute with a product.

**Theorem (the trace and the determinant of a value).** For all biquaternions, with $\beta(\tilde{P},\tilde{Q})=\sum_\mu P_\mu Q_\mu$,

$$
\operatorname{Tr}\Phi(\tilde{P}\star\tilde{Q})=2\beta(\tilde{P},\tilde{Q}),\qquad \det\Phi(\tilde{P}\star\tilde{Q})=\langle\tilde{P},\tilde{P}\rangle_{\natural}\langle\tilde{Q},\tilde{Q}\rangle_{\natural}.
$$

*Proof.* The determinant is multiplicative and $\det\operatorname{adj}(A)=\det A$, so $\det\Phi(\tilde{P}\star\tilde{Q})=\det\Phi(\tilde{P})\det\Phi(\tilde{Q})=\langle\tilde{P},\tilde{P}\rangle_{\natural}\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$. For the trace, $\operatorname{Tr}\Phi(\tilde{P}\star\tilde{Q})=2\mathrm{Sc}(\tilde{P}\star\tilde{Q})$ by the trace identity, and the scalar part of $\tilde{P}^{\natural}\tilde{Q}$ is $P_0Q_0+(\mathbf{P},\mathbf{Q})=\beta(\tilde{P},\tilde{Q})$. $\square$

**The square and the idempotents.** The square of the product is the scalar matrix of the determinant,

$$
\Phi(\tilde{Q}\star\tilde{Q})=\operatorname{adj}\Phi(\tilde{Q})\Phi(\tilde{Q})=\det\Phi(\tilde{Q})\,I=N(\tilde{Q})\,I ,
$$

so the idempotents of the quaternionic product are exactly $0$ and $e_0$, and the zero divisors of the product are exactly the singular matrices. No nontrivial projection of $M_2(\mathbb{C})$ survives as an idempotent: the Hermitian projections $\tfrac12\bigl(I+i\sum_k\hat\mu_k\Phi(e_k)\bigr)$ over the real unit vectors $\hat\mu=(\hat\mu_1,\hat\mu_2,\hat\mu_3)$ are idempotent for the ordinary matrix product and are not idempotent here, becoming square-zero instead, $\operatorname{adj}(B)B=0$.

**The units and the norm.** The product has a unit exactly when the determinant does not vanish: the units of the algebra are the matrices of $GL_2(\mathbb{C})$, the elements with $N(\tilde{Q})\neq0$, and the norm-one group is $SL_2(\mathbb{C})$.

**The symmetrisation and the left multiplications.** The central coefficient of the symmetrisation is half the trace of the transported product, $\beta(\tilde{P},\tilde{Q})=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde{P})\Phi(\tilde{Q})\bigr)$, and the symmetrised product itself is the scalar matrix $\beta(\tilde{P},\tilde{Q})I=\tfrac12\bigl(\operatorname{adj}(A)B+\operatorname{adj}(B)A\bigr)$, which is the matrix form of the centrality of the symmetrisation. The left multiplication by $\tilde{P}$ is the ordinary multiplication by the adjugate, $\Phi\bigl(L_{\tilde{P}}(\tilde{X})\bigr)=\operatorname{adj}\Phi(\tilde{P})\,\Phi(\tilde{X})$, so the composition law $L_{\tilde{P}}\circ L_{\tilde{R}}=L_{\tilde{R}\tilde{P}}$ is the anti-automorphism property $\operatorname{adj}(A)\operatorname{adj}(C)=\operatorname{adj}(CA)$, and the monoid of left multiplications is the opposite of the multiplicative monoid of the matrices.

**The associator.** The associator of the transported product $A\star'B=\operatorname{adj}(A)B$ is

$$
(A\star'B)\star'C-A\star'(B\star'C)=\operatorname{adj}(B)AC-\operatorname{adj}(BA)C=\bigl(\operatorname{adj}(B)A-\operatorname{adj}(BA)\bigr)C ,
$$

the failure of the transpose-conjugation to be multiplicative in the same order: the adjugate sends $BA$ to $\operatorname{adj}(A)\operatorname{adj}(B)$, whereas the first term carries the transposed $B$ past $A$ without reversing. This is the matrix form of the closed form $[\tilde{P},\tilde{Q},\tilde{R}]=(\tilde{Q}^{\natural}\tilde{P}-\tilde{P}^{\natural}\tilde{Q}^{\natural})\tilde{R}$ of the group, and the non-associativity of the product is the elementary fact that a transpose does not commute with a product.

## The General Quaternionic Bilinear Form in the Model

**Theorem (the adjugated trace pairing).** For all biquaternions,

$$
\langle\tilde{P},\tilde{Q}\rangle_{\natural} = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q})\bigr),
$$

the trace pairing in which the second argument is adjugated.

*Proof.* $\operatorname{adj}\Phi(\tilde{Q})=\Phi(\tilde{Q}^{\natural})$, so the right-hand side is $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\Phi(\tilde{Q}^{\natural}))=\mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural})=\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ by the trace identity $\mathrm{Sc}(\tilde{R}\tilde{S})=\tfrac12\operatorname{Tr}(\Phi(\tilde{R})\Phi(\tilde{S}))$.

**Theorem (the diagonal is the determinant).** On the diagonal,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tfrac12\operatorname{Tr}\bigl(\Phi(\tilde{Q})\operatorname{adj}\Phi(\tilde{Q})\bigr) = \det\Phi(\tilde{Q}) = \sum_\mu Q_\mu^2 ,
$$

so the form is the polarisation of the norm, and it is the determinant read as a quadratic form.

**The Gram matrix and the signature.** In the coefficient basis the Gram matrix of the form is the identity $I_4$; over $\mathbb{R}$ the form is the split form of signature $(4,4)$ on the eight real coordinates. It is indefinite and non-degenerate.

**The null set.** The form vanishes exactly on the singular matrices, $\det\Phi(\tilde{Q})=0$, that is on the zero divisors of the algebra; this is a real cone of real dimension $6$ in $\mathbb{R}^8$, the vanishing of one complex quadratic. It is the null set of the general quaternionic bilinear form alone and is strictly smaller than the real isotropic cone of the realified form, of real dimension $7$.

**The restriction to the Hermitian and anti-Hermitian matrices.** The determinant also reads the restriction of the form to the two four-dimensional subspaces of matrices. On the Hermitian matrices $\begin{pmatrix}a&z\\\bar z&b\end{pmatrix}$ with $a,b\in\mathbb{R}$ and $z\in\mathbb{C}$ the determinant is $ab-|z|^2$, a form of signature $(1,3)$ on the real four-space $\mathbb{M}_+$; on the anti-Hermitian matrices $\begin{pmatrix}ia&z\\-\bar z&ib\end{pmatrix}$ the determinant is $|z|^2-ab$, a form of signature $(3,1)$ on $\mathbb{M}_-$. Both are that table read on the matrices, whose general form is in *The Six Subspaces under the General Quaternionic Algebra of Biquaternions*.

**The automorphisms.** The form has Gram matrix $I_4$, so its automorphism group on the coefficient space is the complex orthogonal group $O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$; the real part of the form is the split real bilinear form of signature $(4,4)$, with automorphism group the split orthogonal group $O(4,4)$. The natural conjugation is an automorphism of the form, since the adjugate preserves the adjugated trace pairing.

**The congruence with the general plain bilinear form.** The natural conjugation reverses the pairing, $\langle\tilde P^{\natural},\tilde Q^{\natural}\rangle_{\natural}=\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P,\tilde Q\rangle$ read on $\tilde P^{\natural},\tilde Q^{\natural}$, so with $J=\operatorname{diag}(1,i,i,i)$ the coefficient matrices are congruent,
$$
J^{\mathsf T}\,D\,J=\mathrm{I}_4,\qquad D=\operatorname{diag}(1,-1,-1,-1),
$$
and the two forms share the automorphism group $O_4(\mathbb{C})$; the transport of the four pairings is the dictionary of *The Four Pairings of the Biquaternion Algebra*.

## Worked Examples

**A zero divisor.** Let $\tilde{Q}=e_0+ie_1$. Then $N(\tilde{Q})=1+i^2=0$, so $\tilde{Q}$ is a zero divisor and $\Phi(\tilde{Q})=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ is singular; the quaternionic square is $\tilde{Q}\star\tilde{Q}=N(\tilde{Q})e_0=0$.

**A basis element.** Let $\tilde{P}=e_1$. Then $\operatorname{adj}\Phi(e_1)=\Phi(e_1^{\natural})=-\Phi(e_1)$, and $\Phi(e_1\star\tilde{Q})=-\Phi(e_1)\Phi(\tilde{Q})$; the diagonal of the form is $\langle e_1,e_1\rangle_{\natural}=1$.

**A product read off the determinant.** Let $\tilde{P}=e_0+e_2$ and $\tilde{Q}=e_0-e_2$. Then $N(\tilde{P})=N(\tilde{Q})=2$ and $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=1-1=0$, so the two are isotropic to each other although both are units; the corresponding matrices have determinants $2$ and are isotropic for the adjugated trace pairing.

## Summary

The $2\times2$ realization turns the natural conjugation into the adjugate and the quaternionic product into the adjugated matrix product, $\Phi(\tilde{P}\star\tilde{Q})=\operatorname{adj}\Phi(\tilde{P})\Phi(\tilde{Q})$, with square the scalar matrix of the determinant, $\Phi(\tilde{Q}\star\tilde{Q})=N(\tilde{Q})I$. The adjugate reverses the order, $\operatorname{adj}(AB)=\operatorname{adj}(B)\operatorname{adj}(A)$, which is why the product is not associative: the associator is $\bigl(\operatorname{adj}(B)A-\operatorname{adj}(BA)\bigr)C$. The determinant of a value is the product of the norms, $\det\Phi(\tilde{P}\star\tilde{Q})=\langle\tilde{P},\tilde{P}\rangle_{\natural}\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, and its trace is twice the symmetrisation coefficient, $\operatorname{Tr}\Phi(\tilde{P}\star\tilde{Q})=2\beta(\tilde{P},\tilde{Q})$; the symmetrised product is the scalar matrix $\beta(\tilde{P},\tilde{Q})I$, and the left multiplications are the multiplications by the adjugates, forming the opposite monoid. The general quaternionic bilinear form of the group is the adjugated trace pairing $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))$, whose diagonal is the determinant, whose coefficient Gram matrix is the identity $I_4$, of real signature $(4,4)$, whose null set is the cone of singular matrices of real dimension $6$, and whose automorphism group is $O_4(\mathbb{C})$ on the coefficients and the split group $O(4,4)$ on the realification. The units are the matrices of non-zero determinant, the group $SL_2(\mathbb{C})$ is the norm-one slice, and the idempotents are $0$ and $e_0$ alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(\tilde{Q})$ | the $2\times2$ matrix of the realization, $\operatorname{Tr}\Phi(\tilde{Q})=2Q_0$, $\det\Phi(\tilde{Q})=N(\tilde{Q})$ |
| $\Phi(\tilde{Q}^{\natural})=\operatorname{adj}\Phi(\tilde{Q})$ | the natural conjugation is the adjugate |
| $\operatorname{adj}(AB)=\operatorname{adj}(B)\operatorname{adj}(A)$ | the adjugate reverses the order |
| $\Phi(\tilde{P}\star\tilde{Q})=\operatorname{adj}\Phi(\tilde{P})\Phi(\tilde{Q})$ | the quaternionic product is the adjugated matrix product |
| $\operatorname{Tr}\Phi(\tilde{P}\star\tilde{Q})=2\beta(\tilde{P},\tilde{Q})$, $\det\Phi(\tilde{P}\star\tilde{Q})=\langle\tilde{P},\tilde{P}\rangle_{\natural}\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ | the trace and the determinant of a value |
| $\tfrac12\operatorname{Tr}(\Phi(\tilde{P})\operatorname{adj}\Phi(\tilde{Q}))=\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the general quaternionic bilinear form |
| $I_4$, split of signature $(4,4)$ | the coefficient Gram matrix and the real signature |
| $\det\Phi(\tilde{Q})=0$ | the null set, the singular matrices, of real dimension $6$ |

## Further Reading

- Israel M. Gelfand, *Lectures on Linear Algebra* (Dover, 1989), for the trace, the determinant and the adjugate of a two-by-two matrix.
- Werner Greub, *Linear Algebra* (Springer, fourth edition, 1975), for the transpose as an anti-automorphism of an endomorphism algebra and its order reversal.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the identification of a full matrix algebra with its endomorphism algebra and for the structure of its units and its singular elements.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the two conjugations of an algebra, the transpose and the Hermitian transpose, and the distinction between them.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the description of a split algebra by matrices, with the reduced norm as the determinant and the reduced trace as the trace.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the reading of a twisted product as a product with an anti-automorphism inserted and the defect of its associativity.
- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realization and its first properties
- *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/biquaternion-2x2-matrix-element-representation-m2c.md`), for the further reading of the isomorphism
- *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the quaternionic product on the algebra
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form on the algebra
- *The General Quaternionic Algebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-quaternionic-algebra-in-the-4x4-matrix-representation.md`), for the companion reading of the group
- *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the restriction theory of the form
