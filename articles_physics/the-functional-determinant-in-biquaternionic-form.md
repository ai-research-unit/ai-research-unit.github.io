# __The Functional Determinant in Biquaternionic Form__

## Introduction

The **functional determinant** is what a Gaussian functional integral leaves behind. Integrating out a field with quadratic operator $S''$ produces the factor
$$
\big(\det S''\big)^{-1/2},
$$
and the one-loop effective action of the previous article is its logarithm,
$$
\Gamma_1 = \tfrac12\,\mathrm{Tr}\log S'' .
$$
The determinant is a formal infinite product of the operator's eigenvalues, and its meaning depends on a regularization: the product diverges in the continuum, and the physical content lies in its regularized, renormalized value. This article asks what the biquaternion algebra $\mathbb{B}$ contributes to the determinant, and it separates the contributions that are the algebra's from the regularization that is not.

The findings are these.

- **Established (algebra): the fundamental determinant is the norm form.** In the isomorphism $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ the determinant of the image of $\tilde Q$ is the scalar part of the norm form,
$$
\det\Phi(\tilde Q) = \mathrm{Sc}\big(\tilde Q\bar{\tilde Q}\big) = N(\tilde Q),
$$
a central scalar. Left multiplication and right multiplication by $\tilde Q$ on $\mathbb{B}$ regarded as a four-complex-dimensional space therefore have the same determinant, the square of the fundamental one:
$$
\det\big(L_{\tilde Q}\big) = \det\big(R_{\tilde Q}\big) = N(\tilde Q)^2 .
$$
This is the framework's algebraic determinant; it is checked below and it is the reason the norm form, and not an auxiliary object, is the determinant of an algebra element.
- **Established (algebra): the module determinant is a square.** A biquaternion field's fluctuation operator acts on a two-complex-dimensional fibre per mode, and for a central operator $S''=\kappa e_0$ the determinant on that fibre is the square of the operator's value on a single complex dimension,
$$
\det\big(S''\big)\Big|_{\text{module}} = \kappa^2 ,
$$
the exponent being the module's complex dimension. The determinant on the whole algebra, which is four-complex-dimensional, would be $\kappa^4$; the framework's determinant is defined once the module is chosen, and the module is fixed by the algebra. When $S''$ is not central — the chirality-off-diagonal Dirac mass is the example — the two chiralities mix and the determinant does not factor.
- **Standard, and transcribed.** The zeta-function regularization
$$
\log\det S'' = -\zeta_{S''}'(0),
\qquad
\zeta_{S''}(s) = \sum_n \lambda_n^{-s},
$$
the heat-kernel and Seeley–DeWitt expansion that evaluates $\zeta(0)$ and $\zeta'(0)$, and the proper-time representation. None of these is the algebra's; the algebra supplies the operator on which they act.
- **The physical faces.** Two structural consequences are recorded here because later articles use them: the **phase** of a non-Hermitian determinant (the fermion determinant of a chiral or $\theta$-dependent operator) is the framework's route to the $\theta$ vacuum of *The Theta Vacuum in Biquaternionic Form*, and the **conformal variation** of the determinant is the trace anomaly of *The Trace Anomaly in Biquaternionic Form*.

The article proceeds as follows. A section defines the determinant of a module operator and the fundamental determinant of an algebra element. A section proves the regular-representation identity and verifies it. A section connects the determinant to the Gaussian integral and the one-loop action. A section treats regularization, and a section the fermionic determinant and its phase. A section treats the conformal variation, and a section separates what is established from what is interpretation.

**Conventions.** We use those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$; the isomorphism is $\Phi(e_k)=-i\sigma_k$; the norm form is $N(\tilde Q)=\tilde Q\bar{\tilde Q}\in\mathbb{C}_{\mathbb{B}}$; the trace is $\mathrm{Tr}(\tilde X)=2\mathrm{Sc}(\tilde X)$; the real bilinear form is $\langle\tilde X,\tilde Y\rangle=\mathrm{Re}\,\mathrm{Tr}(\tilde X^\dagger\tilde Y)$, positive on $\mathbb{M}_+$ and negative on $\mathbb{M}_-$; the sectors are $\mathbb{M}_-$ (anti-Hermitian) and $\mathbb{M}_+$ (Hermitian). The central kinetic operator is $\tilde K=\Box-m^2$ with $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial_{ict}^2+\Delta$, and the wave biquaternion is $\tilde k=iEe_0+\mathbf{p}$ with $\tilde k\bar{\tilde k}=-p^2$. The Dirac operator and its mass term are linear and chirality-off-diagonal, $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\bar{\tilde\nabla}\tilde\Psi_L=m\tilde\Psi_R$, as *Conventions in the Biquaternion Universe* fixes.

