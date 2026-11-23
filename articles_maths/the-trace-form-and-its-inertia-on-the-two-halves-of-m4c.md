# __The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$__

## Introduction

**The pairing $\beta(A,B)=\operatorname{tr}(AB)$ is symmetric, non-degenerate and indefinite, and on the real algebra it has inertia $(10,6)$: positive definite on the ten-dimensional symmetric half, negative definite on the six-dimensional antisymmetric half, with the two halves orthogonal; the axis-free basis diagonalises it with entries $\pm4$, the ten plus signs on exactly the symmetric elements and the six minus signs on exactly the antisymmetric ones.**

The article proves the three properties, computes the signs on each half, exhibits the axis-free diagonalisation, contrasts it with the matrix-unit basis where the same inertia is present but hidden inside six hyperbolic planes, and draws the consequence that the symmetric decomposition of the algebra and the inertia of the form are one split read twice.

It assumes *The Two Halves as Orthogonal Complements at $n=4$* for the orthogonality and *The Axis-Free Representation of $M_4(\mathbb{C})$* for the basis $T_{\mu\nu}$. The case $n=2$ is *The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$*; the positive definite companion is *The Hilbert–Schmidt Form at $n=4$*.

## The Form and Its Non-Degeneracy

**Definition.** $\beta(A,B)=\operatorname{tr}(AB)$ for $A,B\in M_4(\mathbb{C})$, and the same formula on the real algebra.

**Proposition.** $\beta$ is symmetric and bilinear, and it is invariant under conjugation: $\beta(PAP^{-1},PBP^{-1})=\beta(A,B)$ for every invertible $P$.

**Proof.** $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ gives symmetry, and $\operatorname{tr}(PAP^{-1}PBP^{-1})=\operatorname{tr}(PABP^{-1})=\operatorname{tr}(AB)$.

**Proposition.** $\beta$ is non-degenerate.

**Proof.** If $\beta(A,B)=0$ for every $B$, take $B=E_{ji}$: then $\operatorname{tr}(AE_{ji})=A_{ij}=0$ for all $i,j$, so $A=0$.

**Proposition.** $\beta$ is indefinite: $\beta(\mathrm I_4,\mathrm I_4)=4>0$ and $\beta(E_{12}-E_{21},E_{12}-E_{21})=-2<0$.

**Proof.** $\operatorname{tr}(\mathrm I_4)=4$ and $(E_{12}-E_{21})^{2}=-E_{11}-E_{22}$, of trace $-2$.

**Corollary.** The form is not an inner product on the real algebra, and no scalar multiple of it is positive definite.

**Proof.** The two values above have opposite signs, and rescaling cannot make them agree in sign.

**The adjoint involution.** $\beta(A^{\mathsf T},B)=\beta(A,B^{\mathsf T})$, so the transpose is the adjoint of the form: $\beta(A^{\mathsf T},B)=\operatorname{tr}(A^{\mathsf T}B)=\operatorname{tr}(A B^{\mathsf T})=\beta(A,B^{\mathsf T})$.

**Proof.** $\operatorname{tr}(A^{\mathsf T}B)=\sum_{ij}A_{ij}B_{ij}=\operatorname{tr}(AB^{\mathsf T})$.

**Corollary.** The isometry group of $\beta$ contains $\mathrm{GL}_4$ acting by conjugation, and its Lie algebra of anti-self-adjoint endomorphisms contains every inner derivation.

**Proof.** The invariance under all of $\mathrm{GL}_4$ was proved above; differentiating gives the statement about derivations, which is the content of *The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form*.

## The Two Halves and Their Signs

**Theorem.** On the real symmetric half, $\beta(S,S)=\operatorname{tr}(S^{2})=\sum_{i,j}s_{ij}^{2}>0$ for $S\neq0$; on the real antisymmetric half, $\beta(K,K)=\operatorname{tr}(K^{2})=-2\sum_{i<j}k_{ij}^{2}<0$ for $K\neq0$.

**Proof.** The diagonal entry $(S^{2})_{ii}=\sum_j s_{ij}s_{ji}=\sum_j s_{ij}^{2}$ since $S$ is symmetric, and summing over $i$ counts every entry once. For antisymmetric $K$, $(K^{2})_{ii}=-\sum_j k_{ij}^{2}$ and summing gives $-2\sum_{i<j}k_{ij}^{2}$.

**Corollary.** $\beta$ is positive definite on $\operatorname{Sym}_4(\mathbb{R})$, of dimension $10$, and negative definite on $\operatorname{Skew}_4(\mathbb{R})$, of dimension $6$.

