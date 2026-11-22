# __The Spin-Three Carrier and the Hermitian Form__

## Introduction

**The subject.** The Hermitian form of the algebra, restricted to the septet, is a complex bilinear form that takes real values on the real form and has signature $(4,3)$ there. The article computes it in the weight basis, proves its invariance and its nondegeneracy, identifies the maximal subspaces on which it is definite, and shows that the signature is the invariant of the carrier that survives every choice of copy and of real structure.

**The order of the article.** The form and its restriction come first, then the weight basis and the array of the form. The signature is computed next, the phase of the real structure is settled, the definite subspaces are identified, and the comparison with the triplet closes the article.

**It assumes** *Introduction to the Spin-Three Carrier: the Top of the Chain* and *The Spin-Two Carrier and the Trace Form*. **The row of the elements is** where the form of the algebra is read on a four-dimensional space; on the real vector part there it is definite.

**The result in one line.** On the seven real dimensions of the carrier the Hermitian form is real, nondegenerate and of signature $(4,3)$, with maximal definite subspaces of dimensions four and three, and the opposite real structure makes it vanish identically.

**Boundaries.** The carrier and its weights are *Introduction to the Spin-Three Carrier: the Top of the Chain*; the ranks and the spectra inside it are the two following articles; the form of the algebra on the whole sixteen is *The Symmetric and Antisymmetric Parts of the Operator Space*.

## The Form of the Algebra

**Definition.** The **Hermitian form of the algebra** is
$$
\mathrm H(X,Y)=\operatorname{tr}(X^{\natural}Y),
$$
where $\natural$ is the quaternion conjugation. On the operator space the same formula is read with the star of the operator space, the exchange of the two sides $\natural(T_{a,b})=T_{b,a}$, and the carrier lies in the symmetric square, where the exchange acts as the identity, so that on $V_3$
$$
\mathrm H(S,T)=\operatorname{tr}(ST).
$$

**Proposition.** The form $\mathrm H$ is complex bilinear, symmetric and nondegenerate on the carrier, and it is invariant under the copy.

*Proof.* Bilinearity and symmetry are those of the trace of a product. Invariance is the computation
$$
\operatorname{tr}([\xi,S]T)+\operatorname{tr}(S[\xi,T])=\operatorname{tr}(\xi ST)-\operatorname{tr}(ST\xi)=0
$$
for a generator $\xi$ of the copy. Nondegeneracy follows because a nonzero element of the carrier has a nonzero coefficient on some basis product and the pairing with the dual basis element is not zero.

**Corollary.** The restriction of $\mathrm H$ to the carrier is the unique invariant symmetric bilinear form on it, up to a scalar.

*Proof.* The carrier is irreducible, so the space of invariant bilinear forms is at most one-dimensional by the lemma of Schur; the form is not zero, so it is exactly one-dimensional.

**The reading.** The form is the operator version of the Hermitian form of the algebra. The phrase Hermitian refers to its origin, in the conjugation of the algebra, and not to conjugate symmetry: the form is complex bilinear, and its conjugate symmetry appears only when it is read on the real form.

## The Weight Basis

**Proposition.** In the weight basis $v_3,v_2,v_1,v_0,v_{-1},v_{-2},v_{-3}$ the form is antidiagonal, and its entries are the signs of the weights:
$$
\mathrm H(v_m,v_n)=0\ \text{unless}\ n=-m,\qquad
\mathrm H(v_m,v_{-m})=(-1)^{m}.
$$

*Proof.* Invariance forces the form to pair only weights summing to zero, and invariance under the copy fixes the remaining entries up to one scalar; the scalar is computed at the pair $(0,0)$, where the value is one, and the ladder relations then propagate it with alternating signs, because each step through the string changes the weight by one and the coefficient by a square root taken with a fixed sign.

**Corollary.** Every weight vector of nonzero weight is isotropic for the form, and the weight-zero vector is not.

*Proof.* The pairing of $v_m$ with itself vanishes unless $2m=0$.

**Corollary.** The array of the form in the weight basis is the reversal of the identity array, with the signs $+,-,+,-,+,-,+$ along the antidiagonal from the weight three to the weight minus three.

*Proof.* The displayed entries, read in the order of the weights.

**The reading.** The form is as far from the identity as a nondegenerate form can be in this basis: it pairs the two ends of the string, then the second from each end, and so on, and it vanishes on every weight vector itself except the middle one.

## The Signature

