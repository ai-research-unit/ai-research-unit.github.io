# __Introduction to the Spin-Two Carrier at $n=4$: the Alternating Square__

## Introduction

**The subject.** The carrier of label two is the alternating square of the module, of dimension five. The article identifies it, computes its weights and its Casimir, and explains its place in the parity rule.

**The order of the article.** The first section identifies the carrier as the alternating square. The second computes the weights and the weight string. The third computes the Casimir and the spectrum. The fourth reads the carrier as a space of forms and locates its Hermitian slice. The fifth draws the boundary.

**It assumes** *The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$* and *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$*. The row at order two is *Introduction to the Spin-One Carrier of the Biquaternion Algebra*.

**The result in one line.** $V_2=\Lambda^{2}V_{3/2}$, of complex dimension five, with weights $\pm2,\pm1,0$, Casimir six, and a determinant equal to the square of the trace form over sixteen.

**Boundaries.** The article introduces the carrier; its trace form, rank strata and spectral strata are treated in the following articles.

## The Alternating Square

**Proposition.** $V_2=\Lambda^{2}\mathbb{C}^{4}$, of complex dimension five, and it is the isotypic component of label two.

*Proof.* The alternating square of the module has dimension $\binom{4}{2}=6$ and decomposes as $V_2\oplus V_0$, of dimensions $5+1$; the label-two piece is the alternating square minus the invariant form, which is the line of scalars.

**Corollary.** The complement of $V_2$ in $\Lambda^{2}$ is the line of the invariant alternating form, that is $V_0$.

*Proof.* The parity rule.

**Corollary.** The carrier is the image of the map $u\wedge v\mapsto uv-vu$ up to the identification with the algebra.

*Proof.* The commutator of two rank-one matrices is alternating.

**The reading.** The quintet is the alternating square of the spinors, and the invariant form is the line removed from it.

## The Weights

**Proposition.** The weights of the carrier are $+2,+1,0,-1,-2$, and a weight basis is $E_{02},E_{01},E_{00}-E_{11},E_{10},E_{20}$ up to normalisation.

*Proof.* The alternating square of the weight string $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ gives the differences $m_i+m_j$ for $i<j$, that is $3,2,1,0,1,2$ with the pairs, and the label-two piece keeps $2,1,0$.

**Corollary.** The carrier is multiplicity-free: each of its five weights occurs once.

*Proof.* The weights displayed are distinct.

**Corollary.** The highest weight vector has weight two and the lowest weight two, so the string is symmetric.

*Proof.* The weight string.

**The reading.** The quintet has the weight string $2,1,0,-1,-2$, which is the string of the label two.

## The Casimir

**Proposition.** The Casimir acts on $V_2$ by the eigenvalue six, and the projector onto the carrier is the Lagrange polynomial of the Casimir vanishing on the other three eigenvalues.

*Proof.* The Casimir eigenvalue on $V_k$ is $k(k+1)$, which gives $6$ for $k=2$; the Lagrange polynomial $\prod_{l\neq6}(C-l)/(6-l)$ over $l\in\{0,2,12\}$ is the projector.

**Corollary.** The trace of the projector is five, and the projector is idempotent.

*Proof.* The rank of a projector is the dimension of its image.

**Corollary.** The carrier is the eigenspace of the Casimir with eigenvalue six, and it is invariant.

*Proof.* The Casimir commutes with the action.

**The reading.** The label is recovered from the Casimir eigenvalue by $k(k+1)=6$, which has the positive root $k=2$.

## The Space of Forms

**Proposition.** Under the identification of $\mathbb{C}^{4}$ with the space of binary cubics, the carrier $V_2$ is the space of alternating two-forms modulo the invariant one, of dimension five, and it is isomorphic to the space of traceless symmetric $3\times3$ matrices over the reals.

*Proof.* The alternating forms on a four-dimensional space form a six-dimensional space; the invariant form spans a line; the quotient is five-dimensional; the real form of the quintet is the traceless symmetric square of the three-dimensional representation.

**Corollary.** The carrier's Hermitian slice is five-real-dimensional, and a general Hermitian element has the spectrum $\pm a$ twice.

*Proof.* The numerical spectrum $2.817,2.817,-2.817,-2.817$ and the determinant formula which forces $\alpha=\beta$.

**Corollary.** The quintet is the carrier whose Hermitian elements are the closest to being reflections.

*Proof.* The spectrum $\pm a$ twice.

