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

**Boundaries.** The four words and the four traces are *Matrix Representations : The Four Words and the Four Traces*; the conjugations as real structures are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the automorphisms that commute with them are *Biquaternion Automorphisms and Derivations*. The $2\times2$ and $4\times4$ source articles are *Matrix Representations : The Conjugations and the Adjoints* and *Matrix Representations : The Conjugations and the Adjoints*.

## The Four Words

**The definitions.** For $\tilde Q=Q_te_t+\vec Q$,
$$
\tilde Q^{\natural}=Q_te_t-\vec Q,
\qquad
\bar{\tilde Q}=\bar Q_te_t+\bar{\vec Q},
\qquad
\tilde Q^{*}=\bar{\tilde Q}^{\natural}=\bar Q_te_t-\bar{\vec Q},
\qquad
\tilde Q^{\flat}=-\tilde Q^{*}.
$$
The first is complex linear, the second and third are conjugate linear, and the fourth is conjugate linear with a sign. The three $\natural$, $\bar{\cdot}$ and $*$ commute, and each squares to the identity; together with the identity they form a Klein four-group. The word $\flat$ also squares to the identity, but it is not an anti-automorphism: it satisfies $\flat(XY)=-\flat(Y)\flat(X)$.

**The anti-automorphisms.** The words $\natural$, $\bar{\cdot}$ and $*$ are anti-automorphisms of the algebra, and $\flat$ is not. The four are the four involutions of the algebra; the sign in $\flat$ is the sign that distinguishes it from the Hermitian word.

**The fixed spaces.** The fixed space of $\natural$ is the centre $\mathbb{C}e_t$. The fixed space of $\bar{\cdot}$ is the real quaternion subalgebra, the algebra read with real coefficients, of real dimension four; in the $2\times2$ display it is the set of matrices $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$. The fixed space of $*$ is the image of the Hermitian subspace, of real dimension four in both displays; the fixed space of $\flat$ is the image of the anti-Hermitian subspace, of the same dimension. In the ambient $M_4(\mathbb{C})$ the Hermitian matrices form a space of real dimension sixteen, but only a four-dimensional part of it lies in the image. The four fixed spaces are the centre, the quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace: four of the six subspaces of *Matrix Representations : The Six Subspaces as Matrix Conditions*. All fixed spaces in this article are taken inside the image; the ambient operation can fix more, and the difference is the transverse part of the regular model. For example, the ambient transpose fixes every symmetric matrix, while inside the image it fixes only the scalars.

## The Three Displays

**The table.** In each display the same four words act as follows.

| Word | Coefficient frame, $4\times4$ | Spinor model, $2\times2$ | Peirce frame, $4\times4$ |
|---|---|---|---|
| $\natural$ | $M^{\mathsf T}$ | $\operatorname{adj}M=\varepsilon M^{\mathsf T}\varepsilon^{-1}$ | $P M^{\mathsf T}P^{-1}$ |
| $\bar{\cdot}$ | $\bar M$ | $\varepsilon\bar M\varepsilon^{-1}$ | $P\bar M P^{-1}$ |
| $*$ | $M^{\dagger}$ | $M^{\dagger}$ | $M^{\dagger}$ |
| $\flat$ | $-M^{\dagger}$ | $-M^{\dagger}$ | $-M^{\dagger}$ |

The table is the whole content of the article. Two columns are dressings of the first: the spinor model dresses the transpose and the entrywise conjugation by $\varepsilon$, and the Peirce frame dresses them by $P$. The dagger is the same in all three.

**Why the dressing appears.** A change of frame $M_c=S M S^{-1}$ carries the transpose to the conjugation by $S^{-1}S^{-T}$, and the entrywise conjugation to the conjugation by $S^{-1}\overline S$. The coefficient frame has $S=\mathrm I$, so both dressings are trivial. For the Peirce change, $C_{\Pi}^{\mathsf T}C_{\Pi}=\tfrac12 P$, so the transpose is dressed by $2P$, which gives the same conjugation as $P$ because the factor two is central; and $C_{\Pi}^{-1}\overline{C_{\Pi}}=P$, so the entrywise conjugation is dressed by $P$ exactly. For the dagger, the unitarity of $C_{\Pi}$ up to scale, $C_{\Pi}^{\dagger}C_{\Pi}=\tfrac12\mathrm I_4$, cancels the two dressings and leaves the plain dagger.

**The consistency.** The three dressings are compatible with the words: in every display $\natural\circ\bar{\cdot}=\bar{\cdot}\circ\natural=*$. In the spinor model the composition is $\varepsilon\varepsilon^{\mathsf T}\bar M^{\mathsf T}\varepsilon^{-\mathsf T}\varepsilon^{-1}=\bar M^{\mathsf T}$ because $\varepsilon\varepsilon^{\mathsf T}=\mathrm I_2=\varepsilon^{-\mathsf T}\varepsilon^{-1}$; in the Peirce frame the same computation uses $P^2=\mathrm I_4$. In the coefficient frame the two operations are already plain. The sign in $\flat$ is the only place where the displays could differ, and they do not.

## The Adjugate

