# __The Symmetric and Antisymmetric Parts of the Operator Space at $n=4$__

## Introduction

**The operator space $\operatorname{End}(M_4(\mathbb{C}))$ has complex dimension $256$ and carries two commuting involutions, the plain transpose and the Hilbert–Schmidt adjoint; the four simultaneous eigenspaces have real dimensions $136$, $136$, $120$ and $120$, the model operator $X\mapsto AXB$ has adjoint $Y\mapsto A^{\ast}YB^{\ast}$, and the commutator $T\mapsto[A,T]$ is always skew for the trace pairing.**

The article sets up the two involutions, proves that they commute, computes the four eigenspaces and their real dimensions, treats the model operator and its adjoint as an example that mixes the two structures, proves the skewness of the commutator, and separates the two scales: the symmetric and antisymmetric parts of the operator space are about operators of dimension $256$, while the two halves of the algebra are about elements of dimension $16$.

It assumes *The Adjoints and the Polar Decomposition of an Operator at $n=4$*, *$\operatorname{End}(M_4(\mathbb{C}))$ as an Algebra: the Regular Representation* and *The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form at $n=4$*. The model at order two is *The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$*.

## The Operator Space and the Two Involutions

**Proposition.** $\operatorname{End}(M_4(\mathbb{C}))$ has complex dimension $256$ and real dimension $512$, and every operator has a representing $16\times16$ matrix in a chosen basis of the matrix space.

**Proof.** A linear map of a complex space of dimension sixteen is a $16\times16$ complex matrix.

**Definition.** The **plain transpose** $\sigma$ sends an operator to its adjoint for $\beta(X,Y)=\operatorname{tr}(XY)$; the **Hilbert–Schmidt adjoint** $\tau$ sends it to its adjoint for $\langle X,Y\rangle=\operatorname{tr}(X^{\ast}Y)$.

**Proposition.** $\sigma$ is complex-linear with $\sigma^{2}=\mathrm{id}$, $\tau$ is antilinear with $\tau^{2}=\mathrm{id}$, and $\sigma\tau=\tau\sigma$.

**Proof.** In a real basis of the matrix space, $\sigma$ is the transpose of the $16\times16$ matrix and $\tau$ is the conjugate transpose, so $\tau=\kappa\sigma$ with $\kappa$ the entrywise conjugation; conjugation commutes with transposition, hence the two commute, and each squares to the identity.

**Corollary.** The four simultaneous eigenspaces are the intersections of the $\pm1$ eigenspaces of the two involutions, and they span the whole space.

**Proof.** Commuting involutions are simultaneously diagonalisable over the reals.

**The sign pattern.** The composition $\sigma\tau=\kappa$ is the coefficient conjugation, so an operator with $\sigma$-eigenvalue $s$ and $\tau$-eigenvalue $t$ has conjugate equal to $st$ times itself.

**Proof.** $\kappa=\sigma\tau$ acts on the simultaneous eigenspace as $st$.

## The Four Eigenspaces

**Theorem.** The four eigenspaces have real dimensions
$$
\dim\{\sigma=1,\tau=1\}=136,\quad \dim\{\sigma=1,\tau=-1\}=136,\quad \dim\{\sigma=-1,\tau=1\}=120,\quad \dim\{\sigma=-1,\tau=-1\}=120,
$$
and they sum to $512$.

**Proof.** The $\sigma=1$ eigenspace is the symmetric $16\times16$ matrices, of complex dimension $136$; inside it the condition $\tau=1$ is the reality of the entries, which halves nothing but fixes the real dimension at $136$, and $\tau=-1$ is the purely imaginary part, also of real dimension $136$. The $\sigma=-1$ eigenspace is the skew matrices, of complex dimension $120$, and again the two reality conditions give real dimensions $120$ and $120$.

**Corollary.** The two complex-linear halves are of complex dimensions $136$ and $120$, and the four real halves are the symmetric-real, symmetric-imaginary, skew-imaginary and skew-real operators.

**Proof.** The classification by the pair of signs.

