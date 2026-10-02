# __Reversible Operators and the Involution__

## Introduction

A **reversible operator** is a linear operator $A$ on a Hilbert space that is conjugated to its inverse by an involution $C$ of the space,

$$
C^2=\mathrm{id}, \qquad C\,A\,C=A^{-1},
$$

where the involution $C$ is **unitary** in the reversible case and **anti-unitary** in the time-reversal case; the pair $(A,C)$ is the operator analogue of a reversible dynamical system, and the identity is the operator transcription of $RTR=T^{-1}$. The consequences for the spectrum are immediate and strong. The conjugation by an involution is an **isospectral** operation, so the spectrum of a reversible operator is invariant under $\lambda\mapsto\lambda^{-1}$: the eigenvalues occur in reciprocal pairs $\lambda,1/\lambda$, the eigenvector $Cv_\lambda$ of an eigenvector $v_\lambda$ is an eigenvector for $1/\lambda$, and the unit circle and the real reciprocal pairs are the two invariant strata. When $C$ is anti-unitary — the operator of complex conjugation, the time-reversal operator of the transfer-operator theory — the involution reverses the complex structure as well, the operator $A$ is real in the $C$-real structure, and the spectrum is invariant under $\lambda\mapsto\lambda^{-1}$ and $\lambda\mapsto\overline\lambda$ simultaneously, so that a real reciprocal pair is the pairing of an eigenvalue with its inverse and a complex pair is the pairing with the inverse conjugate. The companion structure is the **commuting** involution, $\sigma A=A\sigma$, which does not reverse the operator but splits it: the Hilbert space decomposes into the isotypic subspaces of the involution, the operator preserves them, and the spectrum is the union of the spectra of the blocks. The two structures — the reversing and the commuting — are the operator faces of the reversor and of the equivariant symmetry, and they are the subject of the present article.

The article develops the reversible operators and the involution. It defines the reversing and the commuting operator involutions, proves the **spectral theorem** for a reversible operator: the spectrum is invariant under inversion, the point eigenvalues occur in reciprocal pairs, and the eigenvectors are paired by the involution; it separates the **unitary** from the **anti-unitary** case, with the real structure and the additional conjugation symmetry of the latter; it treats the **commuting** involution and the two isotypic blocks, with the invariance of the spectrum as a union of the block spectra; it relates the abstract structure to the dynamics: the Koopman operator $U_T$ of a reversible map is reversible with $C=U_R$, the Perron–Frobenius operator inherits the reversibility, and the resonances of the reversible transfer operator come in reciprocal pairs; and it gives the examples — the reversible matrices and their reciprocal spectra, the elliptic, the hyperbolic and the symmetry-broken cases, and the anti-unitary real structure — with the eigenstructure recomputed.

The Hilbert spaces, the adjoints, the unitarity and the spectral theorem are those of *Hilbert Spaces and Spectral Theory* or the corresponding functional-analysis article of the system; the Koopman and the transfer operators, the adjoint and the duality, are *The Koopman Operator*, *The Transfer Operator* and *The Adjoint of the Koopman Operator*, the last immediately preceding; the reversible dynamics, the reversor and the symmetric orbits are *Reversible Dynamical Systems and Time-Reversal Symmetry* and *Symmetric Periodic Orbits and the Involution*; the self-adjoint time-reversal operator and the real structure are *Time Reversal and the Transfer Operator*, and the reversing symmetry of the flow is *The Involution on the Flow Operator*, both immediately following in this group. The symmetries commuting with the operator are the operator form of *Equivariant Dynamics under an Involution*, above.

No physics is invoked.

## The Reversing Involution on Operators

### Definition

**Definition.** Let $A$ be an invertible bounded operator on a complex Hilbert space $H$. A **reversing symmetry** of $A$ is an involution $C$ of $H$ with

$$
C^2=\mathrm{id}, \qquad C\,A\,C=A^{-1},
$$

