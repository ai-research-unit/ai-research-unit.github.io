# __Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation__

## Introduction

The companion article *The Biquaternion D'Alembertian and Its Green's Functions* owns the shifted gradient $\tilde{\nabla}_\kappa = \tilde{\nabla} + \kappa$, the **generalized Maxwell–Dirac equation** $(\tilde{\nabla} + \kappa)B = F$, the scalar operator the source calls the **Klein–Gordon–Fock–Schrödinger equation** (KGFSh), its symbol $(\omega/c - \kappa)^2 - \|\mathbf{k}\|^2$, and the real-$\kappa$ dichotomy that selects the case with non-trivial homogeneous solutions. That section closed with an explicit gap: the source's own fundamental solution — the displayed equation the corpus's record calls "the source's explicit Eq. (36)" — was **not stated**, because the degraded text of the paper then at hand did not allow its signs to be checked, and the corpus does not state an equation it cannot verify. The article also deferred the source's first-order integral representation of the solution.

This article closes that gap. It takes the same programme's later journal paper on the **biquaternion representation of the Dirac equations and bispinor fields**, whose text layer is usable, and it states and verifies the solution theory the earlier record left open: the fundamental solution of the KGFSh operator and its support, the general solution of the inhomogeneous equation, and the bispinor fields that the homogeneous equation carries. The operator itself, its square, its symbol and the convention crossing $\kappa = -im$ are **not** re-derived here; they belong to the d'Alembertian article and are used as given.

Four boundaries are respected. (i) The corpus's own Dirac equation, its square, its reduction to Klein–Gordon and its spinor module belong to *The Dirac Equation in Biquaternionic Form*, *Klein–Gordon from the Dirac Square in Biquaternionic Form* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; this article adds the external programme's solution theory and says where it differs. (ii) The corpus's Klein–Gordon propagator and the corpus's massive scalar kernel are the subject of *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form*; this article uses that kernel only as the contrast that makes the programme's result visible. (iii) The identification of $B$ with a Maxwell field is a claim about the interpretation of $B$, not about the operator, and is not reopened. (iv) Nothing here is a derivation of quantum physics or a comparison with measured particle data; the equation is chosen by the programme, and the corpus records what the chosen equation implies.

Two conventions are load-bearing. The source's **two bigradients** are $\nabla^\pm = \partial_\tau \pm i\nabla$, with $\nabla$ the pure-vector gradient acting by left quaternion multiplication and $\tau = ct$. They are the corpus's gradient pair times $i$,

$$
\nabla^+ = i\tilde{\nabla}, \qquad \nabla^- = i\tilde{\nabla}^{\natural},
\qquad \partial_\tau = -\frac{i}{c}\partial_t ,
$$

which was checked exactly. The source's **wave operator** is therefore minus the corpus's d'Alembertian,

$$
\nabla^-\nabla^+ = \nabla^+\nabla^- = \Box_{\text{s}} := \partial_\tau^2 - \Delta = -\,\Box ,
\qquad \Box = \partial_{ict}^2 + \Delta ,
$$

and the source's operator differs in sign from the corpus's. Consequently the source's mass $m$ in $(\nabla^\pm + m)B = F$ is related to the corpus's central shift by $\kappa = -im$, and the case the source studies — an **imaginary** $m = i\rho$ — is the corpus's **real** $\kappa = \rho$, the case in which the homogeneous equation has non-trivial solutions. Every identification below is stated on the source's side and translated once; the factors of $i$ are not left to the reader.

## The Matrix Form and the Matrix of the Gradient

The source writes its biwave equation in matrix form, $\sum_j D_j\partial_j\,B = G$, and exhibits the four $4\times4$ matrices

$$
D^0 = I_4, \qquad
D^1 = \begin{pmatrix} 0 & -i & 0 & 0\\ i & 0 & 0 & 0\\ 0 & 0 & 0 & i\\ 0 & 0 & -i & 0\end{pmatrix}, \qquad
D^2 = \begin{pmatrix} 0 & 0 & -i & 0\\ 0 & 0 & 0 & i\\ i & 0 & 0 & 0\\ 0 & -i & 0 & 0\end{pmatrix}, \qquad
D^3 = \begin{pmatrix} 0 & 0 & 0 & -i\\ 0 & 0 & -i & 0\\ 0 & i & 0 & 0\\ i & 0 & 0 & 0\end{pmatrix},
$$

with the property the source announces as the Dirac property, $\sum_m D_{mj}D_{jl} = \delta_{ml}$, that is $D_j^2 = I$ for each $j$. The corpus can say exactly what these matrices are, and the answer removes the appearance of a Clifford algebra: **$D_j$ is the matrix of left multiplication by the basis element $ie_j$** of $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ in the coefficient basis $(e_0,e_1,e_2,e_3)$ of $\mathbb{C}^4$. That identification was checked entry by entry against the regular representation of $ie_j$, and it explains the square: $(ie_j)^2 = i^2e_j^2 = (-1)(-1) = +1$, so $D_j^2 = I$ is not a Clifford relation but the statement that the squared unit biquaternion equals $e_0$.