**The reading.** The quintet is a space of forms with a degenerate Hermitian spectrum, and its real form is the space of traceless symmetric tensors.

## The Boundary

**Against the parity article.** That article proves the splitting; this one studies the summand of label two.

**Against the trace form article.** The form on the quintet is computed there, with the Gram matrix in the weight basis.

**Against the biquaternion row.** At order two there is no carrier of label two: the algebra is four-real-dimensional and its carriers are labels one and zero.

## The Quintet in Coordinates

**The highest weight vector.** The projection of $E_{02}$ onto the carrier is $E_{02}+E_{13}$: the unit $E_{02}$ is not itself in the carrier, because the weight-two space of the algebra is two-dimensional, spanned by $E_{02}$ and $E_{13}$, and the carrier contributes one dimension to it. The element $E_{02}+E_{13}$ is nilpotent of rank two, since the two units have no product in either order.

**The weight-zero vector.** The projection of the traceless diagonal element $E_{00}-E_{11}$ is $\tfrac12\operatorname{diag}(1,-1,-1,1)$, of trace zero and rank four, with the spectrum $\{\tfrac12,\tfrac12,-\tfrac12,-\tfrac12\}$. It is an invertible element of a carrier whose extreme weight vectors are nilpotent, so the two kinds of element are not separated by the weight.

**The determinant.** Since the characteristic polynomial is $(\lambda^{2}-q/4)^{2}$, the determinant is $q^{2}/16$ and the trace of the square is $q$; the two invariants are not independent, and the carrier has a single spectral parameter. The numerical check gives $\det X-(q/2)^{2}=0$ to machine precision on random elements.

**The reading.** The quintet is generated by two kinds of element, the nilpotent weight vectors and the invertible weight-zero element, and the sign of the invariant quadratic form separates them.

## The Carrier and Its Dual

**The dual of the carrier.** The dual of the quintet is the carrier itself, because the trace form pairs the alternating square with itself and is nondegenerate; the pairing is alternating, since the trace form on two alternating tensors is symmetric in the exchange and the two-form description adds the sign.

**The alternating square at order two.** At order two the alternating square of the module is one-dimensional, spanned by the alternating form, and the carrier is the line of the multiples of that form; the whole construction degenerates to a single carrier, which is the reason the row at order two has only one nontrivial carrier.

## The Check of the Split

**The two squares.** The tensor square of the module splits into the symmetric and alternating parts of dimensions ten and six, and the quintet is the even part of the alternating piece; the check is $5+1=6$ and $7+3=10$, with the totals summing to sixteen.

## The Projective Carrier

**The quadric.** The carrier is five-dimensional and its projective space is four-dimensional; the isotropic cone of the trace form cuts the projective space in a quadric of dimension three, and the quadric carries the rank-two elements, one direction for each point.

## Summary

The carrier of label two is the alternating square of the module minus the invariant form, of complex dimension five, with weights $2,1,0,-1,-2$ and Casimir eigenvalue six. Its projector is a Lagrange polynomial in the Casimir, and its Hermitian slice has the spectrum $\pm a$ twice.

The carrier is the space of alternating forms modulo the invariant one, and its real form is the space of traceless symmetric three-by-three matrices.

**The place in the corpus.** The quintet is the carrier of the alternating square, and its single spectral parameter is the shadow of the fact that the alternating square at order two is one-dimensional; the comparison of the two orders is the clearest illustration of how much structure the doubling of the module adds.


**The reading.** The quintet is the middle carrier, between the triplet of the copy and the septet of the top, and its projective quadric is the smallest picture in which the three-parameter behaviour of the algebra begins.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_2=\Lambda^{2}V_{3/2}/V_0$ | the quintet |
| $2,1,0,-1,-2$ | its weights |
| $6$ | its Casimir eigenvalue |
| $\pm a$ twice | the Hermitian spectrum |

## Further Reading

- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module-at-n-4.html), for the splitting.
- [The Spin-Two Carrier and the Trace Form at $n=4$](the-spin-two-carrier-and-the-trace-form-at-n-4.html), for the form.
- [The Spin-Two Carrier and the Rank Strata at $n=4$](the-spin-two-carrier-and-the-rank-strata-at-n-4.html), for the ranks.
- [Introduction to the Spin-One Carrier of the Biquaternion Algebra](introduction-to-the-spin-one-carrier-of-the-biquaternion-algebra.html), for the row at order two.
- [The Spin Decomposition of $M_4(\mathbb{C})$](the-spin-decomposition-of-m4c.html), for the weights.