the involution being **unitary** ($C^*=C^{-1}=C$, so that $C$ is a self-adjoint unitary) in the reversible case, or **anti-unitary** ($C$ is $\mathbb{C}$-anti-linear and $C^2=\mathrm{id}$) in the time-reversal case. The operator is **reversible** if it admits such a $C$; the pair $(A,C)$ is a **reversible operator**. An operator admitting a **commuting** involution $\sigma$ with $\sigma A=A\sigma$ has an **equivariant** (or ordinary) symmetry, and the two structures are distinct.

**Theorem (elementary properties).** Let $(A,C)$ be reversible with the reversing involution $C$. Then (i) $CAC=A^{-1}$ if and only if $C A=A^{-1}C$; (ii) $A$ is reversible with the same $C$ as its inverse and as every power $A^n$; (iii) if $A$ is unitary then $A^*=CAC$, so $A$ is \*-reversible, and in general $CA^*C=A^{-*}$; (iv) if $B=SAS^{-1}$ is a conjugation of $A$ then $SCS^{-1}$ reverses $B$; (v) the operators $AC$ and $CA$ are involutions, $(AC)^2=(CA)^2=\mathrm{id}$, and $A=(AC)\circ C$ is a product of two involutions.

*Proof.* (i) Multiplying $CAC=A^{-1}$ on the left by $C$ gives $AC=CA^{-1}$, and $C^2=I$. (ii) Conjugating $CAC=A^{-1}$ by $C$ gives $CA^{-1}C=A$, so $C$ reverses $A^{-1}$, and induction gives $CA^nC=A^{-n}$. (iii) For unitary $A$, $A^*=A^{-1}=CAC$. (iv) $B=SAS^{-1}$ and $(SCS^{-1})B(SCS^{-1})=SCS^{-1}SAS^{-1}SCS^{-1}=SCACS^{-1}=SA^{-1}S^{-1}=B^{-1}$. (v) $(AC)^2=ACAC=A(CA)C=A(A^{-1}C)C=I$, and $A=(AC)C$.

### The Spectral Theorem

**Theorem (the spectrum is inversion-invariant).** Let $(A,C)$ be reversible. Then the spectrum is invariant under inversion,

$$
\lambda\in\operatorname{spec}(A)\iff \lambda^{-1}\in\operatorname{spec}(A),
$$

and the point spectrum has the eigenvector pairing: if $Av_\lambda=\lambda v_\lambda$ then $A(Cv_\lambda)=\lambda^{-1}(Cv_\lambda)$ when $C$ is a unitary involution. In the anti-unitary case the same holds with $\lambda^{-1}$ replaced by $\overline{\lambda}^{-1}$, and the spectrum is additionally invariant under complex conjugation.

*Proof.* The map $B\mapsto CBC$ is an isospectral automorphism of the algebra of bounded operators (it is an algebra isomorphism, and it preserves invertibility and the norm), so $\operatorname{spec}(CAC)=\operatorname{spec}(A)$; since $CAC=A^{-1}$ this gives $\operatorname{spec}(A^{-1})=\operatorname{spec}(A)$, and $\operatorname{spec}(A^{-1})=\{\lambda^{-1}:\lambda\in\operatorname{spec}(A)\}$. For the eigenvector, $A(Cv_\lambda)=C(A^{-1}v_\lambda)=\lambda^{-1}(Cv_\lambda)$. In the anti-unitary case, $C$ is conjugate-linear, so the same computation with the scalar pulled through $C$ as its conjugate gives $\overline{\lambda}^{-1}$, and $\operatorname{spec}(A)=\operatorname{spec}(\overline A)=\overline{\operatorname{spec}(A)}$ by the real structure.

**Corollary (reciprocal pairs and the strata).** The eigenvalues of a reversible operator occur in reciprocal pairs, $(\lambda,\lambda^{-1})$: on the unit circle as a complex pair conjugate to $(\lambda,\overline\lambda)$ when $A$ is unitary, on the real axis as a pair $(\lambda,1/\lambda)$ with one eigenvalue of modulus greater than one and the other of modulus less than one, and in the anti-unitary case as the quadruple $\{\lambda,\overline\lambda,\lambda^{-1},\overline\lambda^{-1}\}$ when $\lambda$ is not real and not on the unit circle. The unit circle and the reciprocal real pairs are the invariant strata, and the eigenvalues on the unit circle are the ones that do not decay or blow up.