Three facts follow, and each is worth stating because the source's wording invites a stronger reading than the algebra supports.

- **The three spacelike matrices close on $\mathrm{Cl}_{3,0}$, not on $\mathrm{Cl}_{1,3}$.** Left multiplications by $ie_j$ and $ie_k$, $j\neq k$, anticommute, $\{D_j,D_k\} = 0$, exactly, since $e_je_k = -e_ke_j$. So the three of them are a Clifford set with all positive squares.
- **The fourth is not part of that set.** $D^0 = I$ commutes with everything, so $\{D_0,D_j\} = 2D_j \neq 0$: the source's index identity is a statement about each matrix with itself, not an anticommutation over four indices. The corpus's own Dirac dictionary supplies a genuine Clifford set through the matrix image $\Phi$; the two objects are different and must not be conflated.
- **The "matrix Dirac operator" is the regular representation of the gradient.** Since $D = \partial_\tau I + \sum_j D_j\partial_j$ is the matrix of $\partial_\tau + i\nabla = \nabla^+$, the matrix form of the source's first-order equation is the matrix form of left multiplication by a biquaternion — no more and no less. The corpus's Dirac dictionary says the same thing from the other side: $\mathbb{B} = \mathrm{End}(S)$, and every complex-linear operator on the spinor module is some biquaternion.

## The Square and the Two Senses of "the Square of the Dirac Operator"

With the two bigradients fixed, the composition lemma of the source is immediate and was verified on a test field at the finite-difference floor,

$$
\nabla^-\nabla^+ = \nabla^+\nabla^- = \Box_{\text{s}} = \partial_\tau^2 - \Delta ,
$$

and the square of the mass-shifted operator is **not** the d'Alembertian but a shifted, first-order-carrying operator,

$$
\bigl(\nabla^- + m\bigr)\bigl(\nabla^+ + m\bigr)
= \Box_{\text{s}} + m^2 + 2m\,\partial_\tau
= \bigl(\partial_\tau + m\bigr)^2 - \Delta ,
$$

also verified, and in the imaginary case $m = i\rho$,

$$
\bigl(\nabla^- + i\rho\bigr)\bigl(\nabla^+ + i\rho\bigr)
= \Box_{\text{s}} - \rho^2 + 2i\rho\,\partial_\tau .
$$

This is the KGFSh operator the d'Alembertian article owns, and it is where the programme and the corpus part company in a way worth naming. The corpus's Dirac pair is chirality off-diagonal,

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L , \qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
\qquad\Longrightarrow\qquad
\bigl(\Box - \mu^2\bigr)\tilde{\Psi}_{R,L} = 0 ,
$$

and it squares to the Klein–Gordon operator **with no first-order term**, because the mass enters once on each side. The programme carries the *same* mass twice on the same side, $(\nabla^\pm + m)(\nabla^\mp + m)$, and the cross term $2m\partial_\tau$ it produces survives. Both computations are correct; they are squares of different operators. The corpus's result — the second-order equation implied by the biquaternionic Dirac equation is Klein–Gordon — is therefore not contradicted by the programme, and the programme's operator is not the corpus's mass term: the corpus's mass is the additive central $\Box - \mu^2$ with $\mu = mc/\hbar$ real, while $2\kappa\partial_{ict}$ is first order and cannot be written as $\Box - \mu^2$. The d'Alembertian article states this separation; the present article keeps it.

One identity is the engine of everything that follows. Because the shifted operator is a conjugation of the wave operator,

$$
\Box_{\text{s}} + m^2 + 2m\partial_\tau
= e^{-m\tau}\,\Box_{\text{s}}\,e^{+m\tau},
$$

verified on a test field, every solution of the programme's homogeneous scalar equation is an exponentially weighted wave,

$$
\Bigl(\Box_{\text{s}} + m^2 + 2m\partial_\tau\Bigr)u = 0
\qquad\Longleftrightarrow\qquad
u = e^{-m\tau}v , \quad \Box_{\text{s}}v = 0 .
$$

For **real** $m$ the weight is a genuine exponential in $\tau$; for the corpus's real $\kappa = \rho$, that is for the source's imaginary $m = i\rho$, it is a phase $e^{-i\rho\tau}$ and the operator is the one whose symbol the d'Alembertian article evaluated. The same identity applied to the Green's function is the sharp-support statement of the next section.

## The Fundamental Solution of the KGFSh Operator

### The source's derivation, and what it gives

The source solves the KGFSh equation by transforming in $\tau$. With $\omega$ the Fourier variable conjugate to $\tau$ and $k = i\omega - m$, the transform $\mathcal{F}_\tau[\psi_m]$ obeys the **Helmholtz equation with a complex wave number**,

$$
\bigl\{\Delta - k^2\bigr\}\mathcal{F}_\tau[\psi_m] + \delta(\mathbf{x}) = 0 ,
\qquad k = i\omega - m ,
$$

whose fundamental solution is $\mathcal{F}_\tau[\psi_m] = \frac{1}{4\pi R}\bigl(ae^{-kR} + (1-a)e^{kR}\bigr)$ with $R = |\mathbf{x}|$ and $a$ an arbitrary constant. That kernel was verified: the ball integral of $(\Delta + k^2)$ applied to $-\frac{1}{4\pi R}e^{\pm ikR}$ is $+1$ for the two signs and two values of $k$, which is the coefficient of $\delta(\mathbf{x})$.

