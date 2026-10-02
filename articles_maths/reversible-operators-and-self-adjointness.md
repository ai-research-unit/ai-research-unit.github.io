
# __Reversible Operators and Self-Adjointness__

## Introduction

A **reversing symmetry** is an involutive operator that conjugates an operator into its adjoint, and it refines both the self-adjointness and the spectrum. Precisely, let $J$ be an involution of the Hilbert space, $J^2=I$, unitary or anti-unitary; an operator $T$ is **reversible** with respect to $J$ when
$$
T^*=J\,T\,J^{-1}=J\,T\,J ,
$$
that is, when $J$ intertwines $T$ with its adjoint. The definition includes the self-adjoint operators, for which $T^*=T$ and the reversibility is the commutation $TJ=JT$, and it includes the operators that are self-adjoint **only up to the symmetry**, whose spectra are conjugate-symmetric rather than real. The article develops the theory: the parity decomposition induced by a unitary involution, the block form of a reversible operator, the refinement of the spectrum into the parity parts, the conjugate symmetry of the spectrum in the non-self-adjoint case, and the application to a stationary process, where the reversing symmetry is the reversal $U_r$ of the index, the reversible operator is the transition operator of a reversible process, and the refinement of the spectrum is the symmetry of the relaxation of the chain under the reversal of the trajectories.

The conventions are those of the category. The reversible chains, the time reversal and the detailed balance are *Reversible Markov Chains and Time Reversal*, earlier in this category; the reversibility of a stationary process and the reversal of the law are *The Reversibility of a Stationary Process*, earlier in this category; the adjoint of the Markov operator is *The Adjoint of the Markov Operator*, earlier in this category; the involution on the operator algebra of a process, with the reversal unitary $U_r$ and the automorphism $\tau$, is *The Involution on the Operator Algebra of a Process*, earlier in this category; the adjoint of the transition operator is *The Adjoint of the Transition Operator*, earlier in this category. The $J$-self-adjoint and $J$-unitary operators with respect to an indefinite form are *J-Self-Adjoint and J-Unitary Operators*, written, and the self-adjoint operators, the spectral theorem and the functional calculus are *Banach and Hilbert Spaces*, written, and *Self-Adjoint Operators and the Spectral Theorem*, written. The operator algebra and its involutions are *Operator Algebras*, written. No physics is invoked.

Throughout, $\mathcal{H}$ is a complex Hilbert space with the form $\langle\cdot,\cdot\rangle$, $J$ is an involution with $J^2=I$, and $T$ is a bounded operator on $\mathcal{H}$; when $J$ is unitary it is self-adjoint, $J^*=J^{-1}=J$. The parity decomposition is $\mathcal{H}=\mathcal{H}_+\oplus\mathcal{H}_-$ with $\mathcal{H}_\pm$ the $\pm1$-eigenspaces of $J$. The operators of a process act on $\mathcal{H}=L^2(\Omega,\mathbb P)$ with the form $\langle f,g\rangle=\varphi(fg^*)$, and the reversal unitary is $U_rf=f\circ r$.

## The Reversing Symmetry

### Definition and the parity decomposition

**Definition.** A **reversing symmetry** of $\mathcal{H}$ is an involution $J$ with $J^2=I$, either **unitary**, $J^*=J^{-1}=J$, or **anti-unitary**, a conjugation with $J(\lambda x)=\bar\lambda Jx$ and $J^*=J^{-1}=J$ in the anti-linear sense.

**Theorem (the parity decomposition).** For a unitary involution $J$ the eigenspaces
$$
\mathcal{H}_+=\{x:Jx=x\},\qquad \mathcal{H}_-=\{x:Jx=-x\}
$$
are closed, orthogonal, and $\mathcal{H}=\mathcal{H}_+\oplus\mathcal{H}_-$; the orthogonal projections $P_\pm=\frac12(I\pm J)$ are self-adjoint projections and $J=P_+-P_-$. Every $x$ splits uniquely as $x=x_++x_-$ with $x_\pm\in\mathcal{H}_\pm$.

*Proof.* The eigenvalues of an involution are $\pm1$; the eigenspaces of a self-adjoint involution are orthogonal and span the whole space; the projections are the spectral projections of $J$, which are self-adjoint, and the decomposition is the spectral theorem for $J$.