## The Commuting Involution

**Theorem (the isotypic splitting for a commuting involution).** Let $\sigma$ be a unitary involution with $\sigma A=A\sigma$. Then $A$ preserves the eigenspaces $H_+=H_+(\sigma)$ and $H_-=H_-(\sigma)$ of $\sigma$, the space decomposes as the isotypic direct sum $H=H_+\oplus H_-$, and the spectrum is the union

$$
\operatorname{spec}(A)=\operatorname{spec}(A|_{H_+})\cup\operatorname{spec}(A|_{H_-}),
$$

so the symmetric and the antisymmetric modes do not interact; if the involution $C$ reverses $A$ and commutes with $\sigma$, then $C$ exchanges $H_+$ and $H_-$ and pairs the spectra, and the reversible and the equivariant structures coexist.

*Proof.* The commutation gives $A(H_+)\subseteq H_+$: for $v\in H_+$, $\sigma(Av)=A(\sigma v)=Av$. The splitting of the spectrum is the block form of $A$; the last statement follows from $C\sigma=\sigma C$, which makes $C$ map $H_+$ to $H_-$ and conjugate $A|_{H_+}$ to $(A|_{H_-})^{-1}$.

**Remark (the two involutions on the operators).** The reversing involution $C$ and the commuting involution $\sigma$ act on the operator differently: the reversor produces the inversion of the spectrum and the reciprocal pairing, while the commuting symmetry produces the block decomposition and the isotypic union; the two may coexist and their product is then again a reversing involution or a commuting symmetry, in parallel with the group generated by a reversor and a symmetry in the dynamics. This is the operator-level dictionary of *Reversible Dynamical Systems and Time-Reversal Symmetry* and *Equivariant Dynamics under an Involution*.

## The Anti-Unitary Case and the Real Structure

**Definition.** An **anti-unitary involution** (a **conjugation**) is a map $C:H\to H$ with $C(\alpha u+\beta v)=\overline\alpha\,Cu+\overline\beta\,Cv$, $C^2=\mathrm{id}$, and $\langle Cu,Cv\rangle=\overline{\langle u,v\rangle}$. A conjugation defines a **real structure**: the fixed space $H_{\mathbb{R}}=\{u:Cu=u\}$ is a real Hilbert space with $H=H_{\mathbb{R}}\otimes\mathbb{C}$, and an operator is **real** when it commutes with $C$.

**Theorem (the time-reversal structure).** Let $A$ be reversible with respect to a conjugation $C$, $CAC=A^{-1}$. Then (i) the spectrum of $A$ is invariant under both $\lambda\mapsto\lambda^{-1}$ and $\lambda\mapsto\overline\lambda$; (ii) if $A$ is real and self-adjoint then $A=A^{-1}$, so $A$ is an involution with spectrum contained in $\{-1,+1\}$; (iii) an anti-unitary reversing involution makes a **self-adjoint** reversible operator automatically an involution, and the general real reversible operator has the spectrum in reciprocal conjugate pairs.

*Proof.* (i) The anti-unitary conjugation preserves the spectrum after complex conjugation, and the reversibility gives inversion. (ii) For a real self-adjoint $A$ the conjugation $C$ commutes with $A$; the reversibility $CAC=A^{-1}$ then gives $A=A^{-1}$. (iii) is (ii) applied to the self-adjoint case ($A^*=A$ and $A$ real give $CAC=\overline A=A$). The anti-unitary reversibility is the operator form of the time reversal of *Time Reversal and the Transfer Operator*, where the self-adjointness of the transfer operator is the consequence.

## The Dynamical Origin

**Theorem (the Koopman operator of a reversible map is reversible).** Let $T$ be an invertible measure-preserving reversible map with reversor $R$ that also preserves the measure. Then the Koopman operator $U_T$ is reversible:

$$
U_R\,U_T\,U_R=U_T^{-1}=U_T^*,
$$

with the unitary involution $C=U_R$; the Perron–Frobenius operator $P_T=U_T^*$ is likewise reversible, $U_RP_TU_R=P_T^{-1}$, and the resonances of the transfer operator come in reciprocal pairs.

*Proof.* $U_RU_TU_R=U_{RTR}=U_{T^{-1}}=U_T^{-1}$, and this equals $U_T^*$ when $T$ is unitary, by the adjoint theorem of *The Adjoint of the Koopman Operator*; the statement for $P_T=U_T^*$ is the adjoint of the identity, and the reciprocal resonances are the spectral theorem applied to $P_T$.

**Remark (the reversible transfer operator and the resonances).** For a reversible hyperbolic map the **Ruelle–Pollicott resonances** of the transfer operator are the eigenvalues of $P_T$ in the meromorphic continuation; the reversibility forces them into the reciprocal pairs $\lambda,1/\lambda$, and their symmetrisation about the unit circle is the operator-level statement of the reversible structure of the dynamics. The analytic theory of the resonances, their pairity and the zeta function are the subject of *The Transfer Operator* and of *Time Reversal and the Transfer Operator*.

## The Examples

**Example (an elliptic reversible matrix, verified).** The rotation by $\pi/2$,
$M=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, is reversible with the unitary involution $C=\operatorname{diag}(1,-1)$: $CMC=M^{-1}$ was verified exactly, and the eigenvalues are the reciprocal pair $\pm i$ with the product $1$; the operator is on the unit-circle stratum, the reversible analogue of an elliptic symmetric periodic orbit.

**Example (a hyperbolic reversible matrix, verified).** The matrix $M=\begin{pmatrix}2&3\\1&2\end{pmatrix}$ with $\det M=1$ is reversible with the same $C$, $CMC=M^{-1}$ verified exactly, and its eigenvalues are the real reciprocal pair $2\pm\sqrt3$, the larger of modulus greater than one and the smaller the reciprocal; the operator is on the real hyperbolic stratum, the reversible analogue of a hyperbolic symmetric orbit, and the pairing of the eigenvector $Cv_\lambda$ is the eigenvector for $\lambda^{-1}$, verified algebraically through the identity $CM=M^{-1}C$.

**Example (a commuting involution, verified).** The diagonal matrix $M=\operatorname{diag}(2,3)$ commutes with $C=\operatorname{diag}(1,-1)$ (checked exactly); the two isotypic blocks are the coordinate lines, the spectrum is the union $\{2\}\cup\{3\}$ of the block spectra, and there is no inversion pairing — the commuting symmetry does not reverse the operator, in contrast with the previous examples.

**Example (a non-reversible matrix, verified).** The matrix $M=\begin{pmatrix}1.5&0.5\\1&1.5\end{pmatrix}$ is **not** reversible with respect to $C=\operatorname{diag}(1,-1)$: the check $CMC=M^{-1}$ fails with error $0.64$, and the eigenvalue product is $1.75$ rather than $1$. Reversibility is a strong condition on an operator and, exactly as for the maps, it must be verified rather than assumed.

**Example (the anti-unitary real structure).** For the conjugation $C$ of complex conjugation on $\mathbb{C}^2$, a real operator $A$ satisfies $CAC=\overline A=A$, so the reversibility $CAC=A^{-1}$ forces $A^2=I$; the involution $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ satisfies $A^2=I$ exactly (checked), and its spectrum $\{+1,-1\}$ is the maximally symmetric real stratum. This is the operator form of the inversion of time, in which the self-adjointness and the anti-unitary reversal force the operator to be an involution.

## Summary