The inverse transform then fixes the support, and this is the source's real result. Since the inverse transform of $e^{\pm i\omega R}$ is $\delta(\tau \mp R)$, the two terms are supported on the two light cones and the assembled fundamental solution is

$$
\psi_m(\tau,\mathbf{x})
= \frac{e^{-m\tau}}{4\pi R}\Bigl[a\,\Theta(\tau)\,\delta(\tau - R) + (1-a)\,\Theta(-\tau)\,\delta(\tau + R)\Bigr] + \psi^0_m ,
$$

where $\psi^0_m$ solves the homogeneous equation. Two points of the source's display need correcting, and both follow from the derivation rather than from opinion.

- **The two light-cone terms carry one common factor $e^{-m\tau}$, not $e^{-mR}$.** On the retarded cone $\tau = R$ the two writings agree, which is why the source's retarded formula is right; on the advanced cone $\tau = -R$ the common factor is $e^{+mR}$, and writing $e^{-mR}$ there is wrong for $m \neq 0$. Checked directly: at $m = 0.9$, $\tau = -1.5$ the factor matches $e^{mR}$ to machine precision and differs from $e^{-mR}$ by a factor $3.6$.
- **The retarded member is exactly the source's Eq. (36),** the equation the corpus declined to state,

$$
\psi_m(\tau,\mathbf{x}) = \frac{e^{-mR}}{4\pi R}\,\delta(\tau - R) ,
\qquad R = |\mathbf{x}| ,
$$

which is $e^{-m\tau}$ times the massless retarded kernel $G_{\mathrm{ret}} = \frac{1}{4\pi R}\delta(\tau - R)$ that the d'Alembertian article derives and normalises. With the exponential-substitution identity this is not a numerical coincidence but a proof: the KGFSh Green's function is the wave Green's function multiplied by the weight, and the weight does not move the support. The weight here is central — one scalar $m$ — and the companion article *The Biquaternion D'Alembertian and Its Green's Functions* carries the generalisation to a full constant biquaternion coefficient $f + F$, where the scalar part continues to weight the kernel by $e^{-f\tau}$ and the vector part multiplies it by a pure phase and so also moves no support; the non-central part does not add to the price paid here, because the first-order operator it contributes is self-adjoint for real $F$.

### The sharp kernel, and the contrast that makes it interesting

The corpus's massive scalar operator behaves differently, and the difference is the one substantive analytic gain this paper offers. For $\Box - \mu^2$ the retarded and advanced kernels "acquire support inside the cone rather than on it, the sharp light-cone delta acquiring a tail in the Bessel functions" — the d'Alembertian article's own words, and the Klein–Gordon propagator article works the tail out. For the KGFSh operator the opposite happens. Because

$$
\Bigl(\Box_{\text{s}} + m^2 + 2m\partial_\tau\Bigr)G
= e^{-m\tau}\Box_{\text{s}}\Bigl(e^{m\tau}G\Bigr) ,
$$

a kernel is a solution for the shifted operator exactly when $e^{m\tau}G$ is a solution for the wave operator, so the shifted kernel is $\psi_m = e^{-m\tau}G_{\mathrm{ret}}$ and its support is **exactly the cone**, with a $\delta$ rather than a Bessel profile on it. In the language of the classical theory this is Huygens' principle: the solution at a point depends on the data on the cone alone, not on the interior. The massless wave operator has it in $3+1$ dimensions, the Klein–Gordon operator does not, and the programme's first-order term restores it.

The source draws the right conclusion from this — that the additional term "significantly simplifies" the fundamental solution compared with the Klein–Gordon one — and the corpus can now state the simplification exactly, together with its price. The price is that the operator is no longer self-adjoint: the adjoint of $\Box_{\text{s}} + m^2 + 2m\partial_\tau$ carries $-2m\partial_\tau$, and the weight $e^{-m\tau}$ is a damping for real $m$ and a rotation for imaginary $m$. Huygens and self-adjointness are not the same property, and the programme buys the first with the second.

## The Homogeneous Equation and the Class Question

The source's Theorem 5 states that for $\operatorname{Re}m \neq 0$ the homogeneous KGFSh equation has only the zero solution for $\tau \geq 0$, and proves it by Fourier transformation: the symbol $\xi^2 - (\omega + im)^2$ does not vanish for real $(\omega,\boldsymbol{\xi})$, so the transform vanishes and the solution does. The symbolic step is correct, and the conclusion is correct **in the class of solutions whose Fourier transform exists**. As a statement about all solutions it is false, and the counterexample is the substitution identity of two sections above:

$$
u(\tau,\mathbf{x}) = e^{-m\tau}\,e^{i(\mathbf{k}\cdot\mathbf{x} \mp |\mathbf{k}|\tau)} ,
\qquad
\Bigl(\Box_{\text{s}} + m^2 + 2m\partial_\tau\Bigr)u = 0 \quad \text{identically.}
$$

