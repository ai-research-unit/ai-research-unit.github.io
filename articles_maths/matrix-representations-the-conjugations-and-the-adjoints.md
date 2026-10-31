# __Matrix Representations : The Conjugations and the Adjoints__

## Introduction

The biquaternion algebra carries four words: the quaternion conjugation $\natural$, the complex conjugation $\bar{\cdot}$, the Hermitian adjoint $*=\natural\circ\bar{\cdot}$, and the negative adjoint $\flat=-*$. In a matrix display each word becomes a matrix operation, and the operation depends on the display. The coefficient frame is real, so there the words are the plain transpose, the plain entrywise conjugation, the plain dagger and its negative. The spinor model and the Peirce frame are built from complex combinations of the basis, so there the transpose and the entrywise conjugation are *dressed* by a fixed matrix: by $\varepsilon$ in the $2\times2$ model and by $P=-\sigma_2\otimes\sigma_2$ in the Peirce frame. The dagger is undressed in every display.

This article develops the four words, the three displays, the adjugate, the fixed spaces, the four adjoints and the Klein four-group they form. It uses no norm and no module.

**Conventions.** The algebra and the models are those of *Matrix Representations : The Models and the Change of Frame*. The coefficient basis is $(e_t,\vec e_x,\vec e_y,\vec e_z)$. The $2\times2$ model is
$$
\mathsf M_2(\tilde Q)=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix},
$$
and the regular matrix is $I_2\otimes\mathsf M_2(\tilde Q)$ in the Peirce frame. The dressing matrices are
$$
\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
P=-\sigma_2\otimes\sigma_2=
\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$
The Peirce change is $C_{\Pi}$, with columns the four Peirce elements in coefficient coordinates.

**Boundaries.** The four words and the four traces are *Matrix Representations : The Four Words and the Four Traces*; the conjugations as real structures are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the automorphisms that commute with them are *Biquaternion Automorphisms and Derivations*. The $2\times2$ and $4\times4$ source articles are *Matrix Representations : The Conjugations and the Adjoints*.

## Common Aspects

The algebra carries four words: the quaternion conjugation $\natural$, the complex conjugation $\bar{\cdot}$, the Hermitian adjoint $*=\natural\circ\bar{\cdot}$, and the negative adjoint $\flat=-*$. The first is complex linear, the second and third conjugate linear, and the fourth conjugate linear with a sign. The three $\natural$, $\bar{\cdot}$ and $*$ commute, each squares to the identity, and together with the identity they form a Klein four-group. The word $\flat$ squares to the identity too, but it is not an anti-automorphism: it satisfies $\flat(XY)=-\flat(Y)\flat(X)$.

**The fixed spaces.** The fixed space of $\natural$ is the centre $\mathbb{C}e_t$. The fixed space of $\bar{\cdot}$ is the real quaternion subalgebra, of real dimension four. The fixed space of $*$ is the Hermitian subspace and the fixed space of $\flat$ is the anti-Hermitian subspace, both of real dimension four. These are four of the six subspaces of *Matrix Representations : The Six Subspaces as Matrix Conditions*. All fixed spaces are taken inside the image: the ambient operation can fix more, and the difference is the transverse part of the regular model. The ambient transpose, for instance, fixes every symmetric matrix, while inside the image it fixes only the scalars.

**The three displays.** In each display the same four words act as follows.

| Word | Coefficient frame, $4\times4$ | Spinor model, $2\times2$ | Peirce frame, $4\times4$ |
|---|---|---|---|
| $\natural$ | $M^{\mathsf T}$ | $\operatorname{adj}M=\varepsilon M^{\mathsf T}\varepsilon^{-1}$ | $P M^{\mathsf T}P^{-1}$ |
| $\bar{\cdot}$ | $\bar M$ | $\varepsilon\bar M\varepsilon^{-1}$ | $P\bar M P^{-1}$ |
| $*$ | $M^{\dagger}$ | $M^{\dagger}$ | $M^{\dagger}$ |
| $\flat$ | $-M^{\dagger}$ | $-M^{\dagger}$ | $-M^{\dagger}$ |

Two columns are dressings of the first: the spinor model dresses the transpose and the entrywise conjugation by $\varepsilon$, and the Peirce frame dresses them by $P$. The dagger is the same in all three.

**Why the dressing appears.** A change of frame $M_c=S M S^{-1}$ carries the transpose to the conjugation by $S^{-1}S^{-T}$ and the entrywise conjugation to the conjugation by $S^{-1}\overline S$. The coefficient frame has $S=\mathrm I$, so both dressings are trivial. For the Peirce change, $C_{\Pi}^{\mathsf T}C_{\Pi}=\tfrac12 P$ and $C_{\Pi}^{-1}\overline{C_{\Pi}}=P$; the factor two is central and gives the same conjugation as $P$. The dagger is undressed because $C_{\Pi}^{\dagger}C_{\Pi}=\tfrac12\mathrm I_4$ cancels the two dressings. In the spinor model the same computation uses $\varepsilon\varepsilon^{\mathsf T}=\mathrm I_2$.

