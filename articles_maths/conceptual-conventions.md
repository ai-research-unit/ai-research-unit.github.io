# __Conceptual Conventions__

## Introduction

**The rule.** A concept is used in this corpus only when two conditions hold together. It must be consistent with mathematics. And no result of experiment may contradict it. A concept that fails either condition is left out, however familiar it is.

**Why an experiment appears in a mathematics article.** No article in this series draws a physical conclusion, so nothing written here can contradict a measurement. The condition still has work to do. An article here may not support a convention by an appeal to what an electron does. That argument belongs to the physics corpus, and a convention here has to stand on the algebra alone.

**Two ways of using a concept that passes.** A concept that passes both conditions is used in one of two ways. It is **preferred** when the algebra already contains it, so that nothing has to be added and nothing has to be declared. It is **unpreferred** when it is a working tool that brings something the algebra does not contain: a chosen frame, a basis, a root, or a piece of the algebra printed as though it were the whole. An unpreferred concept is not wrong. It is used only when the article says what it brings.

**The two lists.** The next two sections give the lists, the one the corpus avoids first and the one it writes by default second. The first list holds the concepts the corpus writes only under a declaration, with the defect named. The second holds the concepts it writes with no comment at all. The order is the order of the work: the reader meets the problem before the solution. The summary states the result in a few lines.

## Unpreferred Concepts

Each concept below is used somewhere in the corpus, and each one brings something the algebra does not contain. The list names the defect. An unpreferred concept is admitted as a display when the article that prints it declares the missing piece once, at the head of the display.

- **The Pauli matrices $\sigma_k$.** Three matrices, correct and useful. *The defect:* the array fixes an axis that the sentence does not name, and it fixes a Peirce frame with it.
- **The gamma matrices $\gamma_\mu$.** *The defect:* the five cells belong to a frame that is not named, and they carry a dimension and a signature that the algebra does not fix.
- **A Clifford algebra as a foundation.** *The defect:* it starts from a quadratic form, so the signature is fixed before the algebra is read. The biquaternion algebra starts from a central $i$, and the identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ exists.

**The kinds of defect.** A defect is one of three kinds, and each kind has a test that can be run on a sentence.

The first is a **missing datum**. The sentence uses an axis, a dimension, a signature, a root or a basis without naming it. The test is covariance. Rotate the algebra, read the sentence again, and compare. If it comes back unchanged it is a fact about the algebra. If it comes back changed it is a fact about the page, and a fact about the page has to say which page.

The second is **a part printed as the whole**. A half, an ideal, a column or a sector is written as though it were the algebra. The test is a count. Name the other piece and ask where it went. If it was dropped, the sentence describes a part and claims a whole.

The third is **two kinds under one name**: an operator and an element, an involution and a projector, a form and a metric. The test is a question about the subject. What kind of object is the subject, and can a predicate of that kind be true of it? An involution squares to the identity and a projector squares to itself.

A concept that passes all three tests is a preferred concept, and the short list of them is the one the algebra supplies by itself. The list above is what remains when something has to be supplied from outside.

## Preferred Concepts

These concepts are the algebra itself, written down. Each one can be read from an element, a cell or a form, and none of them needs a frame, a root, a basis or a name borrowed from another formalism. The corpus writes them without comment.

- **The two sectors.** The anti-Hermitian subspace $\mathbb{M}_-$ carries the four-vectors and the interval. The Hermitian subspace $\mathbb{M}_+$ carries the observables, the states and the spin generators. The algebra supplies the subspaces and the forms on them, and the identification of a subspace with a physical role is the programme's step, stated at every use.
- **Operator chirality.** An operator has the **left slot** when it is a pure left multiplier $cL_a$, the **right slot** when it is a pure right multiplier $cR_b$, and **both slots** otherwise. The label is read from the cell and from nothing else. The one-sided operators form a seven-dimensional sum inside the sixteen-dimensional endomorphism algebra, and the scalars lie in both families at once, so a scalar has no side. No root, idempotent, ideal, axis or Clifford algebra appears in the definition.
- **The spin.** The generators are $\tilde S_k=\tfrac12 i\vec e_k\in\mathbb{M}_+$, with $[\tilde S_i,\tilde S_j]=i\epsilon_{ijk}\tilde S_k$ and $\tilde S_k^{*}=\tilde S_k$. The Casimir is $C=\tilde S_1^2+\tilde S_2^2+\tilde S_3^2$, and on an irreducible unitary carrier $\rho(C)=s(s+1)$ with $\dim_{\mathbb{C}}W=2s+1$ and $s\in\tfrac12\mathbb{Z}_{\ge0}$. The spin is a real label of a carrier and not a vector, and the definition is a spectrum of elements.

## Summary

A concept is used in this corpus only when it agrees with mathematics and no result of experiment contradicts it. In a mathematics article the second condition is met by restraint, because nothing here draws a physical conclusion.

The concepts that pass are used in one of two ways. Unpreferred concepts are working tools that bring a frame, a basis, a root or a part of the algebra: the Pauli matrices, the gamma matrices and the Clifford algebra. Each is admitted only with the missing piece declared. Preferred concepts are the algebra itself, and there are three: the two sectors, operator chirality and the spin.

Every defect is one of three: a missing datum, a part printed as the whole, or two kinds under one name. Operator chirality passes all three, which is why it is written as a slot and not as a root, an idempotent, a projector, a Clifford product or a gamma subscript.

## Further Reading

- [Algebra and Element Conventions](algebra-and-element-conventions.html). The base, the case rule, the remarkable subspaces and the two levels of the word *metric*.
- [Product and Form Conventions](product-and-form-conventions.html). The twelve products and the four forms, which are the four choices of conjugation on the two slots.
- [Norm and Unitary Conventions](norm-and-unitary-conventions.html). The four norms by letter, the qualified regular and degenerate, and the topological norm.
- [Special Element and Peirce Conventions](special-element-and-peirce-conventions.html). The root, the idempotent, the family, and the spin and spinor conventions with their declared axis.
- [Frame Conventions](frame-conventions.html). The two frames, the Clifford map and the rule that a frame is declared before it is used.
- [Matrix Representations Conventions](matrix-representations-conventions.html). The three displays, the Pauli form, the Clifford structure and the legacy gamma block.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html). The operator that is its element, the dagger and the Fock exception.
- [Operator Family Conventions](operator-family-conventions.html). The four families and the slot label that is the chirality.
- [Index, Notation and Corpus Conventions](index-notation-and-corpus-conventions.html). The marks, the subscripts and the working conventions of the corpus.
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html). The two slots, the chirality operator of a frame, the subscript on an element, and the eight objects the notion does not need.
- [Angular Momentum and Spin in the Biquaternion Algebra](angular-momentum-and-spin-in-the-biquaternion-algebra.html). The generators, the Casimir, the definition of spin, and the carriers that carry it.
- [Introduction to the Mathematical Corpus](introduction-to-the-mathematical-corpus.html). The exclusion of the applications, which is the restraint the second condition asks for.