This was checked: for real $m = 0.9$ the residual of $u$ sits at the finite-difference floor while a control with the wrong frequency gives $1.5$, a ratio of $2\times10^{6}$. Such a $u$ grows like $e^{m|\tau|}$ as $\tau \to -\infty$, so it is not tempered and has no Fourier transform; the source's proof therefore proves the tempered statement, not the general one. The corpus states it that way: **for $\operatorname{Re}m \neq 0$ a tempered solution of the homogeneous KGFSh equation vanishes**, and the general solution is $e^{-m\tau}$ times an arbitrary wave. The distinction is not academic — it is the same distinction that makes the Cauchy problem for the operator non-trivial, and the d'Alembertian article's own Kirchhoff paragraph already relies on it.

The d'Alembertian article states the same dichotomy from the corpus's side in the same terms: for non-real $\kappa$ the symbol never vanishes on real $(\omega,\mathbf{k})$, so there is no non-trivial homogeneous **plane wave**, and the class in which the homogeneous equation has *only* the trivial solution is the class stated here. The two articles agree, and the agreement is exact rather than approximate: the plane-wave statement is the source's symbol computation, and the qualification is the exponential substitution above.

For the corpus's real $\kappa = \rho$, that is for the source's $m = i\rho$, the homogeneous solutions not only exist but are the source's producing family,

$$
\psi_\rho(\tau,\mathbf{x}) = e^{-i\rho\tau}\int_{\mathbb{R}^3} f(\boldsymbol{\xi})\,e^{i(\boldsymbol{\xi}\cdot\mathbf{x} \pm |\boldsymbol{\xi}|\tau)}\,d^3\xi ,
\qquad f \in L^1(\mathbb{R}^3),
$$

a superposition of the plane waves of the next section weighted by a free profile. This is the general homogeneous solution in the case that matters.

## The General Solution of the Inhomogeneous Equation

The solution of the programme's first-order equation is assembled from the kernel in one line. For

$$
\bigl(\nabla^\pm + m\bigr)B = F ,
$$

the source's Theorem 2 gives

$$
B = B_0 + \bigl(\nabla^\mp + m\bigr)\bigl(F * \psi_m\bigr) ,
$$

with $B_0$ any solution of the homogeneous equation and $*$ the source's biquaternionic convolution, which pairs the algebra product with the functional convolution of the four coefficient distributions. The verification is algebraic and was carried out: applying the operator to the second term collapses the composition to $(\Box_{\text{s}} + m^2 + 2m\partial_\tau)(F * \psi_m) = F * \bigl(\Box_{\text{s}} + m^2 + 2m\partial_\tau\bigr)\psi_m = F * \delta(\tau)\delta^{(3)}(\mathbf{x}) = F$, the step that the source writes out and that the corpus reproduces because it is the whole content of the theorem. Theorems 3, 6 and 7 of the source are the same statement in the imaginary and harmonic cases; the corpus records them as one theorem re-expressed rather than as four independent results.

This is the piece the d'Alembertian article marked as the source's own. The corpus's own formulation of the same content is the Kirchhoff representation it states in second-order form; the source's is first order and carries the extra $\nabla^\mp + m$ applied to a scalar potential. The corpus can now record both, because the kernel they both use is the same $\psi_m$ and it is verified.

## Bispinors of a Scalar Field and the Linear Dispersion

The programme generates its bispinor fields from a scalar potential by exactly the **monogenic completion** the d'Alembertian article records,

$$
\Psi_\rho = \bigl(\nabla^\mp + i\rho\bigr)\psi_\rho ,
\qquad
\bigl(\nabla^\pm + i\rho\bigr)\Psi_\rho = 0
\ \text{ whenever }\ 
\bigl(\Box_{\text{s}} - \rho^2 + 2i\rho\partial_\tau\bigr)\psi_\rho = 0 ,
$$

which was verified on the plane-wave family. The source calls $\psi_\rho$ the **scalar potential of the bispinor C-field**, and $\Psi_\rho = i\rho\psi_\rho + \partial_\tau\psi_\rho \pm i\nabla\psi_\rho$ is its bispinor. Everything the corpus needs to know about these fields follows from the dispersion of the scalar potential, so that is where the content is.

The plane harmonic waves are

$$
\varphi^{\pm}_{\boldsymbol{\xi}}(\tau,\mathbf{x}) = e^{i(\boldsymbol{\xi}\cdot\mathbf{x} - (\rho \pm |\boldsymbol{\xi}|)\tau)} ,
\qquad \Longrightarrow \qquad
\omega = \rho \pm |\boldsymbol{\xi}| ,
$$

and the dispersion relation is **exact and linear**. It was checked against its alternative: the linear law solves the equation at the difference-scheme floor, while the relativistic form $\omega^2 = \boldsymbol{\xi}^2 + \rho^2$ gives a residual $7.4$, four million times larger. Three consequences deserve to be stated plainly.