## The Determinant of a Module Operator

Let $S''$ be a linear operator on the biquaternion module, and suppose for the moment that its spectrum is discrete and its determinant exists. Then
$$
\det S'' = \prod_n \lambda_n ,
\qquad
\log\det S'' = \sum_n \log\lambda_n = \mathrm{Tr}\log S'' ,
$$
the second equality making sense on the principal branch. The operator acts on the module $\mathbb{B}P_+(\hat{\boldsymbol\mu})\cong\mathbb{C}^2$ per mode, so each $\lambda_n$ is a two-fold object: the module contributes two complex dimensions, and the determinant is taken over both.

**The central case.** If $S''=\kappa\,e_0$ is a central scalar (for instance the free kinetic operator at a given mode, $\kappa=\tilde k\bar{\tilde k}+m^2=\mathcal{M}(\tilde k)$, whose Lorentzian continuation differs from the action's operator $\Box-m^2$ only by the overall sign that the module's even dimension absorbs), then on the module it is multiplication by $\kappa$ on $\mathbb{C}^2$, and
$$
\det\big(\kappa\,e_0\big)\Big|_{\text{module}} = \kappa^2 .
$$
The factor $\kappa^2$ is the module's two complex dimensions; equivalently, the central eigenvalue contributes once per complex dimension. On the algebra itself, regarded as a four-complex-dimensional space, multiplication by $\kappa$ has determinant $\kappa^4$, and the two are related by the change of the space on which the determinant is taken. The framework's determinant is thus defined once the module is chosen, and the module is fixed by the algebra.

**The non-central case.** If $S''$ is not central, it mixes the two chiralities (the minimal left ideals) and the determinant does not factor. The mass term's right-multiplication form is the standard instance: the Dirac operator
$$
\mathcal{D} = \tilde\nabla + \tilde m ,
$$
with $\tilde m$ implementing the chirality-off-diagonal mass, is a module operator whose determinant carries both a magnitude and a **phase**; the phase is the physically new object and is treated in a later section. The general principle is that the determinant of a central operator is a product of scalars and the determinant of a non-central one is not.

## The Fundamental Determinant and the Norm Form

The determinant of a *single* algebra element is an algebraic quantity, and it turns out to be the norm form.

**Proposition.** For every $\tilde Q\in\mathbb{B}$,
$$
\det\Phi(\tilde Q) = \mathrm{Sc}\big(\tilde Q\bar{\tilde Q}\big) = N(\tilde Q),
$$
where $\Phi$ is the isomorphism onto $M_2(\mathbb{C})$ and $N$ is the norm form.

**Proof.** Both sides are polynomial functions of the four coefficients of $\tilde Q$, so it suffices to check on a basis. On $\Phi(e_0)=I_2$ both sides are $1$; on $\Phi(e_k)=-i\sigma_k$, $\det(-i\sigma_k)=1$ while $N(e_k)=e_k\bar e_k=-e_k^2=e_0$, giving $1$; and both sides are multiplicative, $\det(\Phi(\tilde A)\Phi(\tilde B))=\det\Phi(\tilde A)\det\Phi(\tilde B)$ and $N(\tilde A\tilde B)=\tilde A\tilde B\overline{\tilde A\tilde B}=\tilde A\,N(\tilde B)\,\bar{\tilde A}=\tilde A\bar{\tilde A}\,N(\tilde B)=N(\tilde A)N(\tilde B)$ using the centrality of $N(\tilde B)$. A basis check plus multiplicativity on a generating set establishes the identity on the whole algebra. $\square$

The determinant of $\tilde Q$ is thus the **norm form**, the same object that supplies the Minkowski interval of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*.

