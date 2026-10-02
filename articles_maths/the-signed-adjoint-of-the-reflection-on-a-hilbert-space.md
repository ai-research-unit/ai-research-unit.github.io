# __The Signed Adjoint of the Reflection on a Hilbert Space__

## Introduction

A reflection of the graded algebra $B(H)$ is the signed conjugation $\rho_U(T)=U\,\alpha(T)\,U^{-1}$, the signed sandwich with the second parameter the inverse of the first, and it is an involutive $*$-automorphism for every reflector $U$, that is, every invertible $U$ whose twisted product $U\alpha(U)$ is scalar. This article computes the adjoint of the reflection with respect to the Hilbert–Schmidt form of the category and reads off the consequences. The adjoint is again a reflection,

$$
(\rho_U)^*=\rho_{\alpha(U^*)},
$$

so the family of reflections is closed under adjunction, and the adjoint operation is the composite of the involution of the parameters, $U\mapsto U^*$, with the grade involution, $U\mapsto\alpha(U)$. The reflection is unitary on the Hilbert–Schmidt space whenever the reflector is unitary, and it is self-adjoint exactly when $\alpha(U^*)$ agrees with $U$ up to a scalar. The self-adjointness is therefore not automatic: the inner automorphisms of a Hilbert space are, in general, not self-adjoint operators on the Hilbert–Schmidt space, and the article isolates the condition and the degenerate case in which the correspondence between the reflector and the self-adjoint reflection fails.

This article fixes the reflector and the reflection, the adjoint of the reflection and its closed form, the unitarity of the reflection for a unitary reflector, the self-adjointness criterion, the eigenvalue decomposition of a self-adjoint reflection, and the failure in the degenerate case $\alpha=\mathrm{id}$. The reflections and their algebra are *Reflections as Signed Two-Sided Operators on a Hilbert Space*; the signed sandwich and its composition table are *The Signed Sandwich on a Hilbert Space*; the adjoint of the sandwich is *The Signed Adjoint Sandwich on a Hilbert Space*; the one-sided adjoints are *The Adjoint of the Left Multiplication on a Hilbert Space* and *The Signed Adjoint of the Left Multiplication on a Hilbert Space*; the unitary operators are *Unitary Operators*.

Throughout, $H=H^0\oplus H^1$ is a graded Hilbert space over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ with parity operator $\Gamma$, grade involution $\alpha(T)=\Gamma T\Gamma$ and Hilbert–Schmidt form $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$; a **reflector** is an invertible $U$ with $U\alpha(U)=\lambda I$ scalar, and the **reflection** is the signed conjugation $\rho_U=S_{U,U^{-1}}$, $\rho_U(T)=U\alpha(T)U^{-1}$. The adjoint is taken with respect to the Hilbert–Schmidt form and is written with a star.

## The Adjoint of the Reflection

**Theorem (the adjoint).** For every reflector $U$ the reflection has adjoint

$$
(\rho_U)^*=S_{\alpha(U^*),\,\alpha((U^*)^{-1})}=\rho_{\alpha(U^*)},
$$

so the adjoint of a reflection is the reflection by the $\alpha$-adjoint reflector; the adjoint operation on the reflections is an involution, $((\rho_U)^*)^*=\rho_U$, and it commutes with the scalar ambiguity of the reflector.

*Proof.* The reflection is the signed sandwich $S_{U,U^{-1}}$, whose adjoint is $S_{\alpha(U^*),\alpha((U^{-1})^*)}$ by *The Signed Adjoint Sandwich on a Hilbert Space*; since $(U^{-1})^*=(U^*)^{-1}$ and $\alpha$ is multiplicative, $\alpha((U^{-1})^*)=\alpha((U^*)^{-1})=(\alpha(U^*))^{-1}$, so the second parameter is the inverse of the first and the sandwich is the reflection $\rho_{\alpha(U^*)}$. The square of the operation is the identity because $U\mapsto U^*$ and $\alpha$ are involutions, and a scalar multiple of $U$ produces the same reflector property and the same adjoint reflection.

**Corollary (the unitary case).** If $U$ is unitary then $\alpha(U^*)=\alpha(U)^{-1}$ and

$$
(\rho_U)^*=\rho_{\alpha(U)^{-1}},
$$

so the adjoint is the reflection by the inverse of the twisted unitary, and it coincides with $\rho_U$ exactly when $U^2$ is a scalar.

*Proof.* Substitute $U^*=U^{-1}$ in the theorem; the second parameter of the sandwich adjoint is then the inverse of the first, which identifies the adjoint as the reflection by $\alpha(U)^{-1}$. The comparison with $\rho_U$ is the criterion of the self-adjointness theorem below.