### The two classes of reversing symmetry

**Theorem (the unitary and the anti-unitary case).** A unitary reversing symmetry is the parity operator of a decomposition and refines the spectrum into the parity blocks; an anti-unitary reversing symmetry is a conjugation and gives the classes of **complex symmetric** operators. The two cases share the intertwining relation $T^*=JTJ$ and differ in the reality of the symmetry.

*Proof.* The unitary $J$ is normal and diagonalisable with the eigenvalues $\pm1$; an anti-unitary $J$ has no eigenvalues in the ordinary sense but still satisfies $J^2=I$ and $J^*=J$, and the intertwining relation $T^*=JTJ$ makes sense in both cases because $J$ is anti-linear and $T^*$ is the Hilbert adjoint. The classes are distinguished by whether $J$ preserves the complex structure.

## Reversible Operators

### Definition and first properties

**Definition.** An operator $T$ is **reversible** with respect to $J$ if
$$
T^*=J\,T\,J ,
$$
and it is **$J$-self-adjoint** in the same condition read on the indefinite form $[x,y]=\langle Jx,y\rangle$ (for the unitary $J$).

**Theorem (properties).** The reversibility is an involution-preserving condition: if $T$ is reversible then so are $T^*$ and $JTJ$; the reversible operators form a closed subspace and a Jordan algebra, being closed under the symmetrised product $\{S,T\}=ST+TS$. If $T$ is self-adjoint, the reversibility is the commutation $TJ=JT$, and then $T$ is reversible if and only if it preserves the parity decomposition.

*Proof.* From $T^*=JTJ$, taking adjoints and using $J^*=J$ gives $T=JT^*J$, so $T^*$ is reversible; the subspace is closed because the relation is linear; the Jordan closure is the identity $(ST+TS)^*=S^*T^*+T^*S^*=JSJ\,JTJ+JTJ\,JSJ=J(ST+TS)J$; for a self-adjoint $T$ the condition is $T=JTJ$, which is $TJ=JT$ because $J^2=I$, and the commutation with the parity operator is the preservation of the two eigenspaces.

### Self-adjointness up to the symmetry

**Theorem (the spectrum is conjugate-symmetric).** If $T$ is reversible with respect to $J$, then $J$ intertwines $T$ and $T^*$, so $T$ and $T^*$ are similar and
$$
\operatorname{spec}(T)=\operatorname{spec}(T^*)=\overline{\operatorname{spec}(T)},
$$
that is the spectrum of a reversible operator is symmetric under $\lambda\mapsto\bar\lambda$.

*Proof.* The intertwining gives $T^*=JTJ^{-1}$ with $J^{-1}=J$, so $T^*$ is similar to $T$ and they have the same spectrum; the spectrum of the adjoint is the conjugate, $\operatorname{spec}(T^*)=\overline{\operatorname{spec}(T)}$, since $T^*-\bar\lambda I=(T-\lambda I)^*$; combining the two gives the conjugate symmetry.

**Corollary (self-adjointness and reversibility).** A self-adjoint operator is reversible if and only if it commutes with $J$; an operator that is reversible but not self-adjoint has a conjugate-symmetric spectrum that need not be real, and the non-real eigenvalues occur in conjugate pairs of equal multiplicity.

*Proof.* The self-adjoint case is the theorem above with $T^*=T$, giving $T=JTJ$ and the commutation; in the general case the conjugate symmetry of the spectrum forces the non-real eigenvalues into conjugate pairs, with the multiplicities matched because the similarity $T\simeq T^*$ is implemented by the involution $J$.

## The Refinement of the Spectrum

### The block decomposition

**Theorem (the refinement).** Let $J$ be a unitary involution and let $T$ be reversible and self-adjoint, so that $TJ=JT$. Then $T$ decomposes as
$$
T=T_+\oplus T_-,\qquad T_\pm=T|_{\mathcal{H}_\pm},
$$
the operators $T_\pm$ are self-adjoint on $\mathcal{H}_\pm$, the spectrum splits as
$$
\operatorname{spec}(T)=\operatorname{spec}(T_+)\cup\operatorname{spec}(T_-),
$$
and every eigenvector of $T$ has a definite parity; the reversing symmetry therefore **refines** the spectrum by separating the even and the odd modes.

*Proof.* The commutation $TJ=JT$ makes the eigenspaces of $J$ invariant under $T$, so $T$ is block-diagonal in the parity decomposition; the restrictions are self-adjoint because $T$ is and the subspaces are reducing; the spectrum of a block-diagonal operator is the union of the spectra of the blocks; the eigenvector of a nondegenerate eigenvalue is even or odd by the invariance of the eigenspaces.

**Corollary (the reversing symmetry of the spectral measure).** For a reversible self-adjoint $T$ with the simple spectrum the spectral measure of a vector $x=x_++x_-$ splits into the measures of the parity parts, and the resolvent and the functional calculus preserve the parity; the reversing symmetry is a symmetry of the whole spectral analysis.

*Proof.* The functional calculus of a block-diagonal operator acts blockwise, and the spectral measure of $x$ is the sum of the measures of $x_+$ and $x_-$; the statement is the block form of the spectral theorem.

### The spectral symmetry in the non-self-adjoint case

**Theorem (the conjugate pair reflection).** Let $T$ be reversible with respect to a conjugation $J$ (anti-unitary), the case of the complex symmetric operators. Then the spectrum is conjugate-symmetric and the pairing of the eigenvectors is implemented by $J$: an eigenvector of $T$ at $\lambda$ is carried by $J$ to an eigenvector of $T^*$ at $\bar\lambda$, so the reversing symmetry reflects the spectrum across the real axis.

*Proof.* From $T^*=JTJ$ applied to $Tx=\lambda x$ and the anti-linearity of $J$, one gets $T^*(Jx)=JTx=J(\lambda x)=\bar\lambda\,Jx$, so $Jx$ is an eigenvector of $T^*$ at $\bar\lambda$; the reflection across the real axis is the content of the conjugate symmetry of the spectrum, and the pairing is the intertwining.

## The Reversing Symmetry of a Process

**Theorem (the reversible process).** Let $\{X_n\}$ be a stationary process, $U_r$ the reversal operator, $U_rf=f\circ r$, and $P$ its transition or Markov operator with the stationary measure $\pi$. Then
$$
U_r\,P\,U_r=\hat P ,
$$
the transition operator of the reversed process, and the process is reversible exactly when $U_rPU_r=P$, that is exactly when $P$ is reversible with respect to $U_r$ and self-adjoint for the $\pi$-form. In that case the spectrum of $P$ refines into the even and the odd parts under the reversal, and the eigenfunctions have definite parity.

*Proof.* The conjugation by $U_r$ reverses the direction of the transitions, giving $\hat P$, by *The Involution on the Operator Algebra of a Process* and *The Adjoint of the Markov Operator*, earlier in this category; the self-adjointness $P^*=P$ in the reversible case is the theorem of *The Adjoint of the Markov Operator*; combining, $U_rPU_r=\hat P=P$ and $P$ commutes with the unitary involution $U_r$, so the refinement theorem applies with $J=U_r$.

## Worked Examples

**Example (the parity of the two-state chain).** For the two-state chain the reversal $U_r$ exchanges the two states and is the unitary involution with the parity decomposition into the symmetric and antisymmetric vectors; the transition operator is self-adjoint and commutes with $U_r$, its two eigenvalues $1$ and $1-a-b$ being the eigenvalues on the symmetric and the antisymmetric part; the spectrum refines into the even mode and the odd mode.

**Example (the reflection symmetry of the circle).** On $L^2(\mathbb R/\mathbb Z)$ with $Jf(\theta)=f(-\theta)$ the operator $J$ is a unitary involution with the parity decomposition into the even and the odd functions; the multiplication by $\cos(2\pi\theta)$ is self-adjoint and reversible, and its spectrum $[-1,1]$ refines into the parts of the even and the odd functions, the two parts overlapping on the whole interval.

**Example (the complex symmetric operator).** The operator $T$ represented in a basis by a complex symmetric matrix is reversible with respect to the conjugation $J$ given by the complex conjugation in that basis; its spectrum is conjugate-symmetric and the non-real eigenvalues occur in conjugate pairs, with the eigenvectors paired by $J$. The example is the original class of the reversible operators and the source of the conjugate-pair reflection.

**Example (the non-reversible operator).** For the directed cycle the conjugation by $U_r$ sends the transition operator to $\hat P\ne P$, so the operator is not reversible; its spectrum is not conjugate-symmetric as a whole, being the cyclic shift with the eigenvalues on the unit circle, and no parity refinement occurs. The example shows that the reversibility is a genuine restriction and not a property of every contraction.

## Failure of the Degenerate Cases

The reversibility degenerates in four configurations. First, a reversible operator need not be self-adjoint, and its spectrum need not be real; the conjugate symmetry is the only spectral consequence in general, and the real spectrum holds exactly for the self-adjoint members, which is the extra hypothesis. Second, the reversing symmetry is an involution on the Hilbert space and need not preserve any given dense subspace; the parity decomposition is a statement about the whole space, and the block decomposition requires the reducing hypothesis $TJ=JT$, which is the self-adjoint case. Third, an anti-unitary reversing symmetry gives the conjugate-pair reflection but no parity decomposition in the ordinary sense, since a conjugation has no eigenvalues; treating the two cases alike is the standard error. Fourth, the reversibility of an operator and the reversibility of a process are different statements: the process is reversible when the reversing symmetry fixes its transition operator, while an operator can be reversible with respect to a symmetry that is not the reversal of any measure-preserving involution; the identification is a theorem, not a definition.

## Summary

A reversing symmetry is an involution $J$ of the Hilbert space, unitary or anti-unitary, and an operator is reversible with respect to it when $T^*=JTJ$; the unitary case gives the parity decomposition $\mathcal{H}=\mathcal{H}_+\oplus\mathcal{H}_-$ and the projections $\frac12(I\pm J)$, the anti-unitary case gives the complex symmetric operators, and in both cases the spectrum of a reversible operator is conjugate-symmetric, $\operatorname{spec}(T)=\overline{\operatorname{spec}(T)}$. A self-adjoint operator is reversible exactly when it commutes with $J$, and then it is block-diagonal in the parity decomposition, its spectrum is the union of the spectra of the two blocks, and every eigenvector has a definite parity; this is the refinement of the spectrum by the reversing symmetry. For a stationary process the conjugation by the reversal $U_r$ sends the transition operator to the reversed one, $U_rPU_r=\hat P$, and the process is reversible exactly when $P$ is self-adjoint and commutes with $U_r$, in which case the spectrum of the chain refines into the even and the odd modes. The adjoint is *The Adjoint of the Markov Operator*, earlier in this category, the reversal in the operator algebra is *The Involution on the Operator Algebra of a Process*, earlier in this category, and the indefinite-form theory of the $J$-self-adjoint operators is *J-Self-Adjoint and J-Unitary Operators*, written.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$, $J^2=I$ | the reversing symmetry, unitary or anti-unitary |
| $\mathcal{H}=\mathcal{H}_+\oplus\mathcal{H}_-$ | the parity decomposition |
| $P_\pm=\frac12(I\pm J)$ | the parity projections |
| $T^*=JTJ$ | reversibility |
| $\operatorname{spec}(T)=\overline{\operatorname{spec}(T)}$ | the conjugate-symmetric spectrum |
| $TJ=JT$ | reversibility of a self-adjoint operator |
| $T=T_+\oplus T_-$ | the block refinement |
| $\operatorname{spec}(T)=\operatorname{spec}(T_+)\cup\operatorname{spec}(T_-)$ | the refined spectrum |
| $U_rPU_r=\hat P$ | the reversal of the transition operator |

## Further Reading

- Tsuyoshi Ando and Chi-Kwong Li, "Operator radii and unitary equivalence", in *Operator Theory and Its Applications*, Fields Institute Communications 25 (American Mathematical Society, 2000), for the reversing symmetries and the operator radii.
- Stephan Ramon Garcia and Mihai Putinar, "Complex symmetric operators and applications", *Transactions of the American Mathematical Society* 358 (2006), 1285–1315, for the complex symmetric operators, their spectra and their conjugations.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the $J$-self-adjoint operators, the $J$-unitary operators and the indefinite forms.
- Peter Lancaster and Miron Tismenetsky, *The Theory of Matrices* (Academic Press, 2nd edition, 1985), for the reversing symmetries, the block decompositions and the spectra.
- Peter D. Lax, *Functional Analysis* (Wiley, 2002), for the involutions, the spectral theory and the functional calculus.