**Proposition (regular representation).** Left multiplication $L_{\tilde Q}:X\mapsto\tilde QX$ and right multiplication $R_{\tilde Q}:X\mapsto X\tilde Q$ on $\mathbb{B}$ regarded as a four-complex-dimensional space both have determinant
$$
\det L_{\tilde Q} = \det R_{\tilde Q} = N(\tilde Q)^2 .
$$

**Proof.** Under the isomorphism $\Phi$, left multiplication becomes left multiplication by the matrix $P=\Phi(\tilde Q)$ on $M_2(\mathbb{C})$, which is $P\otimes I_2$ in the basis $E_{ij}$ of matrix units; its determinant is $(\det P)^2$. Right multiplication becomes right multiplication by $P$, which is $I_2\otimes P^T$ in the same basis, with the same determinant $(\det P)^2$. By the previous proposition $\det P=N(\tilde Q)$, so both determinants equal $N(\tilde Q)^2$. $\square$

**Verification.** With $\tilde Q=(0.7+0.2i,\,0.3-0.5i,\,-0.2+0.4i,\,0.1+0.6i)$ in the basis $(e_0,e_1,e_2,e_3)$, the $2\times2$ representation gives
$$
\det\Phi(\tilde Q) = -0.180000-0.060000\,i = \mathrm{Sc}\big(\tilde Q\bar{\tilde Q}\big),
$$
to the accuracy shown, confirming the first proposition, and the $4\times4$ left and right multiplication matrices give
$$
\det L_{\tilde Q} = 0.0288000+0.0216000\,i = \det R_{\tilde Q} = \big(\det\Phi(\tilde Q)\big)^2 ,
$$
confirming the second. The eigenvalues of $\Phi(\tilde Q)$ are $1.520333+0.407233i$ and $-0.120333-0.007233i$, whose product is $-0.18-0.06i$, as required.

**Interpretation of the result.** The determinant of an element of the framework's algebra is the norm form, so a vanishing determinant — a zero divisor — is a vanishing norm, i.e. an element of the zero-divisor cone. This is the algebraic reason the cone of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* is the light cone and the singular locus of the algebra at once. The regular-representation determinant being the square is the algebraic statement that the left and right actions see the same norm; there is no separate "left determinant" and "right determinant".

## The Determinant in the Gaussian Integral

The determinant's function in the formalism is to normalize the Gaussian integral, and its one-loop role follows from the same computation.

**The Gaussian.** For a quadratic action $S[\tilde\Phi]=\tfrac12\langle\tilde\Phi,\tilde K\tilde\Phi\rangle$ the functional-integral article gives
$$
\int\mathcal{D}\tilde\Phi\;e^{-\frac12\langle\tilde\Phi,\tilde K\tilde\Phi\rangle}
= \big(\det\tilde K\big)^{-1/2},
$$
the determinant taken on the module. The factor $-\tfrac12$ is the inverse square root appropriate to a real field (one self-conjugate under the pairing); the determinant is taken over the module's components per mode, so the module's dimension enters as the size of the determinant. The power to which the determinant is raised is a convention of real-versus-complex counting and is fixed with the reality of the field; the algebra fixes the module on which the determinant is taken, not the power.

**The one-loop action.** Expanding about a classical field as in the previous article,
$$
S[\tilde\phi+\tilde\eta] = S[\tilde\phi]+\tfrac12\big\langle\tilde\eta,S''[\tilde\phi]\tilde\eta\big\rangle+\cdots ,
$$
the Gaussian integration of $\tilde\eta$ gives the one-loop effective action
$$
\Gamma_1[\tilde\phi] = \tfrac12\,\mathrm{Tr}\log S''[\tilde\phi] ,
$$
where $\mathrm{Tr}$ is the trace pairing. The determinant and the effective action are thus the same object, and the determinant's regularization is the effective action's regularization.

**The free case.** For the free biquaternion scalar, $S''=\tilde K$ is central and mode-diagonal, and
$$
\Gamma_1 = \frac12\sum_{\text{modes}}\log\big(\tilde k\bar{\tilde k}+m^2\big)^2
= \sum_{\text{modes}}\log\big(k_E^2+m^2\big)
\qquad\text{(Euclidean)},
$$
the exponent $2$ being the module's two complex dimensions, which cancels the $\tfrac12$. This is the biquaternion scalar's one-loop free energy; its divergence and renormalization are standard and are the subject of the renormalization-group article.