**Proof.** The two displays, with the dimensions $10$ and $6$.

**Corollary.** The two halves are orthogonal for $\beta$, so the restriction to each is the orthogonal direct sum, and the inertia on the whole real algebra is $(10,6)$.

**Proof.** $\beta(S,K)=\operatorname{tr}(SK)=0$ by the transpose argument, and $16=10+6$.

**The count.** $10=\tfrac{4\cdot5}{2}$ and $6=\tfrac{4\cdot3}{2}$: the plus signs are the number of symmetric positions and the minus signs the number of antisymmetric ones, counted as unordered pairs.

**Proof.** A symmetric matrix has $\binom{4}{2}$ off-diagonal pairs plus $4$ diagonal entries, $6+4=10$; an antisymmetric one has $\binom{4}{2}$ pairs and no diagonal, $6$.

**The complex reading.** On the complex algebra viewed as a real space of dimension $32$, the real part of $\beta$ has inertia $(16,16)$, since every complex direction contributes a positive and a negative real direction in pairs.

**Proof.** A complex line spanned by $A$ with $\beta(A,A)=c$ contributes the two real directions $A$ and $iA$ with values $c$ and $-c$.

## The Axis-Free Diagonalisation

**Definition.** $T_{\mu\nu}=L^{\mathrm{axf}}_{e_\mu}R^{\mathrm{axf}}_{e_\nu}$ for $\mu,\nu\in\{t,x,y,z\}$, the sixteen two-sided operators of the axis-free frame.

**Theorem.** $\operatorname{tr}(T_{\mu\nu}T_{\rho\sigma})=\pm4\,\delta_{\mu\rho}\delta_{\nu\sigma}$, with $+4$ on ten elements and $-4$ on six, and the same formula with the dagger in place of the second factor: $\operatorname{tr}(T_{\mu\nu}^{\dagger}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$, exact.

**Proof.** The sixteen matrices are signed permutations, so each has a square equal to $\pm\mathrm I_4$ and distinct elements pair to zero trace; the computation is a check of the sixteen signs, and the dagger version follows because the dagger of a signed permutation is its inverse, which pairs with it to the identity.

**Which ten and which six.** The plus set is

$$
T_{tt},\ T_{xx},\ T_{yy},\ T_{zz},\ T_{xy},\ T_{xz},\ T_{yx},\ T_{yz},\ T_{zx},\ T_{zy},
$$

and the minus set is $T_{tx},T_{ty},T_{tz},T_{xt},T_{yt},T_{zt}$. The plus set **is** the set of symmetric elements and the minus set **is** the set of antisymmetric ones; this is a set equality, not a count of equal sizes, and every element belongs to exactly one of the two.

**Proof.** An element $T_{\mu\nu}$ is symmetric exactly when it equals its transpose, and in the axis-free frame the transpose is the quaternion conjugation applied to both slots, which fixes the slot when the index is $t$ and negates it when the index is a vector index. So the element is symmetric exactly when the two indices are equal or both are vector indices, which is the plus set, and antisymmetric exactly when one index is $t$ and the other is a vector index, which is the minus set.

**Corollary.** The basis diagonalises $\beta$: the Gram matrix is diagonal with entries $\pm4$, ten plus and six minus, so the inertia is $(10,6)$ read at sight, and the two eigenspaces are the two halves.

**Proof.** The theorem gives the diagonal form, and the identification of the two sets with the two halves gives the eigenspaces.

**The coordinates.** $A=\sum_{\mu\nu}c_{\mu\nu}T_{\mu\nu}$ with $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}A)$, exact, and $\operatorname{tr}A=4c_{tt}$ because $T_{tt}=\mathrm I_4$ is the only basis element of nonzero trace.

**Proof.** The dual basis to $\{T_{\mu\nu}\}$ for the dagger pairing is $\{\tfrac14T_{\mu\nu}^{\dagger}\}$, and the trace statement is the computation of the trace of each element.

**Corollary.** $\beta(A,A)=4\sum_{\text{plus}}c_{\mu\nu}^{2}-4\sum_{\text{minus}}c_{\mu\nu}^{2}$, so the sign of the square length is the excess of the symmetric coordinates over the antisymmetric ones.

**Proof.** Expand $\operatorname{tr}(A^{2})$ in the diagonal basis.

## The Matrix-Unit Basis and the Hidden Inertia

**Proposition.** $\beta(E_{ij},E_{kl})=\delta_{jk}\delta_{il}$, so the Gram matrix in the matrix-unit basis is a permutation matrix with four fixed points and six transpositions.

**Proof.** $\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\operatorname{tr}(E_{il})=\delta_{jk}\delta_{il}$.