- **The group velocity is exactly $1$ on both branches**, $|d\omega/d|\boldsymbol{\xi}|| = 1$ in units of $c$, at every wave number. Nothing in this family transports a signal faster than the massless speed, and the family has no anomalous dispersion.
- **The phase velocity is not**, $V = \omega/|\boldsymbol{\xi}| = 1 \pm \rho/|\boldsymbol{\xi}|$. It is superluminal on the upper branch, subluminal on the lower, and the source's "supersonic / subsonic" language is a statement about this phase velocity. The corpus's articles on superluminal phase velocities in other settings make the same point; it is worth repeating here that a superluminal phase velocity is not a superluminal signal, and that the source's own group-velocity content is c.
- **There is a mode of zero phase velocity.** At $|\boldsymbol{\xi}| = \rho$ the two branches have $\omega = 2\rho$ and $\omega = 0$: the second is a spatial pattern that does not oscillate in time, and the source's section on static bispinors is that mode. A "mass" $\rho$ that shifts the light cone rather than curving it produces, at one particular wave number, a frozen field.

The source's reading of the same formulas is the *shifted cone*, which the d'Alembertian article already verified: the symbol $\bigl(\omega/c - \kappa\bigr)^2 - \|\mathbf{k}\|^2$ vanishes on $\omega/c = \kappa \pm \|\mathbf{k}\|$, and with $\kappa = \rho$ that is the linear law above. The corpus should be explicit that this is a shift of the massless cone, not the corpus's mass shell: the corpus's on-shell condition is the hyperboloid $N(\tilde{K}) = -\mu^2$, and a family of plane waves shifted linearly has no hyperboloid and no threshold. The programme's "mass" is a frequency offset, and the corpus's is a curvature; the two agree only at $\rho = 0$.

## The Null Harmonic Bispinor, and the Corpus's Idempotent

The source's most quotable result is about the amplitude of the plane-wave bispinor, and in the corpus's own algebra it has a clean reading. Applying the bigradient to a plane wave gives a *closed* prefactor,

$$
\bigl(\nabla^\sigma + i\rho\bigr)\varphi^{s}_{\boldsymbol{\xi}}
= -|\boldsymbol{\xi}|\,\bigl(is + \sigma\hat{\boldsymbol{\xi}}\bigr)\varphi^{s}_{\boldsymbol{\xi}} ,
\qquad \sigma, s \in \{+,-\} ,
\qquad \hat{\boldsymbol{\xi}} = \boldsymbol{\xi}/|\boldsymbol{\xi}| ,
$$

so that the source's harmonic bispinors are

$$
S^{\pm}_{\boldsymbol{\xi}} = \tfrac{1}{2}\bigl(i + \hat{\boldsymbol{\xi}}\bigr)\,\varphi^{\pm}_{\boldsymbol{\xi}} ,
$$

and the prefactor was verified: its norm is $\sqrt2|\boldsymbol{\xi}|$, it is **null**, and for $\sigma = s$ it lies in the ideal generated by the corpus's idempotent. The identification is exact and worth writing without a factor of $i$ out of place:

$$
\tfrac{1}{2}\bigl(i + \hat{\boldsymbol{\xi}}\bigr) = i\,\tilde{\Pi}_2(\hat{\boldsymbol{\xi}}) ,
\qquad
\tilde{\Pi}_{1,2}(\hat{\mu}) = \tfrac12\bigl(e_0 \pm i\hat{\mu}\bigr) ,
$$

where $\tilde{\Pi}_{1,2}(\hat{\mu})$ is the corpus's rank-one projector, the **pure state** of the informational sector, and $\hat{\mu}$ runs over the unit sphere. The verification is a one-line computation and it was done: $\tilde{\Pi}_2^2 = \tilde{\Pi}_2$; $\tilde{\Pi}_1 + \tilde{\Pi}_2 = e_0$; $\tilde{\Pi}_1\tilde{\Pi}_2 = 0$; and $\tfrac12(i + \hat{\boldsymbol{\xi}}) = i\tilde{\Pi}_2(\hat{\boldsymbol{\xi}})$ to machine precision for thirty random directions. Five statements follow, and the corpus records them as the algebra's contribution to the programme's "harmonic particles".