**Theorem.** On the real form of the carrier the form is real, symmetric and of signature $(4,3)$.

*Proof.* The real form is the fixed space of the invariant antilinear involution $J_3$, which sends $v_m$ to a multiple of $v_{-m}$ and fixes the weight-zero direction up to a scalar. It is therefore spanned by the weight-zero vector and by two real combinations in each of the three pairs $\pm3,\pm2,\pm1$. On a pair the form has zero diagonal and the entry $(-1)^{m}$ between the two directions, so the pair contributes one positive and one negative direction whatever the sign. The three pairs contribute three of each, and the weight-zero line contributes one positive. The total is four positive and three negative.

**Corollary.** The maximal subspaces on which the form is definite have real dimensions four and three, and the form is indefinite.

*Proof.* The count of the theorem gives a positive subspace of dimension four and a negative one of dimension three; indefiniteness follows from the existence of an isotropic vector, which is any weight vector of nonzero weight.

**Corollary.** No subspace of real dimension five is definite.

*Proof.* A definite subspace of dimension five would force the signature to have a part of size at least five on one side, and the two sides are four and three.

**The reading.** The signature is read from the string without a computation: each pair of opposite weights contributes one direction of each sign, and the single unpaired weight contributes one positive direction. The septet has three pairs and one unpaired weight, which is why its signature is $(4,3)$.

## The Phase of the Real Structure

**Proposition.** The invariant antilinear involution of the carrier is unique up to sign. The other involution in the same complex line, $iJ_3$, has a fixed space of seven real dimensions, and on that space the form is purely imaginary, equal to $2i$ times its values on the first real form.

*Proof.* The space of invariant antilinear maps is one complex dimensional, and a map $J$ with $J^{2}=1$ stays a real structure when multiplied by a phase of modulus one. A vector fixed by $iJ_3$ has the shape $X=(1+i)Y$ with $Y$ fixed by $J_3$, since $J_3X=J_3Y+iJ_3Y=Y-iY=(1-i)Y$ and $iJ_3X=i(1-i)Y=(1+i)Y$. The square of the factor is $(1+i)^{2}=2i$, so the form on the second real form is $2i$ times the form on the first: it is purely imaginary and takes a real value only at zero.

**Corollary.** The real structure carrying a real-valued form is unique up to sign, so the signature $(4,3)$ is intrinsic.

*Proof.* Of the two real structures in the line exactly one makes the form real-valued, and the other makes it purely imaginary. Changing the sign of the involution does not change its fixed space.

**The reading.** The phase of the real structure is not free. The carrier has one real form on which the form is real and one on which it is purely imaginary, and the signature belongs to the first, which is determined up to sign. The form is attached to the space and not to the copy, so the same signature is read in both readings of the row.

## The Comparison with the Triplet

**Proposition.** The index of the form increases with the label: the operator-row triplet has signature $(2,1)$, the quintet $(3,2)$ and the septet $(4,3)$.

*Proof.* A carrier of label $k$ has $k$ pairs of opposite weights and one unpaired weight zero, so each pair contributes one positive and one negative direction and the zero contributes one positive: the signature is $(k+1,k)$. At $k=1,2,3$ this gives the three signatures displayed.

**Corollary.** The largest carrier is the one on which the form is least definite, its index being three.

*Proof.* The index is the smaller of the two entries, which is $k$; it increases with $k$ and is largest at the top of the chain.

**Corollary.** On the carrier of label one in the row of the elements the form is definite.

*Proof.* There the carrier is the real span of the three pure units, and for two such vectors $\operatorname{tr}(X^{\natural}Y)=4\langle x,y\rangle$, which is positive definite.

**The reading.** Definiteness survives only in the row of the elements. Every carrier of the operator row is indefinite, and the top carrier is the most indefinite of the three, with the largest possible index that a carrier of the row admits.

## Further Reading

- [Introduction to the Spin-Three Carrier: the Top of the Chain](introduction-to-the-spin-three-carrier-the-top-of-the-chain.html), for the carrier and its weight string.
- [The Spin-Three Carrier and the Rank Strata](the-spin-three-carrier-and-the-rank-strata.html), for the isotropic elements.
- [The Spin-Two Carrier and the Trace Form](the-spin-two-carrier-and-the-trace-form.html), for the form on the quintet.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the two squares and the exchange.
- [The Hermitian Pair of Operators Acting on Two Sides](the-hermitian-pair-of-operators-acting-on-two-sides.html), for the adjoint of a two-sided operator.