**The four adjoints.** The four element-level operations switch the four forms. In the entry model the forms are
$$
\tfrac12\operatorname{Tr}(XY),\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y),\qquad
\tfrac12\operatorname{Tr}(XY^{\dagger}),\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y^{\dagger}),
$$
and in the regular model the factor is $\tfrac14$. The first uses no involution, the second uses $\natural$ in the first slot, the third uses $*$ in the second, and the fourth uses both. The word $\flat=-*$ is not among them. These are element-level operations; the adjoint of a linear map with respect to a form is a different object, computed from the Gram matrix, and is not used here.

**The sign of $\flat$.** The word $\flat=-*$ is the negative of the Hermitian word. It squares to the identity but reverses the product only up to sign, so it is the fourth involution and not an anti-automorphism. No change of display changes its sign.

## The Coefficient Frame

**The four words.** In the coefficient frame the basis is real, so the four words are the plain operations: $\natural$ is the transpose $M^{\mathsf T}$, $\bar{\cdot}$ is the entrywise conjugation $\bar M$, $*$ is the dagger $M^{\dagger}=\overline M^{\mathsf T}$, and $\flat$ is $-M^{\dagger}$. No dressing appears. The composition $\natural\circ\bar{\cdot}=\bar{\cdot}\circ\natural=*$ is the identity $\overline{M^{\mathsf T}}=\overline M^{\mathsf T}$.

**The adjugate is cubic.** For $M\in M_4(\mathbb{C})$,
$$
\operatorname{adj}M=N M^{\mathsf T},
\qquad N=\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q),
\qquad \det M=N^2,
$$
where $M^{\mathsf T}$ is the quaternion conjugation. The adjugate is homogeneous of degree three, not linear, and it is not an involution:
$$
\operatorname{adj}(\operatorname{adj}M)=(\det M)^{\,n-2}M,
$$
which for $n=4$ reads $\operatorname{adj}^2M=N^4M$. The adjugate is therefore not a word of the algebra in the regular model; it is a cubic map that agrees with the linear word only in dimension two. Its fixed points are the matrices satisfying $M^2=(\det M)\mathrm I_4$. The image of $i\vec e_x$ is one: its norm is $-1$, its determinant is $1$, and its square is $\mathrm I_4$. The ambient $M_4(\mathbb{C})$ has more fixed points, such as $\operatorname{diag}(1,1,-1,-1)$, which are not in the image.

**The complex conjugation.** The coefficient basis is real, so $\bar{\cdot}$ is entrywise. Its fixed space is the image of the real algebra, a four-real-dimensional subspace of $M_4(\mathbb{R})$, not all of it: the regular matrix has only four real parameters. The anti-fixed space is $i$ times the image.

**The dagger.** The Hermitian adjoint is the plain dagger $M^{\dagger}=\overline M^{\mathsf T}$. Its fixed space is the Hermitian subspace and its anti-fixed space the anti-Hermitian subspace, both four-real-dimensional inside the image. The ambient Hermitian matrices are sixteen-dimensional, but the image carries only the four-dimensional Hermitian part. For every $M$ in the image, $M^{\dagger}M$ is positive semidefinite and is positive definite exactly when $M$ is invertible.

## The Entry Model

**The dressed transpose.** For $M\in M_2(\mathbb{C})$,
$$
\operatorname{adj}M=(\operatorname{Tr}M)\mathrm I_2-M
=\varepsilon M^{\mathsf T}\varepsilon^{-1},
\qquad
\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$
The two formulas are the Cayley–Hamilton identity and the dressed transpose. The adjugate is complex linear, an involution, and its eigenvalues are $+1$ on the centre and $-1$ on the traceless part. Its fixed space is the centre, of complex dimension one, and its anti-fixed space is $\mathfrak{sl}_2(\mathbb{C})$, of complex dimension three.

**The dressed conjugation.** The entry model is not a real display: the image of the real algebra is the quaternion subspace of matrices
$$
\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix},
$$
not the real matrices. The conjugation is therefore
$$
M\longmapsto\varepsilon\bar M\varepsilon^{-1},
$$
the entrywise conjugation followed by the conjugation by $\varepsilon$. The same $\varepsilon$ dresses the transpose.

**The dagger and the sign.** The Hermitian adjoint is the plain dagger $M^{\dagger}$, and $\flat$ is $-M^{\dagger}$. The fixed spaces inside the image are the Hermitian and anti-Hermitian subspaces, of real dimension four each; the ambient $2\times2$ Hermitian matrices are four-real-dimensional as well, so no qualifier about the image is needed here. For $M$ in the image, $M^{\dagger}M$ is positive semidefinite and positive definite exactly when $M$ is invertible.