### The Determinant as a Product over Modes, and Its Ratio

In a translation-invariant background the operator is diagonal in momentum, and the determinant becomes a product over modes. For the central scalar operator on the module,
$$
\det\big(\Box-m^2\big)\Big|_{\text{module}}
= \prod_k\Big(\tilde k\bar{\tilde k}+m^2\Big)^2
= \prod_k\big(k_E^2+m^2\big)^2
$$
in the Euclidean continuation, the square being the module's two complex dimensions and the overall sign of the continuation cancelling in it. The product diverges, and only **ratios** of determinants of operators of the same type are scheme-independent. The ratio
$$
\frac{\det S''_1}{\det S''_2} = \frac{\prod_n \lambda_n^{(1)}}{\prod_n \lambda_n^{(2)}}
$$
is the Ray–Singer torsion of the pair when the operators are Laplacians on a manifold, and it is the finite, physical content of the determinant. In the framework the ratio is taken on a fixed module, and the algebra's contribution is the module's dimension, which fixes the size of each factor.

### The Determinant and the Propagator

The determinant's variation is the trace of the propagator against the variation of the operator,
$$
\frac{\delta}{\delta\chi}\log\det S''[\chi] = \mathrm{Tr}\left( \big(S''[\chi]\big)^{-1}\,\frac{\delta S''[\chi]}{\delta\chi}\right),
$$
where $\chi$ is a background field and $(S'')^{-1}$ is the propagator. This is the identity that makes the determinant the generating functional of one-loop bubbles: differentiating $\log\det$ any number of times produces the connected one-loop graphs with insertions of $\delta S''/\delta\chi$. In the biquaternion framework the inverse is the propagator of *The Feynman Propagator in Biquaternionic Form*, taken on the module, and the trace is the trace pairing. The identity is standard and is recorded because it is the practical route by which the framework's determinants are computed: one computes the propagator and integrates the trace, rather than the product.

## Regularization

The determinant is a divergent product, and its regularized value is defined through the zeta function of the operator.

**Zeta-function regularization.** For an operator $S''$ with discrete spectrum $\{\lambda_n\}$,
$$
\zeta_{S''}(s) = \sum_n \lambda_n^{-s} = \mathrm{Tr}\big(S''\big)^{-s},
\qquad
\log\det S'' = -\zeta_{S''}'(0),
$$
the second relation being the analytic continuation of the first to $s=0$. In this scheme the determinant is finite by construction, and the regularization dependence appears as an additive constant that is fixed by renormalization. For a single mode with eigenvalue $\lambda$ the definition gives $\zeta(s)=\lambda^{-s}$ and $-\zeta'(0)=\log\lambda$, i.e. the ordinary logarithm; the scheme reduces to the ordinary determinant when the product is finite.

**Heat-kernel evaluation.** The zeta function is evaluated from the heat kernel of the previous article,
$$
\zeta_{S''}(s) = \frac{1}{\Gamma(s)}\int_0^\infty dt\;t^{s-1}\,K(t),
\qquad
K(t) = \mathrm{Tr}\,e^{-tS''},
$$
and the small-$t$ expansion $K(t)\sim(4\pi t)^{-d/2}\sum_n a_n t^n$ gives $\zeta(0)$ and $\zeta'(0)$ in terms of the Seeley–DeWitt coefficients $a_n$. In the biquaternion framework $S''$ acts on the module and the coefficients $a_n$ carry the module's dimension and the geometry of the sector on which the operator lives. This is the machinery that the trace anomaly of article 11 uses; here it is recorded as the regularization that gives the determinant its meaning. The heat-kernel method is standard (Seeley, DeWitt, Gilkey) and is cited rather than rebuilt.

**A remark on scheme dependence.** Different regularizations (zeta function, proper time with a cutoff, dimensional regularization) differ by local counterterms, and the *ratios* of determinants of operators of the same type are scheme-independent. In the framework, a scheme-independent statement is one that compares two determinants taken on the same module; this is the same caveat that attends any statement about the norm form's normalization.

