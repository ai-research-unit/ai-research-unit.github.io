# __Spinors and Dirac Spinors in $M_4(\mathbb{C})$__

## Introduction

**The subject.** The article fixes the vocabulary. A spinor is a vector of the module of dimension four; a Weyl spinor is a vector of one of the two halves of dimension two; a Dirac spinor is a pair of Weyl spinors, that is a vector of the whole module. The article shows where each object lives in the algebra.

**The order of the article.** The first section defines the three kinds of spinor. The second locates them in the algebra. The third treats the pairing and the reality conditions. The fourth compares the dimension counts with the biquaternion row. The fifth draws the boundary.

**It assumes** *Introduction to the Spin-$\tfrac32$ Bispinor Spaces at $n=4$* and *The Quaternionic Structure of the Module: Why $V_{3/2}$ Admits Real Forms*. The row at order two is *Spinors and Dirac Spinors*.

**The result in one line.** A spinor is an element of $V_{3/2}=\mathbb{C}^{4}$, a Weyl spinor an element of one of the two halves $S_{\pm}$ of dimension two, and a Dirac spinor a pair of Weyl spinors, that is a spinor.

**Boundaries.** The article fixes terminology and localisation; the identities among bispinors are the subject of *The Fierz–Kofink Identities at $n=4$*.

## The Three Kinds

**Definition.** A **spinor** is a vector of $V_{3/2}=\mathbb{C}^{4}$; a **Weyl spinor** is a vector of one of the two halves $S_{+}$ or $S_{-}$ of dimension two; a **Dirac spinor** is a pair $(Ξ_{\mathrm{wfn},+},Ξ_{\mathrm{wfn},-})$ of Weyl spinors, that is a vector of $S_{+}\oplus S_{-}$.

**Proposition.** The three spaces have dimensions four, two and four, and the Dirac spinor is the same object as the spinor: $S_{+}\oplus S_{-}\cong V_{3/2}$.

*Proof.* The halves are two-dimensional and their sum is four-dimensional; the sum is the whole module.

**Corollary.** The label $\tfrac32$ belongs to the spinor and to the Dirac spinor, and the halves carry the pair $(\tfrac12,\tfrac12)$.

*Proof.* The halves are the pieces of the block reading; the whole module has the label $\tfrac32$.

**Corollary.** A Dirac spinor is a pair of Weyl spinors, and the decomposition into halves is not invariant under the principal copy but only under the block copy.

*Proof.* The halves are invariant under the block copy and not under the principal one, which mixes them.

**The reading.** The three words describe two spaces: the module of dimension four and its splitting into two halves of dimension two.

## Where They Live

**Proposition.** The spinors are the columns of the algebra: the minimal left ideal $M_4P_0$ consists of the matrices whose only nonzero column is the first, and it is isomorphic to $\mathbb{C}^{4}$.

*Proof.* Left multiplication by $P_0$ selects the first column; the map from the column to the matrix is an isomorphism onto the ideal.

**Corollary.** The dual spinors are the rows, and the minimal right ideal $P_0M_4$ consists of the matrices whose only nonzero row is the first.

*Proof.* The transpose of the left statement.

**Corollary.** A bispinor is a matrix, that is a spinor times a dual spinor summed over a basis, which is the content of the bispinor identification.

*Proof.* The rank-one matrices are $Ξ_{\mathrm{wfn}}\bar\chi^{\dagger}$ and they span the algebra.

**The reading.** The spinors are the columns, the dual spinors the rows, and the algebra is the space of bispinors: the three objects are the three ways of looking at a matrix.

## Pairing and Reality

**Proposition.** The module carries an invariant alternating form $\omega$, and the pairing of a spinor with a dual spinor is the evaluation; there is no invariant symmetric form.

*Proof.* The Frobenius–Schur indicator of $V_{3/2}$ is $-1$, so the invariant form is alternating and unique up to a scalar.

**Corollary.** The symmetry between a spinor and its dual is antisymmetric, so a spinor is never paired with itself to a nonzero scalar.

