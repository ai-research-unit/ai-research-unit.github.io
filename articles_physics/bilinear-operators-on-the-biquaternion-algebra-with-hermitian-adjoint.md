# __Bilinear Operators on the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

Every physical statement about a quantum system is a bilinear statement about two amplitudes: a probability is $\langle s|t\rangle$, a polarisation is $\langle s|\sigma_k|t\rangle$, and an observable's matrix element is the same kind of object. This article is the biquaternion instance of the general theory of **bilinear operators on a Clifford module** (*Bilinear Operators on a Clifford Module with Hermitian Adjoint*), and its subject is the completeness of that list of bilinears in the internal space of the framework.

The physical content is one theorem with one consequence. The theorem is the **Fierz identity** of the internal action: the biquaternion algebra is a full matrix algebra, $\mathbb{B}\cong M_2(\mathbb{C})$, so its action on the internal spinor module is an **isomorphism** onto the endomorphisms, and the four **bilinear covariants** of the module — the scalar and the three vector-like covariants — are a basis of the space of internal bilinears. The consequence is that the internal observables are exactly four in number: the probability form and the three components of the Bloch vector, with no fifth independent internal bilinear. In this form the identity is not a technicality of Clifford theory but the statement that **a two-dimensional internal space has a four-dimensional space of bilinears and no more**, the internal counterpart of the completeness of the Pauli basis $I,\sigma_1,\sigma_2,\sigma_3$.

The mathematics is *Bilinear Operators on the Biquaternion Algebra with Hermitian Adjoint*; the module form, its Gram matrix and the Schur uniqueness are *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; the internal Hilbert space and the two sectors are *The Hermitian Subspace M+ as the Informational Sector* and *The Anti-Hermitian Subspace M− as the Material Sector*; the state space, the Bloch ball and the cone are *The Bloch Ball as the Trace-One Slice of the Future Light Cone* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the channel reading of the sandwich is *Completely Positive Maps of the Biquaternion Algebra with Hermitian Adjoint*; the left multiplication as the Clifford action is *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*; and the two-sided operator and its defect are *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*. Nothing owned by those articles is re-derived.

## The Internal Bilinears

**Definition.** The **internal bilinears** of two spinors $s,t$ are the four numbers

$$
b_0(s,t)=s^{\dagger}t,\qquad b_k(s,t)=-i\,s^{\dagger}\sigma_k t ,\qquad k=1,2,3 ,
$$

that is, $b_{\mu}(s,t)=(s,L_{e_{\mu}}t)$ for the four blades $e_0,e_1,e_2,e_3$ and the internal module form $(s,t)=\mathrm{Sc}(s^{\dagger}t)$.

**Physical reading.** $b_0$ is the **probability form**: its diagonal $b_0(s,s)=\lvert s\rvert^2$ is the norm that the Born rule normalises to one, and its off-diagonal is the transition amplitude $\langle s|t\rangle$ of the fidelity and of *Exercise — the Bloch Ball and the Geometry of Mixed States*. The three $ib_k(s,s)$ are real and form the vector $\tilde T=s^{\dagger}\boldsymbol{\sigma}s$, the **Bloch vector** or internal polarisation of the spinor; the density matrix of the state is $\rho=\tfrac12(e_0+i T_k e_k)$, Hermitian of trace one, and the four covariants of the state are its probability and its three polarisation components. So the four internal bilinears of a state are not four abstract forms but the four numbers by which the state is known: the trace and the Bloch vector.

## The Fierz Identity as the Completeness of the Internal Observables

**Theorem (completeness).** The action of the algebra on the internal spinor module is an isomorphism $L:\mathbb{B}\to\mathrm{End}_{\mathbb{C}}(S)$, and the four covariants $b_{\mu}$ are a basis of the space of internal bilinears; every internal bilinear is a unique combination $\sum_{\mu}c_{\mu}b_{\mu}$ with the coefficients $c_{\mu}=\frac12\mathrm{Tr}(e_{\mu}^{\dagger}M)$ of the matrix $M$ of the bilinear.

*Proof.* The mathematics article proves it: $\mathbb{B}\cong M_2(\mathbb{C})$ acts faithfully on $S=\mathbb{C}^2$, the dimensions agree, and the blades $\{I,\sigma_1,\sigma_2,\sigma_3\}$ are a basis of $M_2(\mathbb{C})$, orthogonal for the trace form.

**Physical reading (no fifth internal observable).** The theorem says that the internal observable algebra is exactly $M_2(\mathbb{C})$ and that its bilinear basis is the identity together with the three Pauli directions. Any two-amplitude quantity of the internal space — a probability, a polarisation, an interference term, a matrix element of any internal observable — is one of these four, because there is no room in a four-dimensional space of bilinears for an independent fifth. Read negatively, this is the statement that the internal space hosts no hidden observable beyond the Bloch vector: a proposed internal observable that is not a combination of the identity and the three Pauli matrices is not an observable of the algebra but an element adjoined to it. The claim is the internal, two-dimensional analogue of the spin-statistics article's use of the Pauli basis and it is the reason the density matrix of the framework is exhausted by the Bloch ball of *The Bloch Ball as the Trace-One Slice of the Future Light Cone*.

**Physical reading (the Fierz rearrangement).** The expansion coefficients of a bilinear in the covariant basis are the **Fierz coefficients**, and the rearrangement is a change of basis in the four-dimensional bilinear space: a two-amplitude object written in the matrix units is the same object written in the identity and the Pauli directions. For an internal interaction vertex this is the internal Fierz rearrangement — the rewriting of an internal bilinear in the covariant basis — and the exactness of the theorem means that in the internal space the rearrangement has four terms and no more, with the coefficients computed by the orthogonality of the blades.

## Invariance: The Born Rule Forced by the Internal Symmetry

**Theorem (the unique invariant bilinear).** Under the internal slice $U=U(2)$ the covariants transform as $b_{\mu}(\tilde As,\tilde At)=b_{\tilde A^{\dagger}e_{\mu}\tilde A}(s,t)$; the scalar covariant $b_0$ is **invariant**, the three skew covariants rotate among themselves by the adjoint representation of $SO(3)$, and the invariants of the whole bilinear space are the multiples of $b_0$.

*Proof.* The mathematics article proves it; the invariance is $\tilde A^{\dagger}\Phi(e_0)\tilde A=\tilde A^{\dagger}\tilde A=I$ and the triplet statement is $\tilde A^{\dagger}\sigma_k\tilde A=R_{kl}\sigma_l$ with $R\in SO(3)$.

**Physical reading.** Two statements of the framework are one statement here. First, **the Born rule is the unique internal bilinear compatible with the internal symmetry**: the probability form is the only bilinear pairing fixed by the whole internal slice, up to the normalisation, so the internal group forces the probability rule rather than merely permitting it, and the free scalar is the normalisation convention and not a physical parameter. Second, the three polarisation components form a **vector** under the internal group: they are the triplet of the adjoint representation of $SO(3)\cong SU(2)/\mathbb{Z}_2$, and the scalar is the singlet. The four internal bilinears are therefore the decomposition $\mathbf{1}\oplus\mathbf{3}$ of the internal bilinear space under the internal symmetry group, which is the algebraic form of the statement that a spin state has a scalar (its norm) and a vector (its polarisation).

**Remark (the transitivity of the state space).** The invariant structure is exactly what the Bloch-ball picture needs: the internal group acts transitively on the pure states of the Bloch sphere and by the rotation on the Bloch ball, the scalar being preserved and the vector rotated; the reader comparing with *The Bloch Ball as the Trace-One Slice of the Future Light Cone* will find there the geometry of the same four numbers and here their bilinear origin.

## The Slice, the Boost and the Defect

**Theorem (off the slice).** For an invertible amplitude $\tilde{Q}$ the transformation of the internal bilinears is the two-sided operator, and the bilinear it replaces $b$ by is $b\circ(\tilde{Q}\times\tilde{Q})$; the slice $U(2)$ is exactly the locus on which the covariants are permuted by a conjugation and the bilinears preserved.

*Proof.* The covariants transform by $b_{\mu}(\tilde{Q}s,\tilde{Q}t)=b_{\tilde{Q}^{\dagger}e_{\mu}\tilde{Q}}(s,t)$ precisely by the adjointness of the action, which is the two-sided operator with the parameter $\tilde{Q}^{\dagger}e_{\mu}\tilde{Q}$; the invariance of the bilinear space requires $\tilde{Q}^{\dagger}\tilde{Q}=e_0$, namely the slice. The failure off the slice is the right multiplication by $\tilde{Q}\tilde{Q}^{\dagger}$, the horizontal defect of *Mixed Inner Conjugation and Hermitian Adjoint*, with the amplification read as positivity in *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

**Physical reading.** A rotation of the internal group is a symmetry of the internal bilinears and preserves them; a **boost** is not. A boost carries $\tilde{Q}$ outside the internal slice, conjugates the four covariants by the two-sided operator of *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, and rescales the probability form by $\tilde{Q}\tilde{Q}^{\dagger}$: the amplification is the horizontal defect of *Mixed Inner Conjugation and Hermitian Adjoint* read physically, and it is the covariant statement of the fact that the Lorentz group does not act unitarily on the internal space, only its compact subgroup $SU(2)$ does. So the internal bilinears are Lorentz-covariant objects whose scalar part is the internal probability and whose transformation law is that of the internal observables under the two-sided operator, not under a unitary representation.

**Remark (the null cone is invisible to the internal bilinears).** The scalar covariant is built from the positive definite module form and not from the interval form $N$: it never vanishes on a nonzero spinor, whereas the interval form vanishes on the null cone. Hence no internal bilinear detects the null directions of the material sector. A spinor of vanishing biquaternion norm still has a nonzero probability form and a well-defined Bloch vector; the null cone of the algebra is a property of the interval form of the material sector, not of the internal observables. This is the covariant form of the positivity article's separation of the dagger form from the interval form, and it is the reason the null cone cannot be read off from the internal state.

## Honest Limits

The completeness theorem is exact in the internal space and does not extend to the ambient Dirac space. The internal bilinears are four in number because the internal spinor is two-dimensional; the sixteen Dirac bilinears of four dimensions — scalar, vector, tensor, axial vector and pseudoscalar — live in the ambient Clifford algebra $\mathrm{Cl}_{1,3}$ and not in $\mathbb{B}$, and they are not obtained by adjoining the internal ones. The Fierz rearrangement of the internal space is a four-term rearrangement; the four-dimensional Fierz rearrangement of the Dirac bilinears is a statement about the ambient algebra and is not proved here. The identification of the internal bilinears with the physical probability and the physical polarisation is the dictionary of *The Hermitian Subspace M+ as the Informational Sector* and is a hypothesis of the series, not a consequence of the algebra.

## Summary

The **internal bilinears** of the biquaternion framework are the scalar $b_0(s,t)=s^{\dagger}t$ and the three $b_k(s,t)=-i s^{\dagger}\sigma_kt$; physically they are the probability form and the three components of the Bloch vector, so the four bilinears of a state are exactly the trace and the polarisation by which the state is known. The **Fierz identity** — the action of $\mathbb{B}\cong M_2(\mathbb{C})$ on its spinor module is an isomorphism onto the endomorphisms — makes the four covariants a **basis** of the internal bilinear space, so the internal observables are the identity and the three Pauli directions and no fifth independent internal observable exists; the expansion coefficients are the **Fierz coefficients**, and the internal Fierz rearrangement is a four-term change of basis. This is the internal analogue of the completeness of the Pauli basis and the reason the density matrix is exhausted by the Bloch ball. Under the internal slice $U(2)$ the scalar covariant is **invariant** and the three skew covariants rotate as an $SO(3)$ triplet, so the internal bilinears decompose as $\mathbf{1}\oplus\mathbf{3}$ and the **Born rule is the unique invariant bilinear** of the internal space; the free scalar is the normalisation and not a parameter. A boost lies outside the slice, conjugates the covariants by the two-sided operator and rescales the probability form by $\tilde{Q}\tilde{Q}^{\dagger}$, so the internal bilinears are covariant, not invariant, under the Lorentz group, and only the compact subgroup $SU(2)$ acts unitarily. The scalar covariant never vanishes on a nonzero spinor, so no internal bilinear sees the null cone of the interval form of the material sector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $b_0(s,t)=s^{\dagger}t$ | The scalar covariant; the probability form, positive definite |
| $b_k(s,t)=-i\,s^{\dagger}\sigma_kt$ | The three skew covariants; the polarisation components |
| $T_k=i\,b_k(s,s)=s^{\dagger}\sigma_ks$ | The Bloch vector of a spinor |
| $\rho=\tfrac12(e_0+i T_ke_k)$ | The density matrix of the state; Hermitian of trace one |
| $\mathbb{B}\cong\mathrm{End}_{\mathbb{C}}(S)$ | Completeness: the action is onto the internal endomorphisms |
| $c_{\mu}=\frac12\mathrm{Tr}(e_{\mu}^{\dagger}M)$ | The Fierz coefficients of an internal bilinear |
| $b_0$ invariant, $(b_k)$ by $SO(3)$ | The $\mathbf{1}\oplus\mathbf{3}$ splitting under the internal slice |
| $\tilde{Q}\notin U(2)$: $b\mapsto b\circ(\tilde{Q}\times\tilde{Q})$ | The boost: the covariants by the two-sided operator |

## Further Reading

- F. J. Ynduráin, *Relativistic Quantum Mechanics and Introduction to Field Theory* (Springer, 1996), for the Dirac bilinears, their completeness and the Fierz rearrangement.
- Claude Cohen-Tannoudji, Bernard Diu and Franck Laloë, *Quantum Mechanics*, Vol. 1 (Wiley, 1977), for the density matrix, the Pauli basis and the Bloch representation of a two-level system.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 10th anniversary ed. 2010), for the Bloch ball, the Pauli transfer matrix and the observable basis of a channel.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the completeness of the Clifford action and the invariant forms of a spinor module.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the bilinear covariants of a spinor module and the Fierz identity.