**Corollary.** $136=\tfrac{16\cdot17}{2}$ and $120=\tfrac{16\cdot15}{2}$, so the two linear halves are the symmetric and antisymmetric parts of the operator space in the ordinary sense.

**Proof.** The dimension of the symmetric and of the skew square matrices of order sixteen.

**The analogy with the algebra.** The element space has dimensions $10$ and $6$, the operator space $136$ and $120$, and the ratio is the passage from $n=4$ to $n=16$.

**Proof.** $\tfrac{4\cdot5}{2}=10$ and $\tfrac{4\cdot3}{2}=6$; $\tfrac{16\cdot17}{2}=136$ and $\tfrac{16\cdot15}{2}=120$.

## The Model Operator

**Definition.** For a pair $A,B$ let $\Phi_{A,B}$ be the operator $X\mapsto AXB$.

**Proposition.** $\Phi_{A,B}^{\mathrm{plain}}=\Phi_{B,A}$ and $\Phi_{A,B}^{\ast}=\Phi_{A^{\ast},B^{\ast}}$.

**Proof.** Both are the two-sided adjoint computations of the previous article, read as statements about the single operator $\Phi_{A,B}$.

**Corollary.** $\Phi_{A,B}$ is self-adjoint for the plain pairing exactly when $A=B$, and self-adjoint for the Hilbert–Schmidt pairing exactly when $B=A^{\ast}$.

**Proof.** The two formulas and the independence of the indices.

**Corollary.** The four eigenspaces meet the family $\{\Phi_{A,B}\}$ in four subfamilies, each parametrised by the single element $A$: the conditions are $B=A$, $B=-A$, $B=A^{\ast}$ and $B=-A^{\ast}$.

**Proof.** The two involutions act on the pair of indices by $B\mapsto A$ for the plain transpose and $B\mapsto A^{\ast}$ for the Hilbert–Schmidt adjoint.

**The commutator as a model.** The operator $T\mapsto[A,T]$ is $\Phi_{A,\mathrm I}-\Phi_{\mathrm I,A}$, so it is the difference of two model operators.

**Proof.** $AT-\mathrm I\,T = AT - TA$.

**Corollary.** Its plain adjoint is $\Phi_{\mathrm I,A}-\Phi_{A,\mathrm I}=-T\mapsto[A,T]$, so the commutator operator is plain skew-adjoint.

**Proof.** The adjoint of a difference is the difference of the adjoints.

**Corollary.** Its Hilbert–Schmidt adjoint is $T\mapsto[A^{\ast},T]$, so the commutator operator is skew-Hermitian exactly when $A$ is skew-Hermitian up to a scalar.

**Proof.** $\Phi_{A,I}^{\ast}-\Phi_{I,A}^{\ast}=\Phi_{A^{\ast},I}-\Phi_{I,A^{\ast}}$, and $\operatorname{ad}_{A^{\ast}}=-\operatorname{ad}_A$ forces $A^{\ast}+A$ to be a scalar.

## The Commutator

**Theorem.** For every $A$ the operator $\operatorname{ad}_A:T\mapsto[A,T]$ is a derivation of the algebra, and it is skew for the trace pairing:
$$
\beta(\operatorname{ad}_A T,U)+\beta(T,\operatorname{ad}_A U)=0 .
$$

**Proof.** The derivation property is the Jacobi identity for the associator; for the skewness, $\operatorname{tr}([A,T]U)+\operatorname{tr}(T[A,U])=\operatorname{tr}(ATU-TAU+TAU-TUA)=\operatorname{tr}(ATU)-\operatorname{tr}(TUA)=0$ by cyclicity.

**Corollary.** The derivation is skew for the Hilbert–Schmidt pairing exactly when $A$ is skew-Hermitian, since $\langle[A,T],U\rangle+\langle T,[A,U]\rangle=\operatorname{tr}(T^{\ast}[A^{\ast},U])$ up to a commutator.

**Proof.** The second computation with $A^{\ast}$ in place of $A$, and the vanishing of the mixed term exactly when $A^{\ast}=-A$.

**Corollary.** The two skewness statements differ by the involution, not by the derivation, so the same operator is skew for one pairing and not for the other.