*Proof.* $\omega(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=0$ for an alternating form.

**Corollary.** The reality condition is quaternionic: there is an anti-linear $T$ with $T^{2}=-1$, and a Majorana spinor in the strict sense, which would need $T^{2}=+1$, does not exist.

*Proof.* $T\bar T=(-1)^{2j}=-1$ at $2j=3$; a real structure would need $T^{2}=+1$.

**The reading.** The half-integral label forces the alternating pairing and the quaternionic reality condition, exactly as it forces the absence of a real form of the module.

## The Comparison with Order Two

**Proposition.** At order two the module is $V_{1/2}$ of dimension two, the pairing is again alternating, and the quaternionic structure is the multiplication by $j$ on $\mathbb{H}$.

*Proof.* $2j=1$ is odd, so the indicator is $-1$; the module $V_{1/2}$ is $\mathbb{C}^{2}$ with the quaternionic structure of $\mathbb{H}$.

**Corollary.** At order two there are no Weyl halves: the module has dimension two and cannot split into two invariant lines.

*Proof.* A splitting into lines would need two invariant one-dimensional subspaces, and the module is irreducible.

**Corollary.** At order four the number of Weyl spinors is two and at order two there is one spinor; the count is the number of halves, which is two exactly when the module has even dimension greater than two.

*Proof.* The halves exist when the module can be split by the block copy, which needs a two-dimensional block structure.

**The reading.** The words "Weyl" and "Dirac" belong to the row of order four; at order two there is only the spinor, of dimension two.

## The Boundary

**Against the bispinor introduction.** That article treats the space of pairs; this one names the members of the pair.

**Against the quaternionic article.** That article computes the indicator; this one reads the reality condition from it.

**Against the Fierz article.** The classification of spinors by the rank of the associated bispinor is the next article.

## The Vocabulary in the Module

**The Dirac spinor.** An element of the module is a Dirac spinor of the algebra, and its four components are the coordinates in the standard basis; the copy acts on it through the three generators, and the weights are the four half-integers.

**The Weyl spinor.** Under the block copy the module splits into two two-component halves, and a Weyl spinor is a nonzero element of one half; the Cartan generator acts on the halves with the two signs, so a Weyl spinor is an eigenvector of the chirality up to a phase.

**The Majorana spinor.** A Majorana condition is a real structure on the module, and the module of half-integer label does not carry one; the quaternionic structure gives an anti-linear map whose square is minus one, so it defines a symplectic pairing rather than a real form.

**The reading.** The three words name three different objects: an element of the four-dimensional module, an element of a two-dimensional half, and a real element, which does not exist at this order.

## The Check of the Components

**The four components.** A Dirac spinor has four complex components, and the copy acts on them through the three generators; the components are the coordinates in the basis of weight vectors, and the weights are the four half-integers.

**The two halves.** Under the block copy the components split into two pairs, and each pair is a Weyl spinor; the split is the decomposition of the module under the subgroup, and it is not invariant under the whole copy.

**The reality.** The module has no real structure, so no Majorana condition can be imposed; the quaternionic structure pairs the module with its conjugate, and the pairing is antilinear with square minus one.

## Summary

A spinor is a vector of the module of dimension four, a Weyl spinor a vector of one of its two halves of dimension two, and a Dirac spinor a pair of Weyl spinors. The Dirac spinor and the spinor are the same object; the halves are invariant under the block copy and not under the principal one.

The spinors are the columns of the algebra and the dual spinors its rows; the bispinors are the matrices. The invariant pairing is alternating, and the reality condition is quaternionic, so a strict Majorana spinor does not exist at order four.

At order two there is one spinor of dimension two and no halves.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_{3/2}=\mathbb{C}^{4}$ | the spinors and the Dirac spinors |
| $S_{\pm}$ | the Weyl halves, dimension two |
| $(\tfrac12,\tfrac12)$ | the labels of the halves |
| $\omega$ | the invariant alternating form |

## Further Reading

- [Introduction to the Spin-$\tfrac32$ Bispinor Spaces at $n=4$](introduction-to-the-spin-three-halves-bispinor-spaces-at-n-4.html), for the bispinors.
- [The Quaternionic Structure of the Module: Why $V_{3/2}$ Admits Real Forms](the-quaternionic-structure-of-the-module-at-n-4.html), for the reality conditions.
- [The Fierz–Kofink Identities and the Classification of Spinors at $n=4$](the-fierz-kofink-identities-at-n-4.html), for the classification.
- [Spinors and Dirac Spinors](spinors-and-dirac-spinors.html), for the row at order two.
- [The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals](the-spin-three-halves-bispinors-and-the-minimal-left-ideals-at-n-4.html), for the ideals.