**The $2\times2$ adjugate is linear.** For $M\in M_2(\mathbb{C})$,
$$
\operatorname{adj}M=(\operatorname{Tr}M)\mathrm I_2-M
=\varepsilon M^{\mathsf T}\varepsilon^{-1}.
$$
The two formulas are the Cayley–Hamilton identity and the dressed transpose. The adjugate is therefore complex linear, an involution, and its eigenvalues are $+1$ on the centre and $-1$ on the traceless part. Its fixed space is the centre, of complex dimension one, and its anti-fixed space is $\mathfrak{sl}_2(\mathbb{C})$, of complex dimension three.

**The $4\times4$ adjugate is cubic.** For $M\in M_4(\mathbb{C})$,
$$
\operatorname{adj}M=N M^{\mathsf T},
\qquad N=\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q),
\qquad \det M=N^2,
$$
in the coefficient frame, where $M^{\mathsf T}$ is the quaternion conjugation. It is homogeneous of degree three, not linear, and it is not an involution: for every $n\times n$ matrix,
$$
\operatorname{adj}(\operatorname{adj}M)=(\det M)^{\,n-2}M,
$$
which for $n=4$ reads $\operatorname{adj}^2M=N^4M$. The adjugate is therefore not a word of the algebra in the $4\times4$ model; it is a cubic map that happens to agree with the linear word only in dimension two.

**The fixed space is not the centre.** In the $2\times2$ model the fixed space of the adjugate is the centre. In the $4\times4$ model it is larger: for invertible $M$,
$$
\operatorname{adj}M=(\det M)M^{-1},
$$
so the fixed points are the matrices satisfying $M^2=(\det M)\mathrm I_4$. The image of $i\vec e_x$ is one: its norm is $-1$, its determinant is $1$, and its square is $\mathrm I_4$. The ambient $M_4(\mathbb{C})$ has still more fixed points, such as $\operatorname{diag}(1,1,-1,-1)$, which are not in the image.

**The Peirce display.** In the Peirce frame $M=I_2\otimes B$ with $B=\mathsf M_2(\tilde Q)$ and $N=\det B$, and
$$
\operatorname{adj}M=N\,\bigl(\mathrm I_2\otimes\operatorname{adj}B\bigr)
=\operatorname{diag}(N\operatorname{adj}B,\,N\operatorname{adj}B).
$$
The adjugate respects the block structure: it acts on each spinor plane by the $2\times2$ adjugate, multiplied by the common scalar $N$. In the same frame the word $\natural$ is the signed reversal $P$ applied on both sides, and on the basis it exchanges the two mixed units with a sign.

**The eigenbasis reading.** On an invertible diagonalisable matrix with eigenvalues $\lambda_1,\dots,\lambda_n$, the adjugate has eigenvalues $(\det M)/\lambda_i$, the product of the other $n-1$ eigenvalues. In the $2\times2$ model this is the exchange $\lambda_1\leftrightarrow\lambda_2$. In the $4\times4$ model with the doubled spectrum $\lambda,\lambda,\mu,\mu$ it is the value $\lambda\mu^2$ twice and $\lambda^2\mu$ twice: the adjugate separates the two spectral values even when the matrix does not.

## The Complex Conjugation

**The coefficient frame.** The coefficient basis is real, so the complex conjugation of an element is the entrywise conjugation of its matrix. The fixed space is the image of the real algebra, a real subspace of $M_4(\mathbb{R})$ of real dimension four; the ambient $M_4(\mathbb{R})$ is sixteen-dimensional, and the image is the four-dimensional part cut out by the regular structure. The anti-fixed space is $i$ times the image.

**The spinor model.** The $2\times2$ model is not a real display: the image of the real algebra is the quaternion subspace of matrices $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$, not the real matrices. The conjugation is therefore the dressed operation
$$
M\longmapsto\varepsilon\bar M\varepsilon^{-1},
$$
which is the entrywise conjugation followed by the conjugation by $\varepsilon$. The dressing is the matrix of the conjugation on the spinor basis; it is the same $\varepsilon$ that dresses the transpose.

**The Peirce frame.** The Peirce basis is also not real, and the conjugation is dressed by the same signed reversal:
$$
M\longmapsto P\bar M P^{-1}.
$$
The two mixed units are exchanged with a sign, $\vec\Upsilon_+\mapsto-\vec\Upsilon_-$ and $\vec\Upsilon_-\mapsto-\vec\Upsilon_+$, while the two idempotents are exchanged without a sign. The entrywise conjugation of the Peirce matrix is not the complex conjugation of the element: it is the image of the $\sigma$-involution, the conjugation by $e_y$.

**The real form.** In every display the fixed space of the conjugation is the image of the real algebra, of real dimension four. In the $4\times4$ coefficient frame it is a four-dimensional subspace of $M_4(\mathbb{R})$, not all of it: the regular matrix has only four real parameters. In the $2\times2$ display it is the quaternion subspace of matrices $\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$. The real algebra is the same in the three displays; only the matrix description of its elements changes.

## The Hermitian Adjoint