**Proposition (the adjoint on the eigenvalue pieces).** Let $U$ be a reflector with reflection $\rho=\rho_U$ and eigenvalue decomposition $B(H)=B(H)^+_\rho\oplus B(H)^-_\rho$. The adjoint reflection is again an involutive $*$-automorphism, with its own eigenvalue decomposition

$$
B(H)=B(H)^+_{\rho_{\alpha(U^*)}}\oplus B(H)^-_{\rho_{\alpha(U^*)}} ;
$$

a self-adjoint reflection has mutually orthogonal eigenvalue pieces, the Hilbert–Schmidt orthogonal complement of $B(H)^+_\rho$ being $B(H)^-_\rho$, and in general the two decompositions differ by the adjunction.

*Proof.* The adjunction of operators preserves sums, products and the adjoint, so the adjoint of an involutive $*$-automorphism is again one, and hence has the eigenvalue decomposition; a self-adjoint involution on a Hilbert space has orthogonal eigenspaces, and the two eigenspaces of an involution are complementary, which gives the orthogonality statement; the two decompositions coincide exactly when the reflection is self-adjoint.

## Unitarity and Self-Adjointness

**Theorem (unitarity).** If the reflector $U$ is unitary then the reflection $\rho_U$ is a unitary operator on the Hilbert–Schmidt space; in general, for invertible $U$, the reflection is unitary if and only if $\alpha(U^*)U$ is a scalar, equivalently $\alpha(U^*)=kU^{-1}$.

*Proof.* $\rho_U$ is invertible with inverse $\rho_U^{-1}=\rho_{U^{-1}}$, and $(\rho_U)^*=\rho_{\alpha(U^*)}$; the reflection is unitary exactly when $(\rho_U)^*=\rho_U^{-1}$, and two reflections coincide exactly when their parameters are reciprocal scalar multiples, so the criterion is $\alpha(U^*)=kU^{-1}$, that is, $\alpha(U^*)U=kI$. For a unitary reflector $U^*=U^{-1}$ and $\alpha(U)=\pm U$, so $\alpha(U^*)U=\alpha(U)^{-1}U=\pm U^*U=\pm I$ is a scalar, and the reflection is unitary.

**Theorem (self-adjointness).** The reflection is self-adjoint, $(\rho_U)^*=\rho_U$, if and only if

$$
\alpha(U^*)=k\,U
$$

for a nonzero scalar $k$; for a unitary reflector the criterion is that $U^2$ be a scalar, and it is the same condition for the even and for the odd unitaries. In particular a general unitary reflector does not give a self-adjoint reflection.

*Proof.* The adjoint is $\rho_{\alpha(U^*)}$, and two reflections coincide exactly when their parameters are reciprocal scalar multiples, which gives the criterion. For unitary $U$ one has $U^*=U^{-1}$ and the criterion $\alpha(U^{-1})=kU$ reads $\alpha(U)^{-1}=kU$; multiplying by $U$ gives $\alpha(U)^{-1}U=kU^2$, and since $\alpha(U)=\pm U$ on a unitary, $U^2$ is a scalar. Conversely $U^2=cI$ makes $U^*=c^{-1}U$ and $\alpha(U)=\pm U$, so $\alpha(U^*)=\pm c^{-1}U$ is a scalar multiple of $U$ and the reflection is self-adjoint.

**Corollary (the self-adjoint reflection is an orthogonal symmetry).** A self-adjoint reflection is an involutive unitary with eigenvalues $\pm1$ on the Hilbert–Schmidt space, its eigenvalue pieces are mutually orthogonal and they exhaust the space, and it is the orthogonal symmetry with respect to the fixed algebra $B(H)^+_\rho$.

*Proof.* A self-adjoint involution has the spectral decomposition with eigenvalues $\pm1$ on orthogonal eigenspaces, and its fixed algebra is one of them; the exhaustive decomposition is the eigenvalue decomposition of the reflection, and the orthogonality is the self-adjointness.

**Example (the grade involution).** The identity is a reflector, $\rho_I=\alpha$, and its adjoint is $(\alpha)^*=\rho_{\alpha(I^*)}=\rho_{\alpha(I)}=\rho_I=\alpha$; the grade involution is self-adjoint for the Hilbert–Schmidt form, in agreement with the direct computation $\langle\alpha(X),Y\rangle_{\mathrm{HS}}=\langle X,\alpha(Y)\rangle_{\mathrm{HS}}$. Its eigenvalue pieces are the even and odd parts of $B(H)$, orthogonal in the Hilbert–Schmidt form, and the reflection is the symmetry that distinguishes them.

## The Degenerate Case

**Theorem (failure at $\alpha=\mathrm{id}$).** Suppose the grading is trivial, $H^1=0$, so that $\alpha=\mathrm{id}$; then the reflectors are the scalar multiples of the unitaries, the reflection is the inner automorphism $\iota_U$, and

$$
(\iota_U)^*=\iota_{U^*} .
$$

Consequently $\iota_U$ is self-adjoint if and only if $U^*=kU$ for a nonzero scalar $k$; for a unitary $U$ this is $U^2$ scalar. A general inner automorphism of $B(H)$ by a unitary is therefore not self-adjoint on the Hilbert–Schmidt space, and the correspondence between the reflector and the self-adjoint reflection fails beyond the self-adjoint reflections.

*Proof.* With $\alpha=\mathrm{id}$ the adjoint theorem gives $(\iota_U)^*=\rho_{U^*}=\iota_{U^*}$; the reflection equality $\iota_U=\iota_V$ iff $V=kU$ gives the self-adjointness criterion; for unitary $U$, $U^*=kU$ reads $U^2=k^{-1}I$, so $U^2$ is scalar. Taking a diagonal unitary with distinct unimodular eigenvalues shows $U^2$ is not scalar and the inner automorphism is not self-adjoint.

**Corollary (the self-adjoint inner automorphisms).** In the degenerate case the self-adjoint inner automorphisms are exactly the conjugations by the unitary operators with $U^2$ scalar, that is, the reflections through a real orthogonal structure; the inner automorphism by a self-adjoint unitary is one of them, and the group of self-adjoint inner automorphisms is the group of such unitaries modulo the scalars.

*Proof.* The criterion $U^2$ scalar characterises the unitaries whose conjugation is self-adjoint; the scalar ambiguity of the parameter gives the quotient by the centre, and a self-adjoint unitary $U=U^*$ has $U^2=I$, hence belongs.

**Proposition (the general case contains the degenerate one).** When the grading is nontrivial the reflections include the inner automorphisms by the even unitaries, and for these the self-adjointness condition $\alpha(U^*)=kU$ reduces to $U^*=kU$ because $\alpha$ fixes them; the nontrivial grading therefore does not repair the failure, it only adds the reflections by the odd unitaries, for which the twisted condition differs from the untwisted one by the sign of the odd part.

*Proof.* An even unitary $U$ has $\alpha(U)=U$, so $\alpha(U^*)=\alpha(U)^*=U^*$ and the criterion is the degenerate one; an odd unitary $U$ has $\alpha(U)=-U$, so $\alpha(U^*)=-U^*$ and the criterion is $U^*=-kU$, which is the sign-twisted equation of the degenerate case.

## Summary

For a reflector $U$, the reflection $\rho_U(T)=U\alpha(T)U^{-1}$ has adjoint $(\rho_U)^*=\rho_{\alpha(U^*)}$ with respect to the Hilbert–Schmidt form, so the reflections are closed under adjunction, the operation being the composite of the Hilbert adjoint of the parameter with the grade involution. The reflection is unitary exactly when $\rho_U^*=\rho_U^{-1}$, that is, when $\alpha(U^*)U$ is a scalar, and in particular every unitary reflector gives a unitary reflection; it is self-adjoint exactly when $\alpha(U^*)=kU$ for a scalar, which for a unitary reflector is the scalar condition $U^2=cI$ and for the degenerate grading $\alpha=\mathrm{id}$ is the same condition, so a general unitary reflector does not give a self-adjoint reflection. A self-adjoint reflection is then an orthogonal symmetry with eigenvalues $\pm1$ on the orthogonal pieces it distinguishes. The grade involution itself, the reflection by the identity, is self-adjoint, and the degenerate case shows that the general inner automorphism of $B(H)$ by a unitary is not self-adjoint on the Hilbert–Schmidt space; the nontrivial grading adds the odd reflectors without repairing that failure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_U(T)=U\alpha(T)U^{-1}=S_{U,U^{-1}}(T)$ | the reflection |
| $U\alpha(U)=\lambda I$, $|\lambda|=1$ | the reflector condition |
| $(\rho_U)^*=\rho_{\alpha(U^*)}$ | the adjoint of the reflection |
| $(\rho_U)^*=\rho_U^{-1}\iff\alpha(U^*)U$ scalar | the unitarity criterion |
| $\alpha(U^*)=kU$ | self-adjointness criterion |
| $U^2$ scalar | the criterion in the degenerate case |
| $B(H)^\pm_\rho$ | the eigenvalue pieces of a reflection |
| $\rho_I=\alpha$ | the grade involution, self-adjoint |
| $\iota_U$ | the inner automorphism in the degenerate case |
| $\rho_A=\rho_C\iff A=kC$ | the scalar ambiguity |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the $*$-automorphisms, the inner automorphisms and the adjoint operation.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the elementary operators and their adjoints.
- Barry Simon, *Trace Ideals and Their Applications*, Mathematical Surveys and Monographs 120 (American Mathematical Society, 2nd ed. 2005), for the Hilbert–Schmidt form and the rank-one computations.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the adjoint of an inner automorphism and the reflection examples.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the automorphisms of $B(H)$ and the unitary implementations.