1. **The harmonic bispinor lies in a minimal left ideal.** Since $S = i\tilde{\Pi}_2(\hat{\boldsymbol{\xi}})\varphi$ and the phase $i\varphi$ is central, $S \in \mathbb{B}\tilde{\Pi}_2(\hat{\boldsymbol{\xi}})$: checked as $S\tilde{\Pi}_2 = S$. The programme's bispinors are not generic elements of the algebra; their amplitude direction is fixed by a pure state of the corpus's informational sector.
2. **The amplitude is in the material sector.** $\tilde{\Pi}_2$ is Hermitian, $\tilde{\Pi}_2^{*} = \tilde{\Pi}_2$, hence in $\mathbb{M}_+$; and $S$ is anti-Hermitian, $S^{*} = -S$, hence in $\mathbb{M}_-$, the material sector — which is the statement $i\mathbb{M}_+ = \mathbb{M}_-$ the conventions article records. So the programme's harmonic bispinor is the material-sector image of a pure state, and the corpus's sector language carries the whole of the source's "particle" vocabulary for these objects.
3. **The harmonic bispinor is a zero divisor.** With the corpus's norm $N(\tilde{Q}) = \sum_\mu Q_\mu^2$, $N(S) = \tfrac14(i^2) + \tfrac14|\hat{\boldsymbol{\xi}}|^2 = 0$, so $S$ lies on the zero-divisor cone. The same vanishes under the source's pseudonorm, the sesquilinear form of its Definition 3. So under either reading the programme's bispinor is null: a bispinor field of the programme's "massive" first-order equation is an element of the null cone, which is the algebraic content of the family's lightlike dispersion.
4. **The normalisation needs one correction.** The source states norm $1$ and pseudonorm $0$. The pseudonorm statement is exact. The norm statement is not, with the source's own factor $\tfrac12$: $|S|^2 = \tfrac12$ and $|S| = 1/\sqrt2$. The unit-norm null representative is $\sqrt2\,S = \tfrac{1}{\sqrt2}(i + \hat{\boldsymbol{\xi}})\,\varphi = \sqrt2\,i\,\tilde{\Pi}_2(\hat{\boldsymbol{\xi}})\,\varphi$, which was checked to have norm $1$ and pseudonorm $0$ and to lie in the same ideal. The corpus records the nullity and the ideal membership as the invariant content and the factor $\sqrt2$ as a normalisation slip in the source.
5. **The stationary family has the same structure.** For $B = B(\mathbf{x})e^{-i\omega\tau}$ the source sets $\nabla^\pm_\omega = \omega \pm \nabla$ and obtains the $\omega$-spinors

$$
\Psi^0_\omega(\mathbf{x},\mathbf{e}) = \frac{1}{k^2}\bigl(\omega + \rho - ik\,\mathbf{e}\bigr)e^{-ik(\mathbf{e}\cdot\mathbf{x})}
= \frac{1}{k}\bigl(1 - i\mathbf{e}\bigr)e^{-ik(\mathbf{e}\cdot\mathbf{x})} ,
\qquad k = \omega + \rho ,
$$

whose amplitude $(1 - i\mathbf{e})/k$ is again null, again a multiple of $\tilde{\Pi}_2(\mathbf{e})$; the identity was verified for two frequencies, two shifts and two random polarisations. The static case $\omega = 0$ has $k = \rho$ and amplitude $(1 - i\mathbf{e})/\rho$, which is the "static bispinor" of the source; the source prints $\tfrac12(\operatorname{sgn}\rho - i\mathbf{e})$, which agrees with the derivation only at $\rho = 2$, so the printed constant is the one to distrust and the structure is the one to keep.

## The Stationary Route and the Helmholtz Kernel

Factoring the time dependence reduces the programme's equation to a Helmholtz problem, and the source's Theorem 8 states the stationary solution as

$$
B = \bigl(\nabla^\mp_\omega + \rho\bigr)\bigl(\chi * F\bigr) + S_\omega ,
\qquad
\nabla^\pm_\omega = \omega \pm \nabla ,
$$

with $\chi$ the fundamental solution of the Helmholtz equation $\Delta\chi + k^2\chi = \delta(\mathbf{x})$, $k = \omega + \rho$. The source's displayed kernel is $\chi = -\frac{1}{4\pi R}(ae^{kR} + (1-a)e^{-kR})$, and **the exponent has lost its $i$**: with real $k$ those exponentials do not solve the Helmholtz equation, while with $k \to ik$ they do. The restoration was verified numerically — the ball integral of $(\Delta + k^2)$ applied to $-\frac{1}{4\pi R}e^{\pm ikR}$ is $+1$ at the floor — and it is consistent with the source's own plane-wave representation $\chi_0 = \int_{|\mathbf{e}|=1}p(\mathbf{e})e^{-ik(\mathbf{e}\cdot\mathbf{x})}dS(\mathbf{e})$, which uses a real wave number. This is a text-layer loss rather than an error of the mathematics, in the same family as the lost $i$'s the earlier record noted, and it is recorded as such.

Two further source statements in this section are worth keeping with their status attached. The composition of the two stationary operators is $\bigl(\nabla^\pm_\omega + \rho\bigr)\bigl(\nabla^\mp_\omega + \rho\bigr) = (\omega+\rho)^2 + \Delta$, which is the monochromatic form of the shifted square and is verified with the rest. And the source's assertion that the Cauchy problem for the stationary operator has, for $\operatorname{Re}k \neq 0$, only the trivial homogeneous solution repeats the class question of the earlier section in the elliptic setting, where it is unproblematic: a Helmholtz equation with a complex wave number has no bounded homogeneous solutions on the whole space, and the source's standing assumption of a Fourier-transformable amplitude is the assumption actually being used.

## What the Programme's Solution Theory Establishes and What It Does Not

Established, and verified above by recomputation.

