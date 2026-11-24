# __Spinors and Dirac Spinors__

## Introduction

**The subject.** This article fixes the two words of its title at the row of the operators. A spinor is an element of a minimal left ideal of $\operatorname{End}(\mathbb{B})$, with four complex coordinates; a Dirac spinor is an element of the sum of a minimal left ideal and a minimal right ideal, with eight. The two chiralities are the two summands, and the chirality operator is the difference of their projections.

**The order of the article.** *The Spinor of the Row* fixes the spinor and its four coordinates; *The Dirac Spinor and Its Two Halves* builds the sum and proves it direct; *The Chirality Operator* defines the difference of the projections and computes its square; *The Action of the Copy* reads the two halves in the weight basis; *The Invariants* treats the forms and their pairing; *The Comparison with the Elements* counts the components.

**It assumes** *Introduction to the Spin-$\tfrac32$ Bispinor Spaces*, *Spinors and Dirac Spinors in the Biquaternion Algebra* and *The Symmetric and Antisymmetric Parts of the Operator Space*. **The row of the elements is** where the two counts are two and four.

**The result in one line.** A spinor of the operators has four coordinates $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, a Dirac spinor has eight, and the chirality operator is the difference of the two projections, with square the identity.

**Boundaries.** The classification of a spinor by its type is *The Fierz–Kofink Identities and the Classification of Spinors*; the ideals themselves are *The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals*; the two halves of the algebra at the row of the elements are *The Spin-Half Bispinor Spaces*.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$, with $e_t$ the identity and $\vec e_k^2=-e_t$; $S$ is the minimal left ideal $V_{1/2}$ of the algebra, of complex dimension two; the module of the operators is $V_{3/2}=\operatorname{Sym}^3 S$; $\star$ is the star; $\langle S,T\rangle=\operatorname{tr}(S^{\star}T)$ is the trace form of the operator space; and $\operatorname{tr}$ is the trace of an operator on the four-dimensional algebra.

## The Spinor of the Row

**Definition.** A **spinor** of the row is an element of a minimal left ideal $I_\ell$ of $\operatorname{End}(\mathbb{B})$, the ideal of the operators with image in a fixed complex line $\ell$ of the module $V_{3/2}$. A **weight basis** of $I_\ell$ is a basis of four elements carried by the copy with the weights of the module.

**Proposition.** A spinor has four complex coordinates, and in a weight basis they are $Ξ_{\mathrm{wfn},3/2},Ξ_{\mathrm{wfn},1/2},Ξ_{\mathrm{wfn},-1/2},Ξ_{\mathrm{wfn},-3/2}$, of weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$. The four functionals that read them are a basis of the dual of the ideal.

*Proof.* The ideal is a copy of the module, of complex dimension four, and the module has a weight string of four distinct entries. A functional of weight $\mu$ is non-zero on the line of weight $m$ only when $m+\mu=0$, so the four functionals are dual to the four weight lines.

**The reading.** A spinor is a single object of four coordinates, and the four are the weights taken once each.

## The Dirac Spinor and Its Two Halves

**Definition.** A **Dirac spinor** is an element of $I_\ell\oplus J_h$, where $I_\ell$ is a minimal left ideal and $J_h$ a minimal right ideal of the operator space.

**Proposition.** The sum $I_\ell+J_h$ is direct when the line $\ell$ and the hyperplane $h$ are paired so that $h$ is the annihilator of $\ell$; then a Dirac spinor has eight complex coordinates, four in each half.

*Proof.* The intersection $I_\ell\cap J_h$ is the set of operators with image in $\ell$ and kernel containing $h$, a single line. The sum has dimension $4+4-1=7$ when $\ell\subseteq h$; for $h=\ell^{\perp}$ the intersection is zero, since an operator with image $\ell$ vanishing on $\ell^{\perp}$ is a multiple of the projector onto $\ell$, and that projector does not vanish on $\ell$. Hence the sum is direct, of dimension eight.

**Corollary.** The Dirac spinor splits uniquely as a pair $(Ξ_{\mathrm{wfn}},\chi)$, and the splitting is the pair of projections onto the two summands.

*Proof.* A direct sum gives unique coordinates; the two projections keep one summand and annihilate the other.

**The reading.** The doubling here is not the passage from a complex dimension to a real one. It is the addition of the other side of the algebra, and the two sides are the two chiralities.

## The Chirality Operator

**Definition.** Let $P_L$ be the projection of $I_\ell\oplus J_h$ onto $I_\ell$ and $P_R$ the projection onto $J_h$. The **chirality operator** is

$$
\Gamma=P_L-P_R .
$$

**Proposition.** $\Gamma$ is a complex-linear involution, $\Gamma^2=\mathrm{id}$, its fixed space is the left ideal and its negated space the right ideal, and it commutes with the action of the copy.