## The Fermionic Determinant and Its Phase

The determinant of a fermionic fluctuation operator is the place where the framework's non-central mass term has its clearest consequence.

**The Grassmann integral.** Integrating out a fermion gives a determinant rather than an inverse square root,
$$
\int\mathcal{D}\bar{\tilde\Psi}\mathcal{D}\tilde\Psi\;e^{\,\bar{\tilde\Psi}\mathcal{D}\tilde\Psi} = \det\mathcal{D},
\qquad
\mathcal{D} = i\partial\!\!\!/ - m ,
$$
which is standard. In the framework the spinor field is carried by the spinor module and the mass term is the chirality-off-diagonal, right-multiplication operator of the conventions article; the determinant is therefore that of a module operator whose chiral structure is nontrivial.

**The chiral block structure.** In a chirality basis the fermionic operator has the block form
$$
\mathcal{D} = \begin{pmatrix} -m & \mathcal{D}_R \\ \mathcal{D}_L & -m \end{pmatrix},
$$
whose blocks act between the two minimal left ideals. The mass occupies the diagonal blocks and the derivative terms the off-diagonal ones, so the two chiralities are coupled. In the simplified case where the blocks are scalars the determinant is the elementary $m^2-\mathcal{D}_R\mathcal{D}_L$, checked numerically: for $m=1.3$, $\mathcal{D}_R=0.7+0.4i$, $\mathcal{D}_L=0.9-0.2i$, $\det\mathcal{D}=0.980000-0.220000i=m^2-\mathcal{D}_R\mathcal{D}_L$. In general the mass couples the two chiralities and the determinant is a **product over the chiralities** modified by the mass: $\det\mathcal{D}=\det(\mathcal{D}_L\mathcal{D}_R-m^2)$ up to a sign fixed by the dimension. For the pure off-diagonal (massless) case the block determinant formula gives $\det\begin{pmatrix}0&A\\B&0\end{pmatrix}=(-1)^n\det A\det B$, checked at $n=2$ with $A=\begin{pmatrix}1&2i\\0.5&3\end{pmatrix}$, $B=\begin{pmatrix}2&0.1\\0.3&i\end{pmatrix}$, giving $1.91000+6.03000i=\det A\det B$. The determinant therefore factorizes over the chiralities only in the massless case; the mass term, being the right-multiplication operator that relates the ideals, is exactly what spoils the factorization. This is the same non-centrality that broke the sector factorization of the effective action.

**Hermiticity and phase.** If $\mathcal{D}$ is Hermitian its determinant is real and its sign is physical (the fermion sign problem). If $\mathcal{D}$ is not Hermitian — which is generic for a chiral or a $\theta$-dependent operator — its determinant is complex, and
$$
\det\mathcal{D} = \big|\det\mathcal{D}\big|\,e^{\,i\phi_{\mathcal{D}}},
$$
with the phase $\phi_{\mathcal{D}}$ the object of interest. For a family of operators $\mathcal{D}(t)$ interpolating between two Hermitian endpoints the phase is the **eta invariant** of the family,
$$
\phi_{\mathcal{D}(t)} = \frac{\pi}{2}\,\eta\big(\mathcal{D}(t)\big) + \text{const},
$$
a spectral asymmetry counted by the heat-kernel regularized sum of signs of eigenvalues. This is standard (Atiyah–Patodi–Singer), and it is the analytic home of the framework's $\theta$ dependence: the $\theta$ vacuum of *The Theta Vacuum in Biquaternionic Form* arises when the fermion determinant's phase depends on a background field through the eta invariant, so that $e^{-S}$ acquires a topological phase. The biquaternion content is that the chiral structure whose asymmetry is counted is the two-minimal-left-ideal structure of the algebra, and that the mass term is the right-multiplication operator between them.

**Index and anomaly.** The magnitude's failure to be conformally invariant, and the phase's failure to be trivial, are two faces of the same configuration-space topology. The magnitude's conformal variation is the trace anomaly of *The Trace Anomaly in Biquaternionic Form*; the phase's topology is the $\theta$ vacuum of article 12. Both are properties of a determinant of a module operator, and both are standard field theory written in the framework's notation.