**Corollary.** The inertia is $(10,6)$ in this basis too, but it is not visible: the four fixed points contribute $+1$ each, and each of the six transpositions contributes a hyperbolic plane of inertia $(1,-1)$.

**Proof.** A fixed point gives the $1\times1$ block $[1]$; a transposition of $E_{ij}$ and $E_{ji}$ gives the block $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, whose eigenvalues are $\pm1$.

**What the two bases show.** In the axis-free basis the inertia is a diagonal of signs; in the matrix-unit basis it is a permutation, and reading it requires diagonalising six hyperbolic planes. The two bases are related by an invertible change of coordinates, which preserves the inertia and destroys or reveals its visibility.

**Proof.** Sylvester's law of inertia, and the two computations above.

**Why the visibility matters.** The axis-free basis answers the question "which elements are positive" by naming them: the ten symmetric ones. The matrix-unit basis answers it only after a change of coordinates, and the answer it gives is a mixture of unit matrices, not a recognisable subspace of the algebra.

**Proof.** The plus set is a set of basis elements in the axis-free basis and a set of combinations in the matrix-unit basis.

## The Form and the Two Splits

**Theorem.** The positive eigenspace of $\beta$ is $\operatorname{Sym}_4$ and the negative eigenspace is $\operatorname{Skew}_4$; hence the symmetric decomposition and the diagonalisation of the form are the same split.

**Proof.** Each half is definite of the stated sign and the two are orthogonal and span, so they are the maximal definite subspaces and the eigenspaces.

**Corollary.** The Cartan decomposition $\mathfrak{gl}_4=\mathfrak{so}(4)\oplus\operatorname{Sym}_4$ is an orthogonal decomposition for $\beta$, and the form is negative definite on $\mathfrak{so}(4)$ and positive definite on the traceless symmetric part.

**Proof.** The two summands are the two halves, up to the scalar line in the symmetric part; the scalar $\mathrm I_4$ is positive and is orthogonal to the traceless part.

**The restriction to the Borel.** On $\mathfrak{b}$ the form degenerates, with radical $\mathfrak{n}_+$ of dimension $6$ and rank $4$; the inertia is not defined there and the degenerate radical replaces the negative eigenspace.

**Proof.** The computation of *The Antisymmetric Part inside $UT_4$*: every strictly upper unit pairs to zero with the Borel.

## Summary

The trace pairing is symmetric, non-degenerate, indefinite, invariant under conjugation, and has the transpose as its adjoint. On the real algebra it is positive definite on the ten-dimensional symmetric half and negative definite on the six-dimensional antisymmetric half, the two halves are orthogonal, and the inertia is $(10,6)$, with $10=\binom{4}{2}+4$ and $6=\binom{4}{2}$.

In the axis-free basis the form is diagonal with entries $\pm4$: the ten plus signs on exactly the symmetric elements and the six minus signs on exactly the antisymmetric ones, a set equality verified element by element. The coordinates are $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}A)$ and the trace is $4c_{tt}$.

In the matrix-unit basis the Gram matrix is a permutation with four fixed points and six transpositions, and the inertia is present but hidden in six hyperbolic planes. The form and the symmetric decomposition are one split read twice: the positive and negative eigenspaces of $\beta$ are the two halves, and the Cartan decomposition of the algebra is the same statement in Lie-algebraic form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\beta(A,B)=\operatorname{tr}(AB)$ | the trace pairing |
| $(10,6)$ | its inertia on the real algebra |
| $T_{\mu\nu}$ | the axis-free basis, sixteen signed permutations |
| $\operatorname{tr}(T_{\mu\nu}T_{\rho\sigma})=\pm4\delta$ | the diagonalisation |
| $c_{\mu\nu}$ | the trace-read coordinates |
| $\mathfrak{so}(4)\oplus\operatorname{Sym}_4$ | the orthogonal Cartan decomposition |

## Further Reading

- Werner Greub, *Multilinear Algebra* (Springer, 1978), for symmetric bilinear forms, hyperbolic planes and Sylvester's law of inertia.
- [The Two Halves as Orthogonal Complements at $n=4$](the-two-halves-as-orthogonal-complements-at-n-4.html), for the orthogonality used here.
- [The Axis-Free Representation of $M_4(\mathbb{C})$](m4c-axis-free-representation.html), for the basis and the transpose.
- [The Hilbert–Schmidt Form at $n=4$](the-hilbert-schmidt-form-at-n-4.html), for the positive definite companion of this form.
- [The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$](the-trace-form-and-its-inertia-on-the-two-halves-of-m2r.html), for the same computation at order two.