**The plain dagger.** The Hermitian adjoint is the transpose of the entrywise conjugate, and it is the same operation in the three displays:
$$
M^{*}=M^{\dagger}=\overline{M}^{\mathsf T}.
$$
The reason is that the three bases are adapted to the Hermitian form: the coefficient basis has real structure constants and $e_t^{*}=e_t$, $\vec e_k^{*}=-\vec e_k$; the $2\times2$ display uses the standard orthonormal basis of $\mathbb{C}^2$; and the Peirce basis satisfies $C_{\Pi}^{\dagger}C_{\Pi}=\tfrac12\mathrm I_4$.

**The fixed and anti-fixed spaces.** The fixed space of the dagger inside the image is the image of the Hermitian subspace, of real dimension four; the anti-fixed space is the image of the anti-Hermitian subspace, of the same real dimension. The two are related by multiplication by $i$, and the negative adjoint $\flat$ has them exchanged. In the ambient $M_4(\mathbb{C})$ the Hermitian matrices are sixteen-dimensional, but the image carries only the four-dimensional Hermitian part.

**The positivity.** For every $M$ in the image, $M^{\dagger}M$ is positive semidefinite, and it is positive definite exactly when $M$ is invertible. Since $M=I_2\otimes B$, $M^{\dagger}M=I_2\otimes B^{\dagger}B$: the eigenvalues of $M^{\dagger}M$ are those of $B^{\dagger}B$, each repeated twice, and the singular values of $M$ are those of $B$, each repeated twice.

## The Four Adjoints

**The four forms.** The four element-level operations are the switches of the four forms. In the $2\times2$ display the four forms are
$$
\tfrac12\operatorname{Tr}(XY),\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y),\qquad
\tfrac12\operatorname{Tr}(XY^{\dagger}),\qquad
\tfrac12\operatorname{Tr}(\operatorname{adj}X\,Y^{\dagger}),
$$
and in the $4\times4$ display the factor is $\tfrac14$. The first form uses no involution, the second uses the word $\natural$ in the first slot, the third uses $*$ in the second slot, and the fourth uses both. The four switches are the four combinations: neither slot, the first slot only, the second slot only, and both slots. The fourth word $\flat=-*$ is not among them.

**The element-level and operator-level adjoints.** The adjugate and the dagger are element-level operations on the entries of a matrix. The adjoint of a linear map is a different object: it is the map $T^{\varphi}$ defined by $\varphi(Tx,y)=\varphi(x,T^{\varphi}y)$, and it depends on the Gram matrix of the form. The two notions are related by the Gram matrix, and the operator-level adjoints are computed in *The Four Adjoints of the Biquaternion Algebra in Examples*. This article uses the word "adjoint" in the element-level sense only.

**The sign of $\flat$.** The word $\flat=-*$ is the negative of the Hermitian word. It satisfies $\flat^2=\mathrm{id}$ but $\flat(XY)=-\flat(Y)\flat(X)$, so it is not an anti-automorphism of the algebra; it is the fourth involution, and it is the sign of the negative Hermitian form. No change of display changes its sign.

## The Klein Group

**The group.** The three anti-automorphisms $\natural$, $\bar{\cdot}$ and $*$ commute and square to the identity, so
$$
\{\mathrm{id},\natural,\bar{\cdot},*\}
\cong(\mathbb{Z}/2)\times(\mathbb{Z}/2).
$$
In the matrix display the group is
$$
\{\mathrm{id},\,E\,\cdot^{\mathsf T}E^{-1},\,E\,\bar{\cdot}\,E^{-1},\,\cdot^{\dagger}\},
\qquad E=\mathrm I,\ \varepsilon,\ P,
$$
with $E=\mathrm I$ in the coefficient frame, $E=\varepsilon$ in the spinor model and $E=P$ in the Peirce frame.

**The action on the centre and on the vector part.** Every word fixes the centre, and the three nontrivial words act on the vector part by
$$
\natural:\vec Q\mapsto-\vec Q,
\qquad
\bar{\cdot}:\vec Q\mapsto\bar{\vec Q},
\qquad
*:\vec Q\mapsto-\bar{\vec Q}.
$$
The Klein group is therefore the group of sign changes and conjugations of the three vector coordinates. The fourth word $\flat$ is the product of $*$ with the scalar $-1$.

**The invariant subspaces.** The fixed space of $\natural$ is the centre; the fixed space of $\bar{\cdot}$ is the quaternion subspace; the fixed space of $*$ is the Hermitian subspace; the fixed space of $\flat$ is the anti-Hermitian subspace. The anti-fixed spaces are the vector subspace, the anti-quaternion subspace, the anti-Hermitian subspace and the Hermitian subspace. The six distinct spaces among the eight are the six subspaces of *Matrix Representations : The Six Subspaces as Matrix Conditions*, and the Klein group permutes them.

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
- [Matrix Representations : The Conjugations and the Adjoints](matrix-representations-the-conjugations-and-the-adjoints.html), for the $2\times2$ source
- [Matrix Representations : The Conjugations and the Adjoints](matrix-representations-the-conjugations-and-the-adjoints.html), for the $4\times4$ source