## The Conformal Variation of the Determinant

The determinant responds to a Weyl rescaling of the background, and its response is the trace anomaly; this is worth stating here because it is where the determinant and the energy-momentum trace meet.

Under a local rescaling of the metric, $g_{\mu\nu}\to e^{2\sigma}g_{\mu\nu}$, the quadratic operator and hence the determinant change. For a classically conformally invariant theory the classical action is invariant, but the regularized determinant is not:
$$
\delta_\sigma\log\det S'' \ne 0 ,
\qquad
\big\langle T^\mu_{\ \mu}\big\rangle = -\frac{1}{\sqrt{g}}\,g_{\mu\nu}\frac{\delta\,\Gamma_1}{\delta g_{\mu\nu}} ,
$$
the trace of the energy-momentum tensor being the conformal variation of the one-loop effective action. That this is non-vanishing for a conformally invariant classical theory is the **trace anomaly**, and it is the statement that the regularization of the determinant breaks the classical symmetry. Its coefficient is the Seeley–DeWitt coefficient $a_{d/2}$, and in the biquaternion framework that coefficient carries the module's dimension and the sector structure. The computation and the interpretation of the anomaly are article 11; this article records the determinant-side origin.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The fundamental determinant of an element is the norm form, $\det\Phi(\tilde Q)=N(\tilde Q)=\mathrm{Sc}(\tilde Q\bar{\tilde Q})$; verified and proved.
- Left and right multiplication by $\tilde Q$ on the algebra have equal determinant $N(\tilde Q)^2$; verified and proved.
- A central operator's determinant on the two-complex-dimensional module is the square of its single-complex-dimension value, $\det(\kappa e_0)|_{\text{module}}=\kappa^2$; a non-central operator's determinant does not factor.

**Standard, and transcribed.**
- Zeta-function regularization and $-\zeta'(0)=\log\det$; the heat-kernel and Seeley–DeWitt evaluation; the Grassmann determinant; the eta invariant and its relation to the phase; the conformal variation of $\Gamma_1$ and the trace anomaly.

**Interpretation.**
- Reading the norm form as the determinant, so that zero divisors are exactly the singular elements, is the algebra's own statement. Reading the fermion determinant's phase as the analytic home of the $\theta$ vacuum is the standard Atiyah–Patodi–Singer picture applied to the framework's module.

**Open.**
- The framework has no independent normalization of the determinant; statements are scheme-independent only as ratios on a fixed module.
- Whether the module's dimension and the sector structure produce anomaly coefficients differing from those of a complex scalar is a normalization question that the spin-0 and spin-1/2 articles must fix; this article does not.

## Summary

The functional determinant of a biquaternion operator is a determinant on the module, and the algebra contributes two structural facts to it. The determinant of a single algebra element is the **norm form**,
$$
\det\Phi(\tilde Q) = N(\tilde Q) = \mathrm{Sc}\big(\tilde Q\bar{\tilde Q}\big),
$$
so the singular elements are the zero divisors, i.e. the light cone; and left and right multiplication on the algebra both have determinant
$$
\det L_{\tilde Q} = \det R_{\tilde Q} = N(\tilde Q)^2 .
$$
Both were verified: for $\tilde Q=(0.7+0.2i,\,0.3-0.5i,\,-0.2+0.4i,\,0.1+0.6i)$, $\det\Phi(\tilde Q)=-0.180000-0.060000i$ and $\det L_{\tilde Q}=\det R_{\tilde Q}=0.0288000+0.0216000i=(\det\Phi(\tilde Q))^2$, with $\Phi(\tilde Q)$'s eigenvalues multiplying correctly.

For a central fluctuation operator the module determinant is the square of the single-complex-dimension value, $\det(\kappa e_0)|_{\text{module}}=\kappa^2$, and the free one-loop effective action is $\Gamma_1=\tfrac12\mathrm{Tr}\log S''$; for a non-central operator — the chirality-off-diagonal Dirac mass — the determinant does not factor and acquires a **phase**, the eta invariant of the operator family. Regularization is zeta-function or heat-kernel, with $\log\det=-\zeta'(0)$ and the Seeley–DeWitt coefficient $a_{d/2}$ controlling the divergence; the conformal variation of the determinant is the trace anomaly (article 11) and the phase's topology is the $\theta$ vacuum (article 12). None of the regularization is the algebra's; the operator on which it acts is.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\Phi(e_k)=-i\sigma_k$ | Isomorphism onto $M_2(\mathbb{C})$ |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}$ | Norm form (central); equals the fundamental determinant |
| $\det\Phi(\tilde Q)=N(\tilde Q)=\mathrm{Sc}(\tilde Q\bar{\tilde Q})$ | Determinant of an algebra element |
| $L_{\tilde Q},R_{\tilde Q}$ | Left and right multiplication on the algebra |
| $\det L_{\tilde Q}=\det R_{\tilde Q}=N(\tilde Q)^2$ | Regular-representation determinant |
| $S''[\tilde\phi]$ | Fluctuation operator on the module |
| $\det S''$, $\mathrm{Tr}\log S''$ | Functional determinant; one-loop action |
| $\det(\kappa e_0)|_{\text{module}}=\kappa^2$ | Central operator's module determinant |
| $(\det\tilde K)^{-1/2}$ | Gaussian normalization |
| $\zeta_{S''}(s)=\mathrm{Tr}(S'')^{-s}$, $\log\det S''=-\zeta'(0)$ | Zeta-function regularization |
| $K(t)=\mathrm{Tr}\,e^{-tS''}$, $K\sim(4\pi t)^{-d/2}\sum a_n t^n$ | Heat kernel; Seeley–DeWitt coefficients |
| $a_{d/2}$ | Coefficient controlling the divergence / trace anomaly |
| $\mathcal{D}=i\partial\!\!\!/-m$ | Fermionic fluctuation operator |
| $\det\mathcal{D}=|\det\mathcal{D}|e^{i\phi_{\mathcal{D}}}$ | Complex (chiral) fermion determinant |
| $\eta(\mathcal{D})$ | Eta invariant; spectral asymmetry of the phase |

## Further Reading

- J. S. Schwinger, "On gauge invariance and vacuum polarization," *Physical Review* **82** (1951) 664–679, for the proper-time representation of the one-loop determinant.
- S. W. Hawking, "Zeta function regularization of path integrals in curved spacetime," *Communications in Mathematical Physics* **55** (1977) 133–148, for zeta-function regularization and $-\zeta'(0)$.
- J. S. Dowker and R. Critchley, "Effective Lagrangian and energy-momentum tensor in de Sitter space," *Physical Review D* **13** (1976) 3224–3232, for the zeta-function and point-splitting evaluation of the determinant.
- B. S. DeWitt, *Dynamical Theory of Groups and Fields* (Gordon and Breach, 1965), for the heat kernel and the Seeley–DeWitt coefficients.
- P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem* (Publish or Perish, 1984), for the heat-kernel coefficients and the index theorem.
- M. F. Atiyah, V. K. Patodi, and I. M. Singer, "Spectral asymmetry and Riemannian geometry. I," *Mathematical Proceedings of the Cambridge Philosophical Society* **77** (1975) 43–69, for the eta invariant and the phase of the fermion determinant.
- L. Alvarez-Gaumé and E. Witten, "Gravitational anomalies," *Nuclear Physics B* **234** (1984) 269–330, for anomaly coefficients and their relation to determinants.
- A. S. Schwarz, "The partition function of degenerate quadratic functional and Ray–Singer invariants," *Letters in Mathematical Physics* **2** (1978) 247–252, for the phase of the determinant and the Ray–Singer torsion.
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge, 1982), for the conformal variation of the one-loop determinant.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the determinant and the norm form of the algebra and the module structure.
- Companion articles: *The Functional Integral in Biquaternionic Form*, for the Gaussian determinant and the module; *The Generating Functional and the Effective Action in Biquaternionic Form*, for the one-loop action $\Gamma_1$ and the proper-time form; *The Trace Anomaly in Biquaternionic Form*, for the conformal variation computed; *The Theta Vacuum in Biquaternionic Form*, for the phase and the topological term; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the norm form and the zero-divisor cone; *The Renormalization Group in Biquaternionic Form*, for the regularization dependence and the scheme.