A **reversible operator** is an invertible operator $A$ with a reversing involution $C$, $C^2=\mathrm{id}$, $CAC=A^{-1}$, equivalently $CA=A^{-1}C$; the involution is **unitary** in the reversible case and **anti-unitary** (a conjugation) in the time-reversal case, and the companion structure is a **commuting** involution $\sigma A=A\sigma$. The **spectral theorem** for a reversible operator: the spectrum is invariant under $\lambda\mapsto\lambda^{-1}$, the eigenvalues occur in reciprocal pairs, and the eigenvector $Cv_\lambda$ corresponds to $\lambda^{-1}$ (to $\overline\lambda^{-1}$ in the anti-unitary case, where the spectrum is also conjugation-invariant); the unit circle and the real reciprocal pairs are the invariant strata, and $AC$, $CA$ are involutions with $A=(AC)C$. A **commuting** involution splits the space into the isotypic blocks $H_+\oplus H_-$, preserves the operator, and gives the spectrum as the union of the block spectra; the two structures coexist and compose in parallel with the reversor and the symmetry of the dynamics. In the **anti-unitary** case the conjugation defines a real structure; a real self-adjoint reversible operator is an involution with spectrum in $\{-1,+1\}$. The **dynamical origin** is the Koopman operator of a reversible map, $U_RU_TU_R=U_T^{-1}=U_T^*$, with $C=U_R$, and the Perron–Frobenius operator inherits the reversibility, so the Ruelle–Pollicott resonances of a reversible transfer operator come in reciprocal pairs. The examples verify the elliptic reversible matrix (rotation by $\pi/2$, eigenvalues $\pm i$), the hyperbolic reversible matrix (eigenvalues $2\pm\sqrt3$), the commuting involution (block spectrum $\{2\}\cup\{3\}$), a non-reversible matrix (the check fails), and the anti-unitary real involution ($A^2=I$). The self-adjoint time-reversal operator and the real structure are *Time Reversal and the Transfer Operator*, and the reversing symmetry of the flow operator is *The Involution on the Flow Operator*, both in this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $C$, $CAC=A^{-1}$ | Reversible operator and its reversing involution |
| $C^2=\mathrm{id}$, unitary / anti-unitary | The two kinds of reversing involution |
| $\sigma$, $\sigma A=A\sigma$ | Commuting (equivariant) involution |
| $H_+\oplus H_-$ | Isotypic splitting of the commuting involution |
| $\lambda,\lambda^{-1}$ | Reciprocal eigenvalue pair |
| $AC$, $CA$ | Involutions with $(AC)^2=(CA)^2=\mathrm{id}$, $A=(AC)C$ |
| $H_{\mathbb{R}}=\{u:Cu=u\}$ | Real structure of a conjugation |
| $U_T$, $U_R$, $U_RU_TU_R=U_T^{-1}$ | Koopman operator of a reversible map |
| $P_T=U_T^*$ | Reversible Perron–Frobenius operator |
| $\operatorname{spec}(A^{-1})=\{\lambda^{-1}\}$ | Inversion-invariance of the spectrum |

## Further Reading

- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the spectral theory of bounded operators and the isospectral conjugation.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the unitarity, the anti-unitary operators and the spectral theorem.
- Michael B. Sevryuk, *Reversible Systems* (Springer Lecture Notes in Mathematics 1211, 1986), for the reversible structures and their linear theory.
- John A. G. Roberts and G. R. W. Quispel, "Chaos and time-reversal symmetry. Order and chaos in reversible dynamical systems", *Physics Reports* 216 (1992), 63–177, for the reversible maps and their operator aspects.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the Koopman and the transfer operators and the spectral duality.
- Viviane Baladi, *Positive Transfer Operators and Decay of Correlations* (World Scientific, 2000), for the Ruelle–Pollicott resonances of the transfer operator.
- Fritz Gesztesy, Harald Grosse and Bruno Thaller (eds.), *Recent Developments in Quantum Mechanics* and the standard references on the Krein spaces and the anti-unitary symmetries, for the real and the indefinite structures.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the reversible and the isometric linear structures.
