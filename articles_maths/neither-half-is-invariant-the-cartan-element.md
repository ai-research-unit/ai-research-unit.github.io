# __Neither Half Is Invariant: the Cartan Element Carries $\operatorname{Sym}$ into $\Lambda$__

## Introduction

**The subject.** The two squares are the eigenspaces of the transposition, and the Cartan element of the copy acts on the operator space by left multiplication. The article shows that this action preserves neither square: it carries a symmetric operator to an operator with a nonzero alternating part, and it carries an alternating one back with a symmetric part. The mixing is computed explicitly on the identity, and its measure is the commutator of the action with the transposition.

**The order of the article.** The action and the two projections come first; the explicit image of a symmetric operator second. The mixing of the labels follows, and the reading closes the article.

**It assumes** *The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$*, *The Symmetric and Antisymmetric Parts of the Operator Space* and *The Four Weights of the Module and the Half Angle*. **The row of the elements is** where the Cartan element acts on a space with no such split; here the split exists and the action crosses it.

**The result in one line.** Left multiplication by the Hermitian Cartan element sends the identity to an operator whose symmetric and alternating parts are both nonzero, so neither square is invariant, and the obstruction is measured by the failure of the element to be fixed by the transposition.

**Boundaries.** The parity rule is *The Parity Rule*; the intersection table is *The Intersection Table: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$*; the two halves themselves are *The Symmetric and Antisymmetric Parts of the Operator Space*.

## The Action and the Projections

**Definition.** Let $H=i\,L_{i\vec e_z}$ be the Hermitian Cartan element, acting on the operator space by left multiplication, $S\mapsto HS$, and let $\pi_+=\tfrac12(\mathrm I+\tau)$ and $\pi_-=\tfrac12(\mathrm I-\tau)$ be the projections onto the two squares.

**Proposition.** The projections are self-adjoint idempotents with sum the identity, and the transposition satisfies $\tau(AB)=\tau(B)\tau(A)$.

*Proof.* The transposition is an involution, so the two maps are the spectral projections; the reversal of the product is the anti-automorphism property.

**Corollary.** The action of $H$ preserves a square exactly when $\tau(HS)=\pm HS$ for every $S$ of that square, that is exactly when $\tau(H)=H$.

*Proof.* $\tau(HS)=\tau(S)\tau(H)$; for $S$ in the $+$ square and $\tau(H)=H$ the product is $SH$, which is not $HS$ in general, so the condition is necessary and the failure is the commutator.

**Corollary.** The mixing is measured by the commutator $[H,\tau]$ of the action with the transposition.

*Proof.* The defect of invariance is $\tau(HS)-H\tau(S)=\tau(S)\tau(H)-H\tau(S)$, which vanishes for all $S$ exactly when $\tau(H)$ commutes with every $S$.

**The reading.** The action of the Cartan element does not commute with the transposition, and the failure is concentrated in the alternating part of $H$ itself. The squares are the eigenspaces of $\tau$, and an action that does not commute with $\tau$ cannot preserve them.

## The Image of the Identity

**Theorem.** The identity is symmetric and its image under the Cartan element is $H$, whose symmetric and alternating parts are
$$
\pi_+H=\tfrac{i}{2}\left(T_{i\vec e_z,e_t}+T_{e_t,i\vec e_z}\right),\qquad
\pi_-H=\tfrac{i}{2}\left(T_{i\vec e_z,e_t}-T_{e_t,i\vec e_z}\right),
$$
both nonzero.

*Proof.* The identity is the product $T_{e_t,e_t}$, fixed by the transposition; the image is $H=iT_{i\vec e_z,e_t}$, and the transposition carries it to $iT_{e_t,i\vec e_z}$; the two projections follow.

**Corollary.** A symmetric operator is carried to an operator with a nonzero alternating part, and the two parts have the same dimension.

*Proof.* The computation, and the ranks of the two products of units.

**Corollary.** An alternating operator is carried to an operator with a nonzero symmetric part, by the same computation applied to a difference of products.

*Proof.* Apply the action to $T_{a,b}-T_{b,a}$ and project.

**The reading.** One example suffices to destroy both invariances, and the example is the simplest operator of the space. The Cartan element carries $\operatorname{Sym}$ into $\Lambda$ and back, and it does so on the identity itself.

## The Mixing of the Labels

**Proposition.** The alternating part of the image of a symmetric operator of weight $w$ has weight $w+1$ or $w-1$, so the mixing moves the label by one unit.

*Proof.* The Cartan element carries the weight $w$ to the weight $w+1$ of the same vector under the generator, and the alternating projection does not change the weight.

**Corollary.** The mixing pairs the two squares carrier by carrier, the odd carriers receiving from the even ones and conversely.

*Proof.* The shift of one unit exchanges the parity of the label.

**Corollary.** Two applications of the Cartan element return to the same square, since the shift by one is applied twice.

*Proof.* The weight shift is additive, and two shifts of one unit restore the parity.

**The reading.** The mixing is not wild: it moves by one step in the weight and exchanges the parity. This is why the two squares are exchanged rather than destroyed, and why the carriers are not contained in either square.

## The Size of the Mixing

**Proposition.** The alternating part of the image of a symmetric operator is never larger than the operator itself, and on the identity it is exactly half of it in the basis of products.

*Proof.* The two projections are the coordinates of the operator in the direct sum of the squares, and they satisfy $\|\pi_+S\|^{2}+\|\pi_-S\|^{2}=\|S\|^{2}$ for the trace form; on the identity the image is the Cartan element, whose two parts have equal norm.

**Corollary.** The mixing is an isometry in the sense that it preserves the total norm while moving half of it to the other square.

*Proof.* The identity displayed, applied to the image.

**Corollary.** Iterating the action produces a bounded drift between the squares, and the drift is periodic with period two in parity.

*Proof.* Each application shifts the weight by one unit and exchanges the squares; the weight is bounded by three, so the drift returns.

**The reading.** The mixing has a size, and the size is measured by the two projections. It is not an all-or-nothing phenomenon: the action moves a definite part of each operator into the other square, and the part is computable from the projections.

## The Reading

**Consequence for the carriers.** No carrier of the operator space is contained in one square alone, since the Cartan element carries a nonzero vector of the carrier into the other square. A carrier is stable under the copy and not under the transposition, and the two structures cross.

**Consequence for the projections.** The projections onto the squares do not commute with the copy, so a spectral statement about a carrier and a symmetry statement about a square cannot be combined without a correction term, and the correction is the commutator computed above.

**The three objects.** The transposition gives the split into ten and six; the copy gives the split into seven, five, three and one; and the Cartan element is the operator that shows the two splits are different. The algebra of the operators carries both structures, and neither is a refinement of the other.

## Further Reading

- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module.html), for the split of the carriers between the squares.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the two halves.
- [The Four Weights of the Module and the Half Angle](the-four-weights-of-the-module-and-the-half-angle.html), for the weight shift.
- [The Intersection Table: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$](the-intersection-table-of-the-carriers-with-the-two-halves.html), for the table of the intersections.