**The consistency.** The composition $\natural\circ\bar{\cdot}$ is
$$
\varepsilon\,\overline{\varepsilon M^{\mathsf T}\varepsilon^{-1}}\,\varepsilon^{-1}
=\varepsilon\varepsilon^{\mathsf T}\bar M^{\mathsf T}\varepsilon^{-\mathsf T}\varepsilon^{-1}
=\bar M^{\mathsf T}=M^{\dagger},
$$
because $\varepsilon\varepsilon^{\mathsf T}=\mathrm I_2=\varepsilon^{-\mathsf T}\varepsilon^{-1}$. The dressings of the two factors cancel, and the dagger is plain.

## The Peirce Frame

**The Peirce dressing.** In the Peirce frame the transpose and the entrywise conjugation are dressed by
$$
P=-\sigma_2\otimes\sigma_2=
\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},
$$
so $\natural$ is $M\mapsto P M^{\mathsf T}P^{-1}$ and $\bar{\cdot}$ is $M\mapsto P\bar M P^{-1}$. The dagger is still plain. The sign in $P$ is the signed reversal of the four Peirce coordinates: on the basis it exchanges the two mixed units with a sign, $\vec\Upsilon_+\mapsto-\vec\Upsilon_-$ and $\vec\Upsilon_-\mapsto-\vec\Upsilon_+$, and exchanges the two idempotents without a sign. The entrywise conjugation of the Peirce matrix is therefore not the complex conjugation of the element; it is the image of the $\sigma$-involution, the conjugation by $e_y$.

**The adjugate blockwise.** With $M=\mathrm I_2\otimes B$, $B=\mathsf M_2(\tilde Q)$ and $N=\det B$,
$$
\operatorname{adj}M=N\,\bigl(\mathrm I_2\otimes\operatorname{adj}B\bigr)
=\operatorname{diag}(N\operatorname{adj}B,\,N\operatorname{adj}B).
$$
The adjugate respects the block structure: it acts on each spinor plane by the $2\times2$ adjugate, multiplied by the common scalar $N$. On an invertible diagonalisable matrix with eigenvalues $\lambda,\lambda,\mu,\mu$, the adjugate has eigenvalues $\lambda\mu^2$ twice and $\lambda^2\mu$ twice: it separates the two spectral values even when the matrix does not.

**The conjugation and the dagger.** The fixed space of $\bar{\cdot}$ is the image of the real algebra, of real dimension four, and the fixed space of $*$ is the Hermitian subspace, also four-real-dimensional inside the image. The positivity is blockwise:
$$
M^{\dagger}M=\mathrm I_2\otimes B^{\dagger}B,
$$
so the eigenvalues of $M^{\dagger}M$ are those of $B^{\dagger}B$, each repeated twice, and the singular values of $M$ are those of $B$, each repeated twice.

## Summary

The four words are the quaternion conjugation, the complex conjugation, the Hermitian adjoint and its negative. In the coefficient frame they are the transpose, the entrywise conjugation, the dagger and minus the dagger; in the spinor model the transpose and the entrywise conjugation are dressed by $\varepsilon$; in the Peirce frame they are dressed by $P=-\sigma_2\otimes\sigma_2$. The dagger is plain in all three displays. The $2\times2$ adjugate is the linear word $\natural$; the $4\times4$ adjugate is the cubic map $N M^{\mathsf T}$, its fixed space is not the centre, and on the Peirce display it acts blockwise as $N\operatorname{adj}B$. The three words $\natural,\bar{\cdot},*$ form a Klein four-group; the fourth word $\flat=-*$ is the negative of the Hermitian word, and it is the fourth involution of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\natural$ | quaternion conjugation, $Q_te_t-\vec Q$ |
| $\bar{\cdot}$ | complex conjugation of the coefficients |
| $*=\natural\circ\bar{\cdot}$ | Hermitian adjoint |
| $\flat=-*$ | negative adjoint, the fourth word |
| $\varepsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ | the spinor dressing |
| $P=-\sigma_2\otimes\sigma_2$ | the Peirce dressing, the signed reversal |
| $\operatorname{adj}M$ | the adjugate, linear in $2\times2$ and cubic in $4\times4$ |
| $N$ | the quaternionic norm, $\det M=N^2$; the scalar of the cubic adjugate |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the three displays
- [Matrix Representations : The Four Words and the Four Traces](matrix-representations-the-four-words-and-the-four-traces.html), for the four forms and their traces
- [Matrix Representations : Trace, Determinant and the Biquaternion Norm](matrix-representations-trace-determinant-and-the-biquaternion-norm.html), for the determinant and the norm
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms
- [Biquaternion Automorphisms and Derivations](biquaternion-automorphisms-and-derivations.html), for the automorphisms commuting with the words