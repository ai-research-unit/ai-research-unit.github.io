# __The Functional Integral in Biquaternionic Form__

## Introduction

The **functional integral**, or field integral, is the field-theoretic generalization of the Feynman path integral: instead of summing over the paths of one particle, it sums over all field configurations,
$$
Z = \int  \mathcal{D}\tilde{Ξ}\; \exp(\,iS[\tilde{Ξ}]\frac{k_m}{m\,c}),
$$
and its derivatives generate the correlation functions of the theory. The two integrals are not the same object. The path integral sums over the histories of a fixed finite number of degrees of freedom; the functional integral sums over a field, an infinite-dimensional configuration space, and it is the object from which the S-matrix, the generating functional, and the functional determinant are built. This article asks what the biquaternion algebra $\mathbb{B}$ contributes to the functional integral, taking as its point of departure the companion article *The Path Integral in Biquaternionic Form*, which settles the phase and the Wick rotation for the quantum-mechanical case.

The contributions divide cleanly, and the division is the content of the article.

- **Established, and recomputed below.** The **action** of a biquaternion field is a *real central scalar*, extracted from the Hermitian form, read through the trace. The framework's real bilinear form is
$$
\langle \tilde{Q},\tilde{Q}_1\rangle = \mathrm{Re}\,\mathrm{Tr}\big(\tilde{Q}^{*}\tilde{Q}_1\big),
$$
which is the positive-definite Hilbert–Schmidt form on the algebra; the signature split belongs to the biquaternion norm $\langle\cdot\rangle_{\natural}$, not to this pairing. For a field $\tilde{Ξ}=\tilde{Ξ}_-+\tilde{Ξ}_+$ and a central kinetic operator $W_{\mathrm{kinetic}}=\Box-k_m^{2}$ the quadratic action is
$$
S[\tilde{Ξ}] = \int d^4r\; \Big\langle \tilde{Ξ}, W_{\mathrm{kinetic}}\tilde{Ξ}\Big\rangle,
\qquad
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \sum_\mu\partial^2/\partial R_\mu^2 .
$$
The plain form, read as the trace pairing, is what makes the exponent a number and not a biquaternion. Because $W_{\mathrm{kinetic}}$ is central it preserves each sector, and the sectors are **orthogonal** under the real form,
$$
\big\langle \tilde{Ξ}_-,\tilde{Ξ}_+\big\rangle = 0
\qquad\text{for all } \tilde{Ξ}_\pm\in\mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi} ,
$$
checked identically over the sector bases. Hence the free functional integral **factorizes** over the two sectors,
$$
Z_0[\tilde J_{\Phi}] = Z_-[J_-]\,Z_+[J_+] ,
$$
each factor being a Gaussian integral on the sector's module.
- **Established (algebra).** The Gaussian functional integral is evaluated exactly by the algebra's plain form, read as the trace pairing, and the determinant of $K$ on the module:
$$
\int \mathcal{D}\tilde{Ξ}\; \exp(-\frac12\langle \tilde{Ξ}, K\tilde{Ξ}\rangle + \langle \tilde J_{\Phi},\tilde{Ξ}\rangle)
= \big(\det A_{\mathrm{gau}}\big)^{-1/2}\, \exp(\frac12\langle \tilde J_{\Phi}, A_{\mathrm{gau}}^{-1}\tilde J_{\Phi}\rangle),
$$
where $\langle\cdot,\cdot\rangle$ is built from $\mathrm{Sc}$ and the determinant is taken on the spinor module. The finite-dimensional instance of this formula is verified below with explicit Hermitian matrices, and the dependence of $Z$ on the source reproduces the classical action of the free field up to the factor $\tfrac12$.
- **Standard, and transcribed.** The measure $\mathcal{D}\tilde{Ξ}$, the action functional as a datum, the perturbative expansion in powers of the interaction, and the Grassmann integral for fermions. The algebra supplies none of these; the space of field configurations is infinite-dimensional, and $\mathbb{B}$ is finite-dimensional. The gap is stated rather than closed.
- **The Euclidean rotation.** As in the companion *Interpretation of the Wick Rotation in the Biquaternion Universe* — the identification of the material sector $\mathbb{B}_{\Phi}$ with the real-quaternion subspace $\mathbb{B}_{H}$ — the rotation turns the oscillatory weight $\exp(iS)$ into the decaying weight $\exp(-S_E)$. This is what makes the Gaussian integral convergent and is the framework's own account of why the Euclidean integral is better behaved.

The article proceeds as follows. The next section distinguishes the functional integral from the path integral. A section fixes the field, its two sectors, and the central-scalar action. Two sections evaluate the Gaussian functional integral and verify it in finite dimension. A section exhibits the sector factorization. A section treats the free scalar field explicitly, a section the Euclidean rotation, and a section the measure and the gap. A section separates what is established from what is interpretation, and the article closes with open questions.

## The Functional Integral and the Path Integral

The distinction is worth making precisely, because the two share a notation and not a meaning.

The **path integral** of *The Path Integral in Biquaternionic Form* has for its integration variable a map $r_x:r'_t\mapsto r_x(r'_t)$ from an interval to space, and its measure $\mathcal{D}r_x(r'_t)$ is a limit of finite-dimensional measures on the $N-1$ intermediate positions. The number of integration variables is finite at every stage, and the result is a kernel $G_{\mathrm{prop}}(x_f,r'_{t,f};x_i,r'_{t,i})$ — a function of two points.

The **functional integral** has for its integration variable a field $\tilde{Ξ}:x\mapsto\tilde{Ξ}(x)$, a section of a bundle over spacetime, and its measure $\mathcal{D}\tilde{Ξ}$ is a limit of measures on the field values at finitely many spacetime points. The number of integration variables is finite at every stage too — a lattice regularization makes this explicit — but the limit is over an infinite-dimensional configuration space, and the result is a number $Z$ or a functional $Z[\tilde J_{\Phi}]$.

Two consequences of the distinction matter for the framework. First, the algebra's contribution to the phase — the central scalar imaginary and the location of the $i\epsilon$ along the $i r'_t$ direction — is inherited unchanged, because the weight of the functional integral is the same $\exp(\frac{k_m\,i\,S}{m\,c})$ with the same central $i$. Second, the algebra's contribution to the *action* is new, because a field is biquaternion-valued and the action must be a scalar; this is the subject of the next section. The gap of the path-integral article — that the space of paths is outside the finite-dimensional algebra — is inherited and enlarged: the space of field configurations is outside it too.

There is a third kind of object in Dirac's extension of the construction to fields, and it is the one that plays the role the particle kernel plays rather than the role $Z$ or $Z[\tilde J_{\Phi}]$ plays. If $S[\tilde{Ξ}]$ is the integral of the Lagrangian density over a region of spacetime, the quantum analogue of $\exp(\frac{k_m\,i\,S}{m\,c})$ is a **generalized transformation function**: a functional of the field values on the *boundary* of the region, obeying the same composition law as the kernel — split the region in two, multiply the two functionals, and integrate over the field values on the common boundary. Applied repeatedly, the law connects a region with its infinitesimal sub-regions and contains the quantum analogue of the action principle for fields. Unlike the particle kernel of the companion article, it is not in general a transformation between two sets of dynamical variables, and its probability interpretation is correspondingly restricted: the square of its modulus is a relative a priori probability only when the region is bounded by two separate three-dimensional surfaces, each extending to infinity in the space directions and lying entirely outside every light cone with vertex on the other. That condition is the field-theoretic counterpart of the causal ordering that the Feynman propagator's $i\epsilon$ encodes — the amplitude between two configurations is defined when neither surface reaches the other — and it is a restriction on the region and not on the algebra. The object is formal, a limit of the same finite-dimensional integrals as $Z$; it is named here for what it is, a boundary-value functional rather than a number.

## The Field and the Central-Scalar Action

Let the field be a map
$$
\tilde{Ξ} : \mathbb{R}^{3,1}\longrightarrow \mathbb{B},
\qquad
\tilde{Ξ}(r_x) = Ξ_t(r_x)\,e_t + Ξ_x(r_x)\,\vec e_x + Ξ_y(r_x)\,\vec e_y + Ξ_z(r_x)\,\vec e_z,
$$
with complex coefficients $Ξ_\mu(x)$. The field decomposes along the sectors,
$$
\tilde{Ξ} = \tilde{Ξ}_- + \tilde{Ξ}_+ ,
\qquad
\tilde{Ξ}_\pm = \tfrac12\big(\tilde{Ξ} \mp \tilde{Ξ}^{\flat}\big)\in \mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi} ,
$$
where $\flat=-{}^{*}$ is the anti-Hermitian conjugation; this is the field-level use of the sector split that *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *The Informational Sector: States, Observables and Probability* establish.

**The action must be a scalar, and the algebra supplies the extraction.** A biquaternion is not a number, so a Lagrangian built from $\tilde{Ξ}$ is not automatically an action. The framework's scalar extraction is the trace, whose $e_t$ coefficient,
$$
\mathrm{Sc}(\tilde{Q}) = \tfrac12 \mathrm{Tr}(\tilde Q) ,
$$
is the *scalar part* of $\tilde{Q}$; it is a complex number in general, and the physical action is its real part, equivalently the real bilinear form $\langle\tilde{Q},\tilde{Q}_1\rangle_{*}=\mathrm{Re}\,\mathrm{Tr}(\tilde{Q}^{*}\tilde{Q}_1)$. For a quadratic theory the natural action is
$$
S[\tilde{Ξ}] = \int d^4r\;\Big\langle \tilde{Ξ},W_{\mathrm{kinetic}}\tilde{Ξ}\Big\rangle
+ S_{\mathrm{int}}[\tilde{Ξ}],
\qquad
W_{\mathrm{kinetic}} = \Box-k_m^{2} ,
$$
where $W_{\mathrm{kinetic}}$ is built from the central d'Alembertian and a central mass, and $S_{\mathrm{int}}$ collects interactions. Three properties of this action are the algebra's.

1. **It is a scalar, obtained by the trace.** The integrand is the real part of a trace, hence a number, and the integral is a number. The plain form, read as the trace pairing, is exactly the operation that converts the algebra-valued field into an action. This is the field-theoretic counterpart of the propagator article's trace formula.
2. **It is invariant under the biquaternion-norm isometries.** The quadratic term with $W_{\mathrm{kinetic}}$ central is unchanged by left multiplication $\tilde{Ξ}\mapsto\tilde U\tilde{Ξ}$ and right multiplication $\tilde{Ξ}\mapsto\tilde{Ξ}\tilde u$ by unit real quaternions, $\langle\tilde U\rangle_{\natural} = \langle\tilde U,\tilde U\rangle_{\natural}=\langle\tilde u\rangle_{\natural}=e_t$, since $\tilde U^{*}\tilde U=\tilde u\tilde u^{*}=e_t$. The free biquaternion field therefore carries an $SU(2)\times SU(2)$ global symmetry at the level of the quadratic action. Which part of it survives interactions is a question about $S_{\mathrm{int}}$, not about the quadratic term.
3. **It is sector-blind when $W_{\mathrm{kinetic}}$ is central.** A central $W_{\mathrm{kinetic}}$ commutes with the projections onto $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$, so it does not mix the sectors. The consequences are computed in the next two sections.

The mass term requires a word of care, because the framework's **Dirac** mass is not central. As *The Dirac Equation in Biquaternionic Form* records, the Dirac mass term is linear and chirality-off-diagonal, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$, and it acts as a *right* multiplication, which is what allows it to relate the two minimal left ideals (the chiralities). For a **scalar** example, the mass is the central $m^2$ above and the quadratic operator is sector-diagonal. Both cases are handled by the Gaussian formula; the difference is whether $W_{\mathrm{kinetic}}$ is central. The scalar case is taken as the explicit example below, and the fermionic case is remarked on where the structure differs. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

## The Gaussian Functional Integral

The exact evaluation of the Gaussian functional integral is the backbone of perturbation theory, and in the biquaternion framework it is a finite-dimensional determinant problem per mode.

**Finite-dimensional statement.** Let $\xi\in\mathbb{C}^n$ and let $K$ be an $n\times n$ Hermitian positive-definite matrix. Then
$$
\int d^n\xi\; \exp(-\frac12 \xi^\dagger K\xi + J^\dagger\xi + \xi^\dagger J)
= \frac{(2\pi)^n}{\det A_{\mathrm{gau}}}\, \exp(\,J^\dagger A_{\mathrm{gau}}^{-1} J).
$$
For a real field, $\xi\in\mathbb{R}^n$, the same integral is $(2\pi)^{n/2}(\det A_{\mathrm{gau}})^{-1/2}\exp(\frac12 J^T A_{\mathrm{gau}}^{-1}J)$; the difference of a factor $2$ in the exponent and a factor $2$ in the power of $2\pi$ is the standard real-versus-complex counting, and it is exactly the counting that a biquaternion field's two-complex-dimensional mode supplies. The **free energy** $W[J]=\log Z[J]$ is then
$$
W[J] - W[0] = \tfrac12\, J^\dagger A_{\mathrm{gau}}^{-1}J ,
$$
a Gaussian in the source.

**The biquaternion case.** A field $\tilde{Ξ}$ valued in $\mathbb{B}$ has, at each mode, two complex components — the dimension of the spinor module $\mathbb{B}\tilde\Pi(\vec u)\cong\mathbb{C}^2$. The quadratic form is built from $\mathrm{Sc}$, which is a real bilinear pairing, and the Gaussian integral over the module is
$$
\boxed{\;\int \mathcal{D}\tilde{Ξ}\; \exp(-\frac12\langle\tilde{Ξ},W_{\mathrm{kinetic}}\tilde{Ξ}\rangle + \langle\tilde J_{\Phi},\tilde{Ξ}\rangle)
= \big(\det W_{\mathrm{kinetic}}\big)^{-1/2}\, \exp(\frac12\langle\tilde J_{\Phi},W_{\mathrm{kinetic}}{}^{-1}\tilde J_{\Phi}\rangle)\;},
$$
where $\langle\tilde{Ξ},\tilde{Ξ}_{\mathrm{sp}}\rangle=\mathrm{Re}\,\mathrm{Tr}(\tilde{Ξ}^{*}\tilde{Ξ}_{\mathrm{sp}})$ is the real bilinear form of the action, the determinant is taken on the module, and each mode contributes its two complex dimensions. In the Euclidean reading used for the Gaussian the operator $K$ is the kinetic operator $-\Box+k_m^{2}$, whose momentum symbol is the mass-shell operator $\mathcal{M}(\tilde P_{\Phi})=\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}+m^{2}\,c^{2}$; the Lorentzian action's operator $W_{\mathrm{kinetic}}=\Box-k_m^{2}$ is its negative, a sign that leaves the determinant unchanged on the two-complex-dimensional module but fixes the sign of the kernel $W_{\mathrm{kinetic}}{}^{-1}$. The determinant is the object that *The Functional Determinant in Biquaternionic Form* computes; this article records only that the Gaussian integral reduces to it.

**Finite-dimensional verification.** The **real** form of the identity was checked as follows, on a real symmetric — hence Hermitian — matrix $K$, with complex arithmetic carried through the elimination. For
$$
A_{\mathrm{gau}} = \begin{pmatrix} 2 & 0.5 & 0 \\ 0.5 & 1.5 & 0.3 \\ 0 & 0.3 & 1.2 \end{pmatrix},
\qquad \det A_{\mathrm{gau}} = 3.12 ,
$$
the zero-source integral is $Z_0=(2\pi)^{3/2}(\det A_{\mathrm{gau}})^{-1/2}=8.9165$ and, for $J=(0.4,-0.7,1.1)$, $Z[J]=Z_0\exp(\tfrac12 J^T A_{\mathrm{gau}}^{-1}J)=23.964$, both to the accuracy shown. It is the real form that the biquaternion field's quadratic form requires, since the action is built from $\mathrm{Sc}$ and hence from a real bilinear pairing; the complex form displayed above, $Z_0=(2\pi)^n/\det A_{\mathrm{gau}}$, is the one appropriate to a complex field and gives the correspondingly larger prefactor for the same matrix. In one dimension, $W[J]-W[0]=J^2/(2a)$ for $K=a$ was checked on $a=1.7$, $J=0.9$, giving $0.23824$, equal to $J^2/(2a)$ to machine precision. The source-dependent part of the free energy is thus the classical action of the free field evaluated on the source, with the factor $\tfrac12$ that the Gaussian integration produces.

## Sector Factorization

The central kinetic operator does not mix the sectors, and this makes the free integral factorize.

**The cross term vanishes.** Write $\tilde{Ξ}=\tilde{Ξ}_-+\tilde{Ξ}_+$ and expand the real form:
$$
\Big\langle\tilde{Ξ},W_{\mathrm{kinetic}}\tilde{Ξ}\Big\rangle
= \mathrm{Re}\,\mathrm{Tr}\Big(\tilde{Ξ}^{*}_-W_{\mathrm{kinetic}}\tilde{Ξ}_- + \tilde{Ξ}^{*}_+W_{\mathrm{kinetic}}\tilde{Ξ}_+ + \tilde{Ξ}^{*}_-W_{\mathrm{kinetic}}\tilde{Ξ}_+ + \tilde{Ξ}^{*}_+W_{\mathrm{kinetic}}\tilde{Ξ}_-\Big),
$$
using the centrality of $W_{\mathrm{kinetic}}$. The first two terms are the sector norms; the last two are cross terms. For the cross terms one has the identity
$$
\mathrm{Re}\,\mathrm{Tr}\big(\tilde{Ξ}^{*}_-W_{\mathrm{kinetic}}\tilde{Ξ}_+\big) = 0 = \mathrm{Re}\,\mathrm{Tr}\big(\tilde{Ξ}^{*}_+W_{\mathrm{kinetic}}\tilde{Ξ}_-\big)
\qquad\text{for all } \tilde{Ξ}_\pm\in\mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi} .
$$

**Proof.** It suffices to check the statement on the four units, since the real form is bilinear. In the material sector the coordinates are $Q_t=i r'_t$ and $Q_\eta=x_\eta$, in the informational sector $Q_t=r_t$ and $Q_\eta=i r'_{x_\eta}$, and each elementary term is $\mathrm{Re}\,\mathrm{Tr}(e_\mu^{*}W_{\mathrm{kinetic}}e_\nu)$ times the product of one material coordinate and one informational one. The trace factor vanishes off the diagonal, and on it the coordinate product is purely imaginary, $i r'_t\cdot r_t$ on the time slot and $x_\eta\cdot i r'_{x_\eta}$ on each space slot. A direct evaluation over the $4\times4=16$ elementary products gives zero in every case. The cross terms of the real form therefore vanish, and the quadratic form is block diagonal.

**Consequence: factorisation.** With the source split as $\tilde J_{\Phi}=\tilde J_{\Phi,-}+\tilde J_{\Phi,+}$, the free functional integral is
$$
\boxed{\;Z_0[\tilde J_{\Phi}] = \int\mathcal{D}\tilde{Ξ}_-\,\exp(-\frac12\langle\tilde{Ξ}_-,W_{\mathrm{kinetic}}\tilde{Ξ}_-\rangle+\langle\tilde J_{\Phi,-},\tilde{Ξ}_-\rangle)
\times
\int\mathcal{D}\tilde{Ξ}_+\,\exp(-\frac12\langle\tilde{Ξ}_+,W_{\mathrm{kinetic}}\tilde{Ξ}_+\rangle+\langle\tilde J_{\Phi,+},\tilde{Ξ}_+\rangle)
= Z_-[J_-]\,Z_+[J_+]\;}.
$$
Each factor is a Gaussian integral on one sector's four-real-dimensional space, of the form evaluated above. The free quadratic form is therefore **block diagonal**, and the free integral factorizes into a Gaussian on each sector; the sectors are coupled only through an interaction $S_{\mathrm{int}}$ that is not sector-diagonal. A central kinetic operator cannot couple them; a chirality-off-diagonal Dirac mass can, because it is a right multiplication and so is not central.

**A check of the determinant structure.** For a block-diagonal $W_{\mathrm{kinetic}}=\mathrm{diag}(K_-,K_+)$ the determinant factorizes,
$$
\det W_{\mathrm{kinetic}} = \det K_-\,\det K_+ ,
$$
so the Gaussian prefactor of $Z_0$ is the product of the sector prefactors and the factorisation is consistent at the level of the determinant. This was checked on an explicit block-diagonal Hermitian matrix, and it is the algebraic reason the free quadratic form splits into two block-diagonal parts.

## The Free Scalar Field

The cleanest explicit case is the free scalar field, which the scalar example below supplies.

**The Euclidean action.** After the Wick rotation of the next section, the free action of a real scalar of mass $m$ is
$$
S_E[\xi] = \int d^4r_E\;\tfrac12\Big(\partial/\partial R_\mu\xi\,\partial/\partial R_\mu\xi + m^2\xi^2\Big)
= \tfrac12\int d^4r_E\;\xi\big(-\Delta_E + m^2\big)\xi ,
$$
with $\Delta_E$ the Euclidean Laplacian, and in momentum space the kinetic operator is $k_{\mathrm{eu}}^2+m^2$. In the biquaternion framework the field is scalar-valued for the example and the kinetic operator is the central $-\Box+k_m^{2}$ continued to Euclidean signature, with $\Box=\sum_\mu\partial^2/\partial R_\mu^2$; the wave biquaternion $\tilde P_{\Phi}=i(E/c)e_t+\vec p$ has biquaternion norm $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}=-p^2$, which becomes $k_{\mathrm{eu}}^2$ after the Wick rotation, so that the Euclidean kinetic operator is the central scalar $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}+m^{2}\,c^{2}$.

**The Gaussian result.** The free generating functional is
$$
Z_0[J] = \exp\left(\frac12\int\frac{d^4k_{\mathrm{eu}}}{(2\pi)^4}\,\frac{J(-k)J(k)}{k_{\mathrm{eu}}^2+m^2}\right),
$$
and the two-point function is the propagator
$$
\big\langle \xi(x)\xi(y)\big\rangle = \frac{1}{k_{\mathrm{eu}}^2+m^2}
\;\longrightarrow\;
D_F(x-y) \quad\text{(Lorentzian)},
$$
the Feynman propagator of *The Feynman Propagator in Biquaternionic Form*, whose algebra content is the wave biquaternion and the $i r'_t$ axis of the $i\epsilon$ deformation. The functional integral thus reproduces the propagator from the quadratic action, and the algebra's role is confined to naming the kinetic operator's central scalar and the axis of the continuation.

**The determinant.** The prefactor of $Z_0$ is $(\det W_{\mathrm{kinetic}})^{-1/2}$ with the determinant taken on the module, and since the module has two complex dimensions the free determinant is $\prod_k(\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}+m^{2}\,c^{2})^2$ and the prefactor is the product over modes of $(\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}+m^{2}\,c^{2})^{-1}$ — the module's dimension and the $-\tfrac12$ power together giving one inverse power per mode, the convention that *The Functional Determinant in Biquaternionic Form* fixes and that its one-loop free energy $\Gamma_1=\sum_{\text{modes}}\log(\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}+m^{2}\,c^{2})$ records. This determinant is divergent and requires regularization; its computation, its regularization dependence, and its relation to the trace anomaly are the subjects of *The Functional Determinant in Biquaternionic Form* and *The Trace Anomaly in Biquaternionic Form*. This article records the reduction and does not compute the determinant.

**A remark on the biquaternion field.** A genuinely biquaternion-valued scalar has four complex coefficients, equivalently eight real components, and the sector split assigns four real components to each sector; the factorisation above is the statement that the free quadratic form is block diagonal with respect to that split. The two sectors are **not** independent fields in the sense of being separately adjustable: they are related by multiplication by the central $i$, $\mathbb{B}_{\Phi}=i\mathbb{B}_{\Psi}$, so the sector split is a decomposition of one field into its graded parts and not a doubling of the field content. The counting is a component count fixed by the algebra, and it is *not* a claim that the biquaternion scalar is a multiplicity of complex scalars; the sector interpretation is the one of *The Partition Function in Biquaternionic Form* and *The Harmonic Oscillator in Biquaternionic Form*.

## The Euclidean Rotation

The convergence of the Gaussian functional integral is best seen after the Wick rotation, and the framework's account of the rotation is the reason the Euclidean integral is well defined.

The rotation is the replacement of the material time by imaginary time, $r'_t\mapsto -i\tau$, which in the framework is the identification
$$
\mathbb{B}_{\Phi} \;\longrightarrow\; \mathbb{B}_{H},
\qquad
i r'_t\,e_t \;\longmapsto\; c\tau\,e_t ,
$$
i.e. the relabeling of the imaginary-time coefficient as a real one, $ic(-i\tau)=c\tau$, as *Interpretation of the Wick Rotation in the Biquaternion Universe* establishes.
Under this identification the time coefficient $Q_t=i r'_t$ becomes the real $Q_t=c\tau$, so the interval $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$ becomes the sum of squares $\sum_\mu Q_\mu^2$, the biquaternion norm with every coefficient $+1$, and the oscillatory weight becomes a decaying one:
$$
\exp(\,iS[\tilde{Ξ}]) \;\longrightarrow\; \exp(-S_E[\tilde{Ξ}]),
\qquad
S_E[\tilde{Ξ}] = \int d^4r_E\;\mathrm{Sc}\Big(\tilde{Ξ}^{\natural}\big(-\Box_E+m^2\big)\tilde{Ξ}\Big).
$$
For the free theory $S_E\ge 0$ on the configurations that dominate, so the Gaussian weight is bounded and the finite-dimensional integrals converge; this is the framework's own explanation of why the Euclidean functional integral is the better-defined object and why the Lorentzian integral is recovered by analytic continuation. The reader should note that the rotation is a *relabeling within the algebra*, not a rotation of a real time axis into an imaginary one: the imaginary unit is already present, and the rotation moves the coefficient between the anti-Hermitian and real-quaternion subspaces. This is why the $i\epsilon$ prescription and the Wick rotation locate the same axis.

## Localisation to a Causally Complete Region

The functional integral above is written over the whole of spacetime, and Dirac's boundary-value functional is written over a region with boundary. Both are made more precise by restricting the region to one that is **causally complete**, and the restriction is the field-theoretic counterpart of the localisation that the standard treatment of the path integral records.

**Causal completeness.** In a Lorentzian manifold the **causal complement** $O_{\mathrm c}$ of a region $O$ is the set of points that are spacelike to every point of $O$, and $O$ is **causally complete** — causally closed — when
$$
O_{\mathrm{cc}}=O ,
$$
that is, when taking the causal complement twice returns the region. A region is causally complete when it contains every point that can be influenced by, or can influence, its interior through causal curves; equivalently, when the boundary data on $\partial O$ determine the field throughout the region. The standard example is the **double light cone** — the intersection of the future cone of one point with the past cone of another, a bounded causal diamond, the set of points at time separation less than the light-travel distance between the two tips. The **wedge** of the modular articles is the other standard example, unbounded. Both are causally complete; a single light cone is not, and a spacelike slice is not.

**The functional integral on a causally complete region.** Let the field $\tilde{Ξ}$ be restricted to a causally complete region $O$, with the field values on $\partial O$ held fixed as boundary data. Because $O_{\mathrm{cc}}=O$, the boundary data propagate to a definite interior configuration, and the functional integral on $O$ is an **amplitude functional of the boundary values**, the object named in the first section of this article. Splitting $O$ into two causally complete subregions sharing a common boundary, and multiplying their amplitude functionals and integrating over the shared boundary values, reproduces the amplitude of $O$: this is the composition law of the generalized transformation function, and it is at once the statement that the boundary data determine the interior and the quantum analogue of the action principle.

**Why the restriction is made.** Restricting everything to a finite causally complete region is what gives the functional integral its mathematically precise and physically rigorous form, for three reasons. The number of degrees of freedom in a bounded region is controlled, so the regulator has a natural home; the amplitude depends only on data on a compact boundary; and the assignment of observables to regions — the net of local algebras of algebraic quantum field theory — can be stated, with **isotony** (a smaller region's algebra sits inside a larger one's) and **Einstein causality** (observables in spacelike-separated regions commute). The unbounded integral over all spacetime is the limit in which the region is enlarged to the whole manifold, and it is the limit that requires the regulator and the renormalisation of the next section.

**The interpretation in the algebra.** The causal structure is the framework's own, because the cones are the null cones of the material-sector interval: the material reading $Q_t=i r'_t$, whose time square is $-{r'_{t}}^2$, fixes which events are spacelike- and timelike-separated, exactly as *Causality and the Light Cone as an Information Barrier in Biquaternionic Form* and the mathematical article *Pseudo-Riemannian and Lorentzian Geometry* set out, with the causal order, its partial-order properties, and the causal complement. The algebra therefore supplies the **interval that defines the cones** and, with it, the causal relation on which $O_{\mathrm{cc}}=O$ is built; and it supplies **microcausality**, the statement that the field commutator vanishes outside the light cone, which the canonical-quantization and spin–statistics articles record and which is the operator form of Einstein causality. The framework's one fully worked causally complete region is the **wedge**, whose modular Hamiltonian $\tilde H_{\Psi,\mathrm{modular},W}=2\pi G_1$ and Bisognano–Wichmann identification the modular articles and the quantum-gravity agenda exhibit; the double light cone is the bounded instance and is not worked out.

What the algebra does **not** supply is the rest: the construction of the region in the continuum, the restriction of the measure to it, the regulator, and the net of local algebras as an operator-algebraic structure. The restriction is on the **region** and not on the algebra — the same statement the boundary-value functional made — and it leaves the algebra's standing gaps, the measure and the space of configurations, exactly where they were. In this the localisation is the field-theoretic case of the path-integral article's time slicing: the region defines where the integral is taken, and the algebra's contribution is the interval of the cones and the microcausality of the observables, not the integral itself.

## The Measure and the Gap

The functional integral requires an integration measure, and the measure is the algebra's largest gap.

**What the measure is.** In the regulated theory the measure is a product over lattice sites or over modes,
$$
\mathcal{D}\tilde{Ξ} = \prod_{x}\prod_{\mu\in\{t,x,y,z\}}dΞ_\mu(x)
\quad\text{or}\quad
\mathcal{D}\tilde{Ξ} = \prod_{\eta}\prod_{\mu\in\{t,x,y,z\}}dΞ_\mu(k),
$$
a product of Lebesgue measures on the coefficients, one per biquaternion component. The algebra fixes the *number* of components — four complex coefficients, two per sector — and the fact that the measure is the volume form of the module; it does nothing else.

**The gap.** The algebra does not supply: the space of field configurations (infinite-dimensional, and outside the finite-dimensional algebra); the action functional beyond its quadratic part; the choice of regulator; and the definition of the continuum measure. These are the analytic data of the theory, and they are transcribed from the standard treatment. The path-integral article's gap for the space of paths is the same gap in one fewer dimension. What the algebra *does* supply is the scalar extraction that turns a biquaternion Lagrangian into an action, the two-sector structure that factorizes the free theory, the central character of the kinetic operator, and the identification of the Euclidean rotation with a sector relabeling.

**Fermionic fields.** On the spinor-module representative of the chiral pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$, written as the two-by-two array of its two lines with the mass on the diagonal, the functional integral is over Grassmann-valued spinors, and the Gaussian integral returns a determinant rather than an inverse square root,
$$
\int\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}\;\exp\big(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}\,\mathcal{F}\,\tilde{Ξ}_{\mathrm{sp}}\big) = \det\mathcal{F},
\qquad
\mathcal{F}=\begin{pmatrix}-k_m&\mathcal{F}_R\\ \mathcal{F}_L&-k_m\end{pmatrix},
$$
with the spinor structure carried by the module and the mass term linear and chirality-off-diagonal as the conventions require. The Grassmann integral and the determinant are standard; the biquaternion content is the spinor module on which the operator acts and the mass term's right-multiplication form. The fermionic path integral is developed in its own place in the corpus and is not rebuilt here.

## What Is Established and What Is Interpretation

**Established (algebra).**
- The quadratic action of a biquaternion field is the central scalar $\int\mathrm{Sc}(\tilde{Ξ}^{\natural}W_{\mathrm{kinetic}}\tilde{Ξ})$; the Hermitian form, read through the trace, is the scalar extraction.
- For a central kinetic operator the cross terms $\mathrm{Sc}(\tilde{Ξ}^{\natural}_-\tilde{Ξ}_+)$ vanish identically over the sector bases, so the free quadratic form is block diagonal and the free functional integral factorizes, $Z_0=Z_-\cdot Z_+$.
- The Gaussian functional integral is $(2\pi)^{N/2}(\det A_{\mathrm{gau}})^{-1/2}\exp(\frac12\langle J,A_{\mathrm{gau}}^{-1}J\rangle)$ on the module, with $N$ the real dimension of the module; checked in finite dimension with explicit Hermitian matrices.
- The Wick rotation is the identification $\mathbb{B}_{\Phi}\to\mathbb{B}_{H}$ and turns $\exp(iS)$ into $\exp(-S_E)$.
- The material reading $Q_t=i r'_t$ fixes the interval $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$, hence the null cones and the causal relation on which the causally complete regions are built, and microcausality — the vanishing of the field commutator outside the light cone — is the operator form of Einstein causality; the wedge with $\tilde H_{\Psi,\mathrm{modular},W}=2\pi G_1$ is the one fully worked causally complete region.

**Standard, and transcribed.**
- The definition of the functional integral, the measure, the lattice or mode regularization, the perturbative expansion, the Grassmann integral and its determinant, and the free scalar propagator.
- The localisation to a causally complete region, the condition $O_{\mathrm{cc}}=O$, the double light cone and the wedge as instances, and the net of local algebras with isotony and Einstein causality.

**Interpretation.**
- Reading the sector factorization as a framework-specific statement, and the Wick rotation as a relabeling within the algebra rather than a rotation in spacetime, follow the path-integral and Wick-rotation articles; the mathematical contents are checkable and were checked.

**Open.**
- Whether the sector factorization has consequences for anomaly or theta-vacuum structure — where a non-central operator is essential — is taken up in *The Trace Anomaly in Biquaternionic Form* and *The Theta Vacuum in Biquaternionic Form*.
- The determinant is not computed here; its computation and regularization are the subject of *The Functional Determinant in Biquaternionic Form*.

## Summary

The functional integral over a biquaternion field reduces, in its free part, to a block-diagonal quadratic form and hence to a Gaussian integral on each sector's four-real-dimensional space, and its algebra content is the scalar extraction that makes the exponent a number. For a field $\tilde{Ξ}=\tilde{Ξ}_-+\tilde{Ξ}_+$ and a central kinetic operator $W_{\mathrm{kinetic}}=\Box-k_m^{2}$ with $\Box=\tilde\nabla\tilde\nabla^{\natural}=\sum_\mu\partial^2/\partial R_\mu^2$,
$$
S[\tilde{Ξ}]=\int d^4r\;\Big\langle\tilde{Ξ},W_{\mathrm{kinetic}}\tilde{Ξ}\Big\rangle,
\qquad
\Big\langle\tilde{Ξ}_-,\tilde{Ξ}_+\Big\rangle=0 ,
$$
the cross terms vanishing identically over the sector bases (their real part is exactly zero; the leftover complex cross part is purely imaginary and central), so that
$$
\boxed{\;Z_0[\tilde J_{\Phi}]=Z_-[J_-]\,Z_+[J_+] ,
\qquad
Z_\pm[J_\pm]=\big(\det A_{\mathrm{gau},\mathrm{kin},\pm}\big)^{-1/2}\exp(\frac12\langle J_\pm,A_{\mathrm{gau},\mathrm{kin},\pm}{}^{-1}J_\pm\rangle)\;}.
$$
The Gaussian formula was verified in finite dimension ($\det A_{\mathrm{gau}}=3.12$, $Z_0=8.9165$, $Z[J]=23.964$, and $W[J]-W[0]=J^2/(2a)$ in one dimension), and the determinant factorizes for a block-diagonal $W_{\mathrm{kinetic}}$.

The **measure**, the **space of field configurations**, and the **interaction** are outside the algebra and are transcribed; the space of fields is infinite-dimensional, and $\mathbb{B}$ is finite-dimensional. Restricting the integral to a **causally complete region** — the double light cone, or the wedge — makes the boundary-value functional precise and is where the net of local algebras and Einstein causality live; the algebra supplies the interval of the cones, which fixes the causal relation $O_{\mathrm{cc}}=O$, and the microcausality of the observables, while the region, its measure, and the net are transcribed, with the wedge and $\tilde H_{\Psi,\mathrm{modular},W}=2\pi G_1$ the one worked instance. The Wick rotation, in the framework's interpretation, is the identification of the material sector $\mathbb{B}_{\Phi}$ with the real-quaternion subspace $\mathbb{B}_{H}$, and it is what turns the oscillatory weight into the decaying Euclidean one and makes the Gaussian integral converge. The determinant that the Gaussian integral leaves behind is the subject of the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H},\mathbb{B}_{C}$ | Real-quaternion subspace; centre |
| $\tilde{Ξ}=\tilde{Ξ}_-+\tilde{Ξ}_+$ | Biquaternion field and its sector parts |
| $\mathrm{Sc}(\tilde{Q})=\tfrac12\mathrm{Tr}(\tilde{Q})$ (complex scalar part) | Scalar extraction; the trace converts a biquaternion into a number |
| $\langle\tilde{Q},\tilde{Q}_1\rangle=\mathrm{Re}\,\mathrm{Tr}(\tilde{Q}^{*}\tilde{Q}_1)$ | Real bilinear form of the action; sector-orthogonal |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}=\sum_\mu\partial^2/\partial R_\mu^2$ | d'Alembertian, series convention |
| $\tilde P_{\Phi}=i(E/c)e_t+\vec p$, $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}=-p^2$ | Wave biquaternion; Euclidean $k_{\mathrm{eu}}^2$ |
| $S[\tilde{Ξ}]=\int d^4r\,\langle\tilde{Ξ},W_{\mathrm{kinetic}}\tilde{Ξ}\rangle$ | Quadratic biquaternion action; $W_{\mathrm{kinetic}}=\Box-k_m^{2}$ |
| $Z[\tilde J_{\Phi}]=\int\mathcal{D}\tilde{Ξ}\,\exp(-\frac12\langle\tilde{Ξ},W_{\mathrm{kinetic}}\tilde{Ξ}\rangle+\langle\tilde J_{\Phi},\tilde{Ξ}\rangle)$ | Functional integral with source |
| $Z_0=(\det W_{\mathrm{kinetic}})^{-1/2}\exp(\frac12\langle\tilde J_{\Phi},W_{\mathrm{kinetic}}{}^{-1}\tilde J_{\Phi}\rangle)$ | Gaussian result; $\prod_k(\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}+m^{2}\,c^{2})^{-1}$ per mode for the free central operator |
| $W[\tilde J_{\Phi}]=\log Z[\tilde J_{\Phi}]$, $W-W_0=\tfrac12\langle\tilde J_{\Phi},W_{\mathrm{kinetic}}{}^{-1}\tilde J_{\Phi}\rangle$ | Free energy |
| $r'_t\mapsto-i\tau$, $\mathbb{B}_{\Phi}\to\mathbb{B}_{H}$ | Wick rotation; $\exp(iS)\to \exp(-S_E)$ |
| $O$, $O_{\mathrm c}$, $O_{\mathrm{cc}}=O$ | Region, causal complement, causal completeness (localisation) |
| $\tilde H_{\Psi,\mathrm{modular},W}=2\pi G_1$ | Wedge modular Hamiltonian (the worked causally complete region) |
| $\det\mathcal{F}$, $\mathcal{F}=\begin{pmatrix}-k_m&\mathcal{F}_R\\ \mathcal{F}_L&-k_m\end{pmatrix}$ | Fermionic Gaussian result (Grassmann integral) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- P. A. M. Dirac, "The Lagrangian in quantum mechanics," *Physikalische Zeitschrift der Sowjetunion* **3** (1933) 64–72, for the transformation function and its extension to fields, the generalized transformation function.
- R. P. Feynman, "Space-time approach to non-relativistic quantum mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the path integral from which the functional integral descends.
- R. P. Feynman, "The theory of positrons," *Physical Review* **76** (1949) 749–759, for the functional treatment of fields.
- J. Schwinger, "Quantum electrodynamics. I. A covariant formulation," *Physical Review* **74** (1948) 1439–1461, for the action-based formulation of field theory.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the functional integral, the measure, and the perturbative expansion.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for Gaussian functional integrals, generating functionals, and the free propagator.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford, 2002), for the Euclidean formulation, the measure, and the Gaussian evaluation.
- J. W. Negele and H. Orland, *Quantum Many-Particle Systems* (Addison-Wesley, 1988), for the Grassmann functional integral and the determinant of the Dirac operator.
- L. S. Schulman, *Techniques and Applications of Path Integration* (Wiley, 1981), for the finite-dimensional limits that define both integrals.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the net of local algebras, isotony, Einstein causality, and the localisation to causally complete regions.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the axioms of local quantum field theory and the causal structure on which the region $O_{\mathrm{cc}}=O$ is built.
- G. W. Gibbons, S. W. Hawking, and M. J. Perry, "Path integrals and the indefiniteness of the gravitational action," *Nuclear Physics B* **138** (1978) 141–150, for the convergence of the Euclidean functional integral.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the module structure on which the biquaternion field's Gaussian integral is taken.
- Companion articles: [The Path Integral in Biquaternionic Form](the-path-integral-in-biquaternionic-form.html), for the phase, the central imaginary, and the gap for the space of paths; [Interpretation of the Wick Rotation in the Biquaternion Universe](interpretation-of-the-wick-rotation-in-the-biquaternion-universe.html), for the rotation as a sector identification; [The Generating Functional and the Effective Action in Biquaternionic Form](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), for $W[\tilde J_{\Phi}]$ and $\Gamma[\tilde{Ξ}]$; [The Functional Determinant in Biquaternionic Form](the-functional-determinant-in-biquaternionic-form.html), for the determinant left by the Gaussian integral; [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html), for the Euclidean trace and the imaginary-time circle; [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the sector split used in the factorization.