*Proof.* The two projections are complementary idempotents, $P_L+P_R=\mathrm{id}$ and $P_LP_R=0$, so the square of the difference is the sum, which is the identity. The eigenspaces of an involution with eigenvalues $\pm1$ are the images of its two projections. Commutation with the copy: the copy preserves the type of an ideal, so it carries a left ideal to a left ideal, and both projections are equivariant.

**Corollary.** The eight coordinates split into four of $\Gamma=+1$ and four of $\Gamma=-1$; the chirality is the sign of the half.

*Proof.* The halves are the eigenspaces, each of complex dimension four.

**The reading.** $\Gamma$ is not a new datum: it is the difference of the two projections, and it exists because the ideals are distinguished by their side and not by their size.

## The Action of the Copy

**Proposition.** The copy acts on each half by the module action; in the weight basis its Cartan element is diagonal with the four weights in both halves, and the raising operator carries the coefficients $\sqrt3$, $2$, $\sqrt3$ in both.

$$
\varrho(H)=\operatorname{diag}\bigl(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32\bigr)\ \text{on}\ I_\ell,\qquad \varrho(H)=\operatorname{diag}\bigl(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32\bigr)\ \text{on}\ J_h .
$$

*Proof.* Each half is a copy of the module, of dimension four and irreducible for the copy, so the weights and coefficients are those of $V_{3/2}$. The halves differ by the side on which the operators multiply, and the copy acts by conjugation, which does not see the side.

**Corollary.** A Dirac spinor has a definite chirality on each weight component, and the eight coordinates are the four weights repeated twice with opposite chirality.

*Proof.* The chirality operator commutes with the copy, and the weight decomposition is the same in the two halves.

**The reading.** The diagonal shape says that the two halves are the same module. The conjugation of the algebra exchanges the sides, and it is the star, not the side, that reverses the weights.

## The Invariants

**Definition.** For a Dirac spinor $(Ξ_{\mathrm{wfn}},\chi)$ put

$$
q_L(Ξ_{\mathrm{wfn}})=\langleΞ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}}\rangle,\qquad q_R(\chi)=\langle\chi,\chi\rangle,\qquad \beta(Ξ_{\mathrm{wfn}},\chi)=\langleΞ_{\mathrm{wfn}},\chi\rangle,
$$

the restrictions of the trace form to the halves and the pairing between them.

**Proposition.** $q_L$ is positive definite on the left ideal and $q_R$ on the right ideal; $\beta$ is complex bilinear and non-degenerate for the annihilator pairing; and the three are the only invariants the trace form produces.

*Proof.* The trace form on the whole operator space is positive definite, so its restriction to a subspace is positive definite. The pairing is the same form read across the halves, and it is non-degenerate because the form is. Any other invariant is a combination of these three, by the invariance of the form under the copy.

**Corollary.** A Dirac spinor is null exactly when each half is null, and the pairing of a pure spinor with a pure conjugate spinor is the product of the two coordinate functionals.

*Proof.* The form on the sum is the sum of the two restrictions plus twice the pairing; the restrictions are positive definite, so vanishing forces both halves and the pairing to vanish. On pure elements the form is a product of one value from each side.

**The reading.** Two forms and a pairing is the whole invariant theory of the Dirac spinor, of the same shape as at the row of the elements; only the number of coordinates changes.

## The Comparison with the Elements

**Proposition.** At the row of the elements a spinor has two coordinates and a Dirac spinor four; at the row of the operators the numbers are four and eight. The count of a Dirac spinor at the operators is the count of a spinor at the elements multiplied by four, the complex dimension of the algebra.

*Proof.* The first pair is $\dim S=2$ and $2\dim S=4$; the second is $\dim\operatorname{Sym}^3S=4$ and twice that, $8$, and $8=2\cdot\dim_{\mathbb{C}}\mathbb{B}$.

**Corollary.** The two rows are related by the cubing of the module, and the doubling of the coordinates is the addition of the second side and not a change of the ground field.

*Proof.* The module of the operators is the cube of the module of the elements, and the second side doubles the count at both rows.

**The reading.** The number of components of a spinor is the dimension of the module and nothing else: it doubles because the module is cubed, and doubles again because the second side is added.

## Further Reading

- [Introduction to the Spin-$\tfrac32$ Bispinor Spaces](introduction-to-the-spin-three-halves-bispinor-spaces.html), for the module of the operators and its four weights
- [Spinors and Dirac Spinors in the Biquaternion Algebra](spinors-and-dirac-spinors-in-the-biquaternion-algebra.html), for the same three levels at the row of the elements
- [The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals](the-spin-three-halves-bispinors-and-the-minimal-left-ideals.html), for the family of ideals and its projective line
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the trace form and its two squares
- [The Fierz–Kofink Identities and the Classification of Spinors](the-fierz-kofink-identities-and-the-classification-of-spinors-of-the-operators.html), for the bilinears of a spinor and their relations