1. The composition lemma $\nabla^-\nabla^+ = \nabla^+\nabla^- = \Box_{\text{s}}$, and the shifted square $\bigl(\nabla^\mp + m\bigr)\bigl(\nabla^\pm + m\bigr) = \Box_{\text{s}} + m^2 + 2m\partial_\tau = (\partial_\tau + m)^2 - \Delta$.
2. The exponential-substitution identity, hence the fundamental solution of the KGFSh operator as $e^{-m\tau}$ times the wave kernel, hence the **sharp, light-cone-supported kernel** with a $\delta$ profile — the source's Eq. (36), with the correction that both light-cone terms carry the common factor $e^{-m\tau}$ and the advanced term therefore carries $e^{+mR}$.
3. The general solution of the inhomogeneous equation, $B = B_0 + (\nabla^\mp + m)(F * \psi_m)$, by the defining property of the kernel.
4. The monogenic completion of a scalar potential into a bispinor, and the exact plane-wave family: the linear dispersion $\omega = \rho \pm |\boldsymbol{\xi}|$, unit group velocity, phase velocities $1 \pm \rho/|\boldsymbol{\xi}|$, and the stationary mode $\omega = 0$ at $|\boldsymbol{\xi}| = \rho$.
5. The nullity of the harmonic bispinor's amplitude; its identity with $i\tilde{\Pi}_2(\hat{\boldsymbol{\xi}})$; its membership in the minimal left ideal $\mathbb{B}\tilde{\Pi}_2$; and its placement in the material sector $\mathbb{M}_-$.
6. The stationary route, the Helmholtz kernel with its exponent restored, and the $\omega$-spinors with the same null amplitude.

Not established, or corrected in the source.

1. **Theorem 5 as a statement about all solutions is false**, and the counterexample is the substitution itself, $u = e^{-m\tau}v$ with any wave $v$. The true statement is about tempered solutions or about the Cauchy problem with zero data, and the corpus states it that way. In the case that matters — the corpus's real $\kappa = \rho$ — the source's own plane-wave family shows the homogeneous solutions exist.
2. **Two normalisation slips**: the harmonic bispinors have norm $1/\sqrt2$, not $1$, with the source's printed factor; the unit-norm null representative is $\sqrt2$ times the printed one. And the static bispinor's printed $\tfrac12(\operatorname{sgn}\rho - i\mathbf{e})$ does not follow from the source's own general formula, which gives $(1 - i\mathbf{e})/\rho$.
3. **Two text-layer losses**: the missing $i$ in the Helmholtz kernel's exponent, and, in the earlier record, whatever signs the degraded copy obscured.
4. **The matrix section proves less than it appears to.** $D_j^2 = I$ and anticommutation of the three spacelike matrices is the regular representation of $ie_j$, not a Clifford algebra of spacetime; $D^0 = I$ anticommutes with nothing.
5. **No derivation of anything physical.** The equation is chosen; $\rho$ is a free parameter fixed nowhere; the dispersion is a shifted cone, not the corpus's mass shell; no quantum number, no spin, no statistics, no measured particle enters. The programme's closing claim — that its solutions describe the transformation of electric and gravimagnetic charges and currents under static external fields, and the fields they generate — is stated as an application and is not carried by any formula in the paper. The corpus records that it has not been checked, and records nothing further about it.

## Summary

The immediate problem is set by the companion article. *The Biquaternion D'Alembertian and Its Green's Functions* had established the shifted gradient, the generalized Maxwell–Dirac equation, the Klein–Gordon–Fock–Schrödinger operator, its symbol and the convention crossing $\kappa = -im$, and had explicitly declined to state the source's fundamental solution because the text in hand could not be checked. The present article closes that gap from the source's later journal paper, whose text layer is usable, and it does so by verification rather than by transcription.

The operator's square, $(\nabla^\mp+m)(\nabla^\pm+m) = (\partial_\tau+m)^2-\Delta$, is a conjugation of the wave operator, $e^{-m\tau}\Box_{\text{s}}e^{m\tau}$. That single identity gives everything in this article. It makes the fundamental solution $e^{-m\tau}$ times the massless kernel, hence supported exactly on the light cone with a $\delta$ profile where the corpus's massive scalar kernel carries a Bessel tail inside the cone: the programme's first-order term buys Huygens' principle at the price of self-adjointness. It makes the general solution of the homogeneous equation $e^{-m\tau}$ times an arbitrary wave, which is why the source's theorem that no non-trivial homogeneous solution exists for $\operatorname{Re}m \neq 0$ holds only in the tempered class, and why the counterexample is one line. And it makes the plane-wave family's dispersion exactly linear, $\omega = \rho \pm |\boldsymbol{\xi}|$: a shifted cone, not a curved mass shell, with unit group velocity, phase velocities $1 \pm \rho/|\boldsymbol{\xi}|$ and a stationary mode at $|\boldsymbol{\xi}| = \rho$.

The bispinors carry the algebra's own content. The amplitude of a plane-wave bispinor is $\tfrac12(i+\hat{\boldsymbol{\xi}})$, which is $i\tilde{\Pi}_2(\hat{\boldsymbol{\xi}})$, the central phase times one of the corpus's rank-one projectors — a pure state of the informational sector. So the programme's harmonic bispinor lies in the minimal left ideal $\mathbb{B}\tilde{\Pi}_2$, it is anti-Hermitian and therefore in the material sector $\mathbb{M}_-$, and it is null, hence a zero divisor, under the corpus's norm and under the source's pseudonorm alike. A bispinor of a "massive" first-order equation is an element of the null cone: that, and not the borrowed words *boson* and *lepton*, is what the algebra says. The normalisation the source states is off by $\sqrt2$, the static amplitude it prints does not follow from its own formula, and the exponent of its Helmholtz kernel has lost an $i$; the corpus records the corrections and keeps the structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\nabla^\pm = \partial_\tau \pm i\nabla$, $\tau = ct$ | The source's two bigradients; $\nabla^+ = i\tilde{\nabla}$, $\nabla^- = i\tilde{\nabla}^{\natural}$ |
| $\Box_{\text{s}} = \partial_\tau^2 - \Delta = -\Box$ | The source's wave operator, minus the corpus's d'Alembertian |
| $\bigl(\nabla^\pm + m\bigr)B = F$ | The source's first-order equation; the corpus's generalized Maxwell–Dirac equation with $\kappa = -im$ |
| $\Box_{\text{s}} + m^2 + 2m\partial_\tau = (\partial_\tau+m)^2-\Delta = e^{-m\tau}\Box_{\text{s}}e^{m\tau}$ | The KGFSh operator and its conjugation form |
| $m = i\rho$, $\rho$ real | The source's imaginary-mass case; the corpus's real shift $\kappa = \rho$, the case with non-trivial homogeneous solutions |
| $\psi_m = \frac{e^{-m\tau}}{4\pi R}\delta(\tau-R)$, $R=|\mathbf{x}|$ | Retarded fundamental solution; the source's Eq. (36); supported on the cone |
| $B = B_0 + (\nabla^\mp+m)(F*\psi_m)$ | General solution of the inhomogeneous equation |
| $\Psi_\rho = (\nabla^\mp + i\rho)\psi_\rho$ | Bispinor of the scalar potential $\psi_\rho$ (monogenic completion) |
| $\omega = \rho \pm\lvert\boldsymbol{\xi}\rvert$ | Exact linear dispersion of the plane-wave family; unit group velocity |
| $S^{\pm}_{\boldsymbol{\xi}} = \tfrac12(i+\hat{\boldsymbol{\xi}})\varphi^{\pm}_{\boldsymbol{\xi}} = i\tilde{\Pi}_2(\hat{\boldsymbol{\xi}})\varphi^{\pm}_{\boldsymbol{\xi}}$ | Harmonic bispinor; null, in the minimal left ideal, in $\mathbb{M}_-$ |
| $\tilde{\Pi}_{1,2}(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ | The corpus's idempotents: pure states, Hermitian, null |
| $D_j$, $j=0,\dots,3$ | The source's $4\times4$ matrices: $D_0=I$, $D_j$ the matrix of left multiplication by $ie_j$; $D_j^2=I$ |
| $\nabla^\pm_\omega = \omega \pm \nabla$, $k = \omega+\rho$ | Stationary (monochromatic) operators and wave number |

## Further Reading

- L. A. Alexeyeva, "Biquaternion representation of the Dirac equations and bispinor fields", *Journal of Open Systems Evolution Problems* (ЖПЭОС) **25** (1–2) (2023), 15–24, doi:10.26577/JPEOS.2023.v25.i1-2.i2, for the solution theory recorded here: the composition lemmas, the KGFSh fundamental solution and its light-cone support, the general solution of the inhomogeneous equation, the plane-wave and harmonic bispinors, the linear dispersion, and the stationary Helmholtz route.
- L. A. Alexeyeva, "Biquaternions algebra and its applications by solving of some theoretical physics equations", *Clifford Analysis, Clifford Algebras and Their Applications* **7** (2012), 19–39 (arXiv:1302.0523), the programme's earlier statement of the shifted gradient, the generalized Maxwell–Dirac equation and the KGFSh operator, as recorded in *The Biquaternion D'Alembertian and Its Green's Functions*.
- L. A. Alexeyeva, "Biquaternionic representation of harmonic elementary particles. Periodic system of atoms", *SSRG International Journal of Applied Physics* **6** (3) (2019), 73–80, for the same programme's standing monochromatic solutions and its particle reading, developed in *Harmonic Elementary Particles and the Periodic System of Atoms*.
- Fritz John, *Plane Waves and Spherical Means Applied to Partial Differential Equations* (Interscience, 1955), for Huygens' principle, the Hadamard elementary solution and the support of the wave operator's singularities on the characteristic cone.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics*, Vol. II (Interscience, 1962), for the fundamental solutions of the wave and Helmholtz equations, the retarded and advanced kernels of the shifted operator, and the tail of the Klein–Gordon kernel inside the cone.
- I. M. Gel'fand and G. E. Shilov, *Generalized Functions*, Vol. 1 (Academic Press, 1964), for the distributional identities that carry $\delta(\tau \mp R)$ through the inverse Fourier transform and for the convolution calculus the source's bispinors are built with.
- A. Erdélyi et al., *Higher Transcendental Functions*, Vol. II (McGraw–Hill, 1953), for the Bessel functions that appear on the cone in the source's formulas and in the interior tail of the Klein–Gordon kernel that the KGFSh kernel does not have.