**Proof.** The two computations.

**The image of the commutator.** The inner derivations are $\operatorname{ad}_{\mathfrak{sl}_4}$ and every derivation of $M_4$ is inner, so the commutator map is onto the derivations of the algebra.

**Proof.** Central simplicity and the derivation theorem.

**The operator of the commutator.** The map $T\mapsto[A,T]$ is an operator on the sixteen-dimensional space $M_4$; for a generic $A$ with distinct eigenvalues its kernel is the four-dimensional algebra generated by $A$, so its rank is $12$.

**Proof.** The kernel is the centraliser of $A$, which for a matrix with distinct eigenvalues is the algebra of polynomials in $A$, of dimension four; the rank is the difference.

## The Two Scales

**Proposition.** The symmetric and antisymmetric parts of the operator space are about the space $\operatorname{End}(M_4)$ of dimension $256$, while the two halves $\operatorname{Sym}_4$ and $\operatorname{Skew}_4$ are about the space $M_4$ of dimension $16$; the second pair is not a restriction of the first.

**Proof.** The dimensions differ and the objects live in different spaces.

**Corollary.** An element of $M_4$ that is symmetric as a matrix is not an operator, and an operator that is self-adjoint for the plain pairing is not an element; the words "symmetric" and "antisymmetric" apply to both only by analogy.

**Proof.** The two spaces are different, and the involutions are different.

**Corollary.** The bridge between the two scales is the regular representation: $A\mapsto L_A$ carries the element algebra into the operator space as the four-dimensional subalgebra $\mathbb{B}_L$.

**Proof.** The left multiplications form a subalgebra of dimension four, isomorphic to $M_2(\mathbb{C})$.

**The mixed statement.** The operator $L_A$ is self-adjoint for the plain pairing exactly when $A$ is a scalar, since $L_A^{\mathrm{plain}}=R_A$ and $R_A=L_A$ only then.

**Proof.** The plain adjoint of $L_A$ is $R_A$, and the two families meet in the scalars.

**Corollary.** The symmetric half of the algebra does not map to the self-adjoint part of the operator space under the left regular representation; the self-adjoint part of $\mathbb{B}_L$ is only the scalars.

**Proof.** The previous proposition.

## Summary

The operator space has complex dimension $256$ and carries two commuting involutions, the plain transpose and the Hilbert–Schmidt adjoint. The four simultaneous eigenspaces have real dimensions $136$, $136$, $120$ and $120$, and they sum to the real dimension $512$; the two complex-linear halves have dimensions $136$ and $120$, the symmetric and antisymmetric parts of a $16\times16$ matrix space.

The model operator $X\mapsto AXB$ has plain adjoint $X\mapsto BXA$ and Hilbert–Schmidt adjoint $X\mapsto A^{\ast}XB^{\ast}$, and the commutator $T\mapsto[A,T]$ is a difference of two model operators. The commutator is always skew for the trace pairing and is skew for the Hilbert–Schmidt pairing exactly when $A$ is skew-Hermitian.

The two scales must be kept apart: the halves of the algebra are a ten and a six inside a sixteen, the halves of the operator space a $136$ and a $120$ inside a $256$, and the left regular representation does not carry one to the other in the naive way.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | the plain transpose involution, complex-linear |
| $\tau$ | the Hilbert–Schmidt adjoint, antilinear |
| $136$, $120$ | the complex dimensions of the two linear halves |
| $\Phi_{A,B}(X)=AXB$ | the model operator |
| $\operatorname{ad}_A(T)=[A,T]$ | the commutator operator |
| $\kappa=\sigma\tau$ | the coefficient conjugation |

## Further Reading

- [The Adjoints and the Polar Decomposition of an Operator at $n=4$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-4.html), for the two adjoints of a single operator.
- [$\operatorname{End}(M_4(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m4c-as-an-algebra-the-regular-representation.html), for the operator algebra and the two images.
- [The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form at $n=4$](the-derivation-commutator-and-its-skewness-for-the-trace-form-at-n-4.html), for the derivation and the two skewness statements.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-4.html), for the halves of the element space.
- [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html), for the case at order two.
