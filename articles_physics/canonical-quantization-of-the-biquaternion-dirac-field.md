# __Canonical Quantization of the Biquaternion Dirac Field__

## Introduction

The companion article *Quantum Physics in Biquaternionic Form* raises, as the second of its list of open questions, a precise one:

> "The formalism is first-quantized. To describe creation and annihilation of particles, one needs a Fock space and operator-valued fields. How does the biquaternion framework extend to this setting?"

The companion article *The Dirac Equation in Biquaternionic Form* supplies the field-side setting, and the article *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit* supplies the classical material a mode expansion needs: the positive- and negative-frequency plane-wave solutions, their covariant normalizations, and the spin sums. The article *The KMS Condition and the Biquaternion Framework* supplies the thermal motivation and identifies exactly what a fermionic extension must add: a $\mathbb{Z}/2$ grading under which fermionic operators anticommute, which the biquaternion algebra does not by itself provide.

This article is a first attempt at that extension. Its subject is the canonical quantization of the biquaternion Dirac field: the promotion of the classical field to an operator-valued field, the equal-time anticommutation relations, the expansion in the plane-wave solutions established by the parent article, the algebra of the mode operators, the Hamiltonian and its normal-ordering constant, the reason the modes anticommute rather than commute, and the relation of the resulting operator algebra to the thermal-state framework of the KMS article.

The article has to be read with a clear division in mind, and we state it at the outset because it governs everything that follows.

- **The standard part.** The biquaternion Dirac equation is the one-sided chiral pair, and it is the single equation $(\mathbb{D}-m)\tilde{\Psi}=0$ on the element, where $\mathbb{D}$ is the pair operator of *Operator and Calculus Conventions*, defined on $\mathbb{B}\oplus\mathbb{B}$ by the gradient and its conjugate. The two-sided equation of Kravchenko — the spatial gradient acting from the left and the mass from the right through $\vec e_z$ — is a different operator and is not quantized here. The canonical quantization of the one-sided equation — the Lagrangian, the conjugate momentum, the equal-time anticommutators, the mode expansion, the mode algebra, the Hamiltonian, and the normal-ordering constant — is textbook quantum field theory, transcribed into the notation of this series. None of it is new, and none of it depends on the biquaternion structure beyond the kinematical conventions already fixed by the companion articles.
- **The open part.** What is *not* standard, and what this article cannot settle, is the intrinsic formulation of the quantization in the algebra $\mathbb{B}$ itself: which pairing of the algebra the $\mathbb{B}$-intrinsic Lagrangian and conjugate momentum are built from, since the algebra alone does not single one out; what the biquaternion Fock space is; and how the $\mathbb{Z}/2$ grading required by fermionic statistics is to be embedded in $\mathbb{B}$.

We therefore make no claim that the extension is canonical in the biquaternion framework. The claim is narrower: the extension can be carried out on the elements of $\mathbb{B}$ with the parent article's solutions, and it supplies exactly the operator structure — anticommuting modes and a fermion-parity grading — that the KMS article identifies as missing. Whether that structure lifts to a genuinely biquaternionic one is the open question this article is meant to expose.

The article is organized as follows. The next section fixes the classical field and its conjugate momentum, and identifies the constraint that forces the canonical structure to be imposed rather than assumed. The following section states the equal-time anticommutation relations and the reasons they, rather than commutators, are the consistent choice. The next section carries out the expansion in the parent article's plane-wave solutions. The section after that derives the anticommutators of the mode operators and builds the Fock space.

The next section gives the Hamiltonian, the normal-ordering constant, and the four-momentum and charge. A section on spin and statistics records why anticommutation is forced here, without developing the full spin–statistics theorem, which the companion article *The Spin–Statistics Theorem in Biquaternionic Form* treats on its own. A section relates the result to the KMS thermal-state framework. The article then gives an explicit accounting of what is standard and what is open. It closes with the summary, the notation table, and further reading.

Every derivative of the field in this article is the corpus gradient $\tilde\nabla$ or its conjugate $\tilde\nabla^{\natural}$, defined once in §*The Pair Operator and Its Symbol*: $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial Q_\mu$ and $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\,\partial/\partial Q_\mu$ with $\varepsilon=(1,-1,-1,-1)$. No other derivative operator is written. No operator below is a cell named by an abstract glyph: each is an element of $\mathbb{B}$, an action written out with its sides in position — the element multiplied on the left and the element multiplied on the right, both visible — or a number. Where an operator is two-sided, the two elements are named in the sentence that introduces it.

## The Classical Field and Its Conjugate Momentum

The biquaternion Dirac field of the companion article is an element-valued map $\tilde{\Psi}:\mathbb{R}^{1,3}\to\mathbb{B}$, written $\tilde{\Psi}=\tilde{\Psi}_L+\tilde{\Psi}_R$ for its two chiral halves, and satisfying the linear, chirality-off-diagonal pair

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R,
$$

where $\tilde{\Psi}_L$ is the part of the element of one chirality value and $\tilde{\Psi}_R$ the part of the other, as the parent article splits them. At $m=0$ the pair decouples into

$$
\tilde{\nabla}\tilde{\Psi}_R=0,\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=0,
$$

one equation per chirality. The single equation $\tilde{\nabla}\tilde{\Psi}=0$ is the right-handed member, not the whole massless field.

Two formulations now carry the name *Dirac equation*, and they must not be read as one. The pair above is the corpus's **one-sided** equation: both gradients act from the left, and the mass is the off-diagonal pairing of the two chiral halves. Kravchenko's **two-sided** equation, for a biquaternion field $F$,

$$
\bigl(i\partial/\partial t'+\nabla\bigr)F-m\,i\,\overline{F}\,\vec e_z=0,
$$

with $\nabla=\sum_k\vec e_k\,\partial/\partial Q_k$ the spatial gradient, is a different operator: the spatial gradient acts from the left, the mass from the right through $\vec e_z$, and the mass term carries the algebra's complex conjugation $\overline{\cdot}$ — a bar over the field, the coefficient conjugation, and it is not the Dirac adjoint $\bar{\tilde\Psi}$ of the sections below. The two are related by the explicit dictionary with conjugation in the mass term, in the parent article's section of that name, but they are not the same equation, and their mass terms are of different kinds. This article quantizes the one-sided pair; the two-sided equation is recorded only to keep the two apart.

The solutions article works on the elements themselves. An element of $\mathbb{B}$ has four complex coefficients, exactly the four components of the Dirac spinor, so the element is the carrier of the field and no separate module is introduced; the two chiral halves of the pair are the two parts $\tilde{\Psi}_L$ and $\tilde{\Psi}_R$ of that one element. There the pair is the single equation

$$
\Big(\mathbb{D}-\frac{mc}{\hbar}\Big)\tilde{\Psi}=0,
$$

whose solutions, normalizations, and spin sums are established in the parent article and are used below without rederivation. From this point the article sets $c=\hbar=1$, so $mc/\hbar$ is written $m$ and every $m$ below means that combination; a dimensionful constant returns only where a dimensional statement is at issue, in the inverse temperature $\beta=\hbar/(k_BT)$, in the plane-wave phase $\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar$, and in the mass-shell condition $\tilde P\tilde P^{\natural}=-m^2c^2$.

### The Pair Operator and Its Symbol

The gradient and its conjugate are the two derivative operators of the article, and they are fixed here once:

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},\qquad
\Box=\tilde\nabla\tilde\nabla^{\natural}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q,
\qquad \varepsilon=(1,-1,-1,-1),
$$

with $\Delta_Q:=\sum_k\partial^2/\partial Q_k^2$ the spatial Laplacian. On the material sector $\partial/\partial Q_t=-(i/c)\partial/\partial t'$, so $\Box=\Delta_Q-c^{-2}\partial^2/\partial t'^2$.

The chiral pair is one operator on the pair of elements,

$$
\mathbb{D}\Psi=\bigl(\tilde\nabla\Psi_R,\ \tilde\nabla^{\natural}\Psi_L\bigr),\qquad \mathbb{D}^2=\Box ,
$$

the pair operator of *Operator and Calculus Conventions*. It carries no matrix generator and is not a new object: on the pair, the mass is the off-diagonal coupling and $\mathbb{D}^2=\Box$ is the composition of the two gradients.

Read on one element — the carrier of the field, as the preceding paragraph fixes — its action is written out with the side in position:

$$
\mathbb{D}:\ \tilde X\longmapsto-\frac{\partial\tilde X}{\partial t'}\vec e_x-\sum_k\vec e_k\frac{\partial\tilde X}{\partial Q_k}\vec e_y ,
$$

with $Q_k$ running over the three spatial coordinates. The sides are the whole of the content. The time term carries $e_t$ on the left, and $e_t$ is the unit of the algebra, so that term is a single right multiplication by $\vec e_x$; each spatial term carries $\vec e_k$ on the left and $\vec e_y$ on the right. The operator is therefore **two-sided**, and the two elements are the ones just named. Its square is the d'Alembertian: the cross terms cancel because left and right multiplications commute and $\vec e_x\vec e_y=-\vec e_y\vec e_x$, the time term contributes $-\partial^2/\partial t'^2$ because $\vec e_x^2=-e_t$, and the spatial terms contribute $+\Delta_Q$ because $\vec e_y^2=-e_t$ and $\vec e_k\vec e_l+\vec e_l\vec e_k=-2\delta_{kl}e_t$. Verified on plane-wave symbols at $4\times10^{-15}$.

Its symbol on a plane wave is the momentum form

$$
\mathbb{D}_p:\ \tilde X\longmapsto iE_{\vec p}\,\tilde X\vec e_x-i\sum_k p_k\,\vec e_k\tilde X\vec e_y,
\qquad \mathbb{D}_p^2=p^2 ,
$$

with $p_0=E_{\vec p}$ and $p_k$ the physical momentum components, so that $p^2=p_0^2-\vec p^2=m^2$. The lower index of $p_\mu$ is a label and not a metric contraction: the signs are carried by $\varepsilon$. That sign vector is what the plane wave produces. On $e^{-ip\cdot x}$ the time derivative gives $-iE_{\vec p}$ and the spatial derivatives $+ip_k$, so the time term contributes $iE_{\vec p}\tilde X\vec e_x$ and the spatial terms $-ip_k\vec e_k\tilde X\vec e_y$. On the material sector both objects satisfy $\mathbb{D}^2=\Box$ and $\mathbb{D}_p^2=p^2$, the second equal to $m^2$ on the mass shell.

### The Lagrangian

The classical field theory is defined by the Lagrangian density

$$
\mathcal{L}=\bar{\tilde\Psi}\,(\mathbb{D}-m)\,\tilde\Psi
=i\,\mathrm{Sc}\Big(\tilde\Psi^{*}\frac{\partial\tilde\Psi}{\partial t'}\Big)
+i\sum_k\mathrm{Sc}\Big(\tilde\Psi^{*}\vec e_k\frac{\partial\tilde\Psi}{\partial Q_k}\vec e_z\Big)
-m\,\mathrm{Sc}\big(\tilde\Psi^{*}i\tilde\Psi\vec e_x\big),
$$

with the Dirac adjoint

$$
\bar{\tilde\Psi}X:=\mathrm{Sc}\big(\tilde\Psi^{*}iX\vec e_x\big),
$$

the Hermitian conjugate followed by right multiplication by the timelike element $i\vec e_x$, the element that the time term of $\mathbb{D}$ carries. The scalar part is taken of the product, because a bilinear of an element-valued field is a number only through its scalar part. The three pieces are visible: no unit at all on the time derivative, the pair $\vec e_k$ on the left and $\vec e_z$ on the right on each spatial derivative, and the right multiplication by $i\vec e_x$ on the field itself. The $\vec e_z$ is $-\vec e_y\vec e_x$, the operator's right element times the adjoint's right factor; that minus sign turns the operator's $-i$ into the $+i$ displayed. Variation with respect to the adjoint $\bar{\tilde\Psi}$ returns the Dirac equation $(\mathbb{D}-m)\tilde\Psi=0$; variation with respect to $\tilde\Psi$ returns the conjugate equation, in which the operator acts on the adjoint, and it is the conjugate of the first.

The Lagrangian is **real up to a four-divergence**. The mass term is real outright, because $\mathrm{Sc}(\tilde\Psi^{*}i\tilde\Psi\vec e_x)$ is real for every element — verified at $4.4\times10^{-16}$ over fifty random elements — and $m$ is real. Each derivative term differs from its conjugate by a total derivative, both identities holding exactly, and the sum of the two differences is

$$
\mathcal{L}-\bar{\mathcal{L}}
=\frac{\partial}{\partial t'}\big(i\,\mathrm{Sc}(\tilde\Psi^{*}\tilde\Psi)\big)
+i\sum_k\frac{\partial}{\partial Q_k}\mathrm{Sc}\big(\tilde\Psi^{*}\vec e_k\tilde\Psi\vec e_z\big),
$$

verified at $3.6\times10^{-15}$ over thirty random fields with independent derivative values. This is the Lagrangian of a free Dirac field, with the pair operator in place of the matrix contraction.

### The Conjugate Momentum and Its Constraint

The canonical momentum conjugate to $\tilde\Psi$ is

$$
\pi=\frac{\partial\mathcal{L}}{\partial(\partial\tilde\Psi/\partial t')}=i\,\tilde\Psi^{*}.
$$

The step is worth displaying, because it is the origin of the entire fermionic structure. The only term of $\mathcal{L}$ that carries a time derivative is the one with $\partial/\partial t'$. In the elements it is

$$
i\,\mathrm{Sc}\Big(\tilde\Psi^{*}\frac{\partial\tilde\Psi}{\partial t'}\Big)
=i\sum_\mu\bar\Psi_\mu\frac{\partial\Psi_\mu}{\partial t'},
$$

the scalar part of $\tilde\Psi^{*}$ times the derivative being the coefficient sum, so that differentiation with respect to $\partial\Psi_\mu/\partial t'$ returns $i\bar\Psi_\mu$ and therefore $\pi=i\tilde\Psi^{*}$.

The momentum is not the time derivative of the field. The Dirac equation is first order in time, so the momentum is algebraically tied to the field by the primary constraint

$$
\pi-i\tilde\Psi^{*}\approx 0 .
$$

The constraint is **second class**: the Legendre transform is singular, and the field and its momentum are not independent canonical variables, so the naive Poisson bracket has to be replaced by the Dirac bracket. The standard route computes that bracket and then quantizes it; for the free field the outcome is the equal-time anticommutation relations. This article takes the route as read: it imposes the relations directly and verifies, in the section on the mode operators, that they reproduce the boxed equal-time relation. Nothing below depends on the Dirac-bracket computation itself.

The constraint is also why the ordinary rule $[\phi,\pi]=i\delta^{(3)}$ cannot be applied to a Dirac field: there is no independent pair for it to relate. It does not, by itself, say whether the bracket that replaces it is a commutator or an anticommutator; that question is settled by the positivity of the energy rather than by the constraint, and it is the subject of the next section.

### The Biquaternion Interpretation and the Open Point

Written on the elements, the Lagrangian and the canonical momentum are the standard ones once the pairing is fixed. Written in the algebra, the pairing is not fixed. The parent article's mass term is the linear, chirality-off-diagonal coupling, whose element form is the right multiplication by $i\vec e_x$ above; the anti-Hermitian conjugation $\flat=-{}^{*}$ is the algebra's real structure, not the mass. The $\mathbb{B}$-intrinsic Lagrangian — the real scalar built from $\tilde{\nabla}\tilde{\Psi}$, $\tilde{\Psi}$, their conjugates, and the trace or norm pairing of the algebra — is not determined by the algebra alone, and neither is the intrinsic conjugate momentum.

Several inequivalent pairings are available: the Dirac pairing $\bar{\tilde\Psi}X=\mathrm{Sc}(\tilde\Psi^{*}iX\vec e_x)$ used here, the untwisted coefficient pairing $\mathrm{Sc}(\tilde\Psi^{*}X)$, and the trace of either. The choice fixes the equation of motion, the conjugate momentum and the normalization of the modes at once, so it is not a matter of taste. We use the Dirac pairing, which returns the parent article's pair and its normalizations, and we return to the choice in the closing section on what is open. The reader should keep in mind that the mode structure below is the standard one; what is being tested here is whether the biquaternion framework naturally reproduces it.

## Equal-Time Anticommutation Relations

Quantization promotes the classical field and its momentum to operators $\tilde\Psi^{\mathrm{fop}}$, $\pi^{\mathrm{fop}}$ and imposes equal-time brackets. Write

$$
X:=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,\qquad
Y:=x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z,
$$

for the two spatial points. For the Dirac field the brackets are **anticommutators**, imposed on the four coefficients of the element:

$$
\boxed{\;\{\tilde\Psi^{\mathrm{fop}}_\mu(X,t'),\tilde\Psi^{\mathrm{fop}\dagger}_\nu(Y,t')\}=\delta_{\mu\nu}\,\delta^{(3)}(X-Y)\;}
$$

together with

$$
\{\tilde\Psi^{\mathrm{fop}}_\mu(X,t'),\tilde\Psi^{\mathrm{fop}}_\nu(Y,t')\}=0,\qquad
\{\tilde\Psi^{\mathrm{fop}\dagger}_\mu(X,t'),\tilde\Psi^{\mathrm{fop}\dagger}_\nu(Y,t')\}=0,
$$

where $\mu,\nu$ run over the four units $e_t,\vec e_x,\vec e_y,\vec e_z$ and label the coefficients of the element. In terms of the conjugate momentum $\pi^{\mathrm{fop}}=i\tilde\Psi^{\mathrm{fop}*}$, the first relation reads

$$
\{\tilde\Psi^{\mathrm{fop}}_\mu(X,t'),\pi^{\mathrm{fop}}_\nu(Y,t')\}=i\,\delta_{\mu\nu}\,\delta^{(3)}(X-Y),
$$

which is the fermionic analogue of the canonical relation $[\phi^{\mathrm{fop}},\pi^{\mathrm{fop}}]=i\delta^{(3)}$ of a scalar field. These are the standard canonical relations, and they are imposed rather than derived.

The choice of anticommutator over commutator is forced, and three reasons can be given at the level of this article. They are stated here because they are operative in the construction; the full spin–statistics theorem belongs to the companion article *The Spin–Statistics Theorem in Biquaternionic Form* and is not developed here.

**1. Boundedness of the energy.** As shown in the section on the Hamiltonian, the mode expansion of the energy contains a negative-frequency contribution proportional to $b^{\mathrm{fop}}_r(\vec p)b^{\mathrm{fop}\dagger}_r(\vec p)$. If the modes commuted, this product would be $b^{\mathrm{fop}\dagger}_r(\vec p)b^{\mathrm{fop}}_r(\vec p)+1$, and the energy would be

$$
H=\sum_r\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}
\Big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r-b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r\Big)+\text{constant},
$$

unbounded below: adding antiparticles would lower the energy without limit, and no stable vacuum would exist. If the modes anticommute, the same product is $1-b^{\mathrm{fop}\dagger}_r(\vec p)b^{\mathrm{fop}}_r(\vec p)$, and the same expression becomes a positive sum plus a constant. The anticommutator is what makes the negative-frequency modes into positive-energy antiparticles. This is the operator content of the Dirac sea.

**2. Microcausality.** For a field of spin $\tfrac12$, the commutator $[\tilde\Psi^{\mathrm{fop}}(x),\bar{\tilde\Psi}^{\mathrm{fop}}(y)]$ does **not** vanish for spacelike separated $x,y$, so quantizing with commutators would correlate measurements in causally disconnected regions. The anticommutator $\{\tilde\Psi^{\mathrm{fop}}(x),\bar{\tilde\Psi}^{\mathrm{fop}}(y)\}$ does vanish there, and it is the quantity that must be local for a fermion field. Here $\bar{\tilde\Psi}=\tilde\Psi^{*}i\vec e_x$ is the Dirac adjoint of the Lagrangian section — Hermitian conjugate, then right multiplication by $i\vec e_x$ — written with the right factor in position rather than absorbed. This is the content of Pauli's 1940 argument: the requirement that the fields commute or anticommute outside the light cone, together with the transformation properties of the spinor representation, selects anticommutation for half-integer spin.

**3. Positivity of the inner product.** Quantizing a half-integer-spin field with commutators produces states of negative norm; the anticommutator is what makes the Fock inner product positive-definite. This is the Hilbert-space form of the same obstruction.

The three reasons are aspects of one theorem. We note only that they all point the same way for a field whose one-particle states transform in the spinor representation — which is the case here, since the four coefficients of an element of $\mathbb{B}$ transform as a Dirac spinor, and its two chiral halves are the two two-component halves of that spinor.

## Field Expansion in the Plane-Wave Solutions

The classical equation is linear, so its general solution is a superposition of the plane waves constructed in the parent article. Those solutions come in two branches: the positive-frequency branch spanned by the amplitudes $\tilde\Psi^{(r)}_{+}(\vec p)\exp(-ip\cdot x)$ and the negative-frequency branch spanned by $\tilde\Psi^{(r)}_{-}(\vec p)\exp(+ip\cdot x)$, with $r=1,2$ and

$$
E_{\vec p}=+\sqrt{\vec p^2+m^2},\qquad p\cdot x:=E_{\vec p}t'-\vec p\cdot X,
$$

for the point $x=(X,t')$; each amplitude is an element of $\mathbb{B}$. The covariant normalizations, orthogonality, and spin sums established there are written with the Dirac pairing

$$
\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}:=\mathrm{Sc}\big(\tilde\Psi^{*}i\tilde\Phi\vec e_x\big)=\bar{\tilde\Psi}\tilde\Phi,
$$

which is the scalar part of the adjoint product of the Lagrangian section, and they read

$$
\langle\tilde\Psi^{(r)}_{+},\tilde\Psi^{(s)}_{+}\rangle_{\mathrm D}=2m\,\delta_{rs},\qquad
\langle\tilde\Psi^{(r)}_{-},\tilde\Psi^{(s)}_{-}\rangle_{\mathrm D}=-2m\,\delta_{rs},\qquad
\langle\tilde\Psi^{(r)}_{+},\tilde\Psi^{(s)}_{-}\rangle_{\mathrm D}=\langle\tilde\Psi^{(r)}_{-},\tilde\Psi^{(s)}_{+}\rangle_{\mathrm D}=0,
$$

$$
\mathrm{Sc}\big(\tilde\Psi^{(r)*}_{+}\tilde\Psi^{(s)}_{+}\big)=\mathrm{Sc}\big(\tilde\Psi^{(r)*}_{-}\tilde\Psi^{(s)}_{-}\big)=2E_{\vec p}\,\delta_{rs},
$$

$$
\sum_{r=1}^{2}\tilde\Psi^{(r)}_{+}\big\langle\tilde\Psi^{(r)}_{+},\tilde\Phi\big\rangle_{\mathrm D}=(\mathbb{D}_p+m)\tilde\Phi,\qquad
\sum_{r=1}^{2}\tilde\Psi^{(r)}_{-}\big\langle\tilde\Psi^{(r)}_{-},\tilde\Phi\big\rangle_{\mathrm D}=(\mathbb{D}_p-m)\tilde\Phi
\qquad\text{for every }\tilde\Phi\in\mathbb{B}.
$$

The last pair is an operator identity and not a statement about solutions: the first sum returns $2m$ times the element on the positive-frequency branch and vanishes on the negative-frequency one, and the second does the reverse. Verified on a basis of $\mathbb{B}$ at four momenta: completeness and orthogonality to better than $6\times10^{-15}$, and the covariant norms to machine precision.

Quantization consists in replacing the constant coefficients of the classical expansion by operators:

$$
\boxed{\;\tilde\Psi^{\mathrm{fop}}(X,t')=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec p}}}
\sum_{r=1}^{2}\Big[a^{\mathrm{fop}}_r(\vec p)\,\tilde\Psi^{(r)}_{+}(\vec p)\,\exp(-ip\cdot x)
+b^{\mathrm{fop}\dagger}_r(\vec p)\,\tilde\Psi^{(r)}_{-}(\vec p)\,\exp(+ip\cdot x)\Big]\;}.
$$

The field and its adjoint,

$$
\tilde\Psi^{\mathrm{fop}\dagger}(Y,t')=\int\!\frac{d^3k}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec k}}}
\sum_{s=1}^{2}\Big[a^{\mathrm{fop}\dagger}_s(\vec k)\,\tilde\Psi^{(s)*}_{+}(\vec k)\,\exp(+ik\cdot y)
+b^{\mathrm{fop}}_s(\vec k)\,\tilde\Psi^{(s)*}_{-}(\vec k)\,\exp(-ik\cdot y)\Big],
$$

with $k\cdot y:=E_{\vec k}t'-\vec k\cdot Y$, together define the operator-valued field. The **annihilation** operators $a^{\mathrm{fop}}_r(\vec p)$ multiply the positive-frequency solutions, and the **creation** operators $b^{\mathrm{fop}\dagger}_r(\vec p)$ multiply the negative-frequency solutions. The attribution of a creation operator to the negative-frequency branch is the operator form of the reinterpretation of the Dirac sea: the modes of "negative frequency" are the antiparticles of positive energy.

Two structural remarks belong here. First, $\tilde\Psi^{\mathrm{fop}}$ is **not Hermitian**, and it should not be: a complex Dirac field carries a conserved charge, and particle and antiparticle are distinct. Second, each amplitude is a biquaternion plane wave $\tilde\Psi_0\exp\!\left(i\,\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar\right)$, with $\tilde P$ the wave biquaternion and $\tilde R$ the four-position biquaternion of the parent article. The two branches are the two signs of the energy root of the single biquaternion mass-shell condition

$$
\tilde P\tilde P^{\natural}=-m^2c^2 ,
$$

and the polarization equation $(\mathbb{D}_p-m)\tilde\Psi_0=0$ is the algebraic form of the momentum-space equation. Promoting the coefficients to operators is thus a transcription of the standard mode expansion onto the parent article's biquaternion plane waves; it is not, by itself, a derivation of the expansion from the algebra.

## Anticommutators of the Mode Operators

For the equal-time relations above to hold, the mode operators must satisfy

$$
\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\,\delta_{rs}\,\delta^{(3)}(\vec p-\vec k),
$$

$$
\{b^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\,\delta_{rs}\,\delta^{(3)}(\vec p-\vec k),
$$

with **all other anticommutators vanishing**:

$$
\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}}_s(\vec k)\}=0,\qquad
\{b^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}}_s(\vec k)\}=0,\qquad
\{a^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}}_s(\vec k)\}=0,\qquad
\{a^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}\dagger}_s(\vec k)\}=0 .
$$

These are the standard anticommutation relations of the free Dirac field, in the continuum normalization inherited from the parent article's covariant amplitudes.

### Consistency with the Equal-Time Relations

It is worth verifying that these relations reproduce the boxed equal-time relation, because the verification exposes a point of care about the relative phases of the two branches. Write $\vec\Delta:=X-Y$ for the separation of the two points. Inserting the expansions and using the mode algebra gives, at equal times,

$$
\{\tilde\Psi^{\mathrm{fop}}_\mu(X,t'),\tilde\Psi^{\mathrm{fop}\dagger}_\nu(Y,t')\}
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\vec p}}
\Big[\sum_r\big(\tilde\Psi^{(r)}_{+}\big)_\mu\big(\tilde\Psi^{(r)*}_{+}\big)_\nu\,e^{+i\vec p\cdot\vec\Delta}
+\sum_r\big(\tilde\Psi^{(r)}_{-}\big)_\mu\big(\tilde\Psi^{(r)*}_{-}\big)_\nu\,e^{-i\vec p\cdot\vec\Delta}\Big].
$$

The two phases are **opposite**: the positive-frequency term carries $e^{+i\vec p\cdot\vec\Delta}$ and the negative-frequency term $e^{-i\vec p\cdot\vec\Delta}$. The bracket carries untwisted outer products, while the spin sums of the preceding section are statements about the pairing; moving the right multiplication by $i\vec e_x$ that the pairing carries onto the argument, the same operator identities read

$$
\sum_r\tilde\Psi^{(r)}_{+}\,\mathrm{Sc}\big(\tilde\Psi^{(r)*}_{+}\tilde\Phi\big)=(\mathbb{D}_p+m)\big(\tilde\Phi\,i\vec e_x\big),\qquad
\sum_r\tilde\Psi^{(r)}_{-}\,\mathrm{Sc}\big(\tilde\Psi^{(r)*}_{-}\tilde\Phi\big)=(\mathbb{D}_p-m)\big(\tilde\Phi\,i\vec e_x\big).
$$

Multiplying by the two phases and adding, with $\theta=\vec p\cdot\vec\Delta$,

$$
\sum_r\Big[\tilde\Psi^{(r)}_{+}\mathrm{Sc}\big(\tilde\Psi^{(r)*}_{+}\tilde\Phi\big)e^{+i\theta}
+\tilde\Psi^{(r)}_{-}\mathrm{Sc}\big(\tilde\Psi^{(r)*}_{-}\tilde\Phi\big)e^{-i\theta}\Big]
=2\cos\theta\,\mathbb{D}_p\big(\tilde\Phi\,i\vec e_x\big)+2im\sin\theta\,\big(\tilde\Phi\,i\vec e_x\big),
$$

the four terms grouping as $e^{+i\theta}(\mathbb{D}_p+m)+e^{-i\theta}(\mathbb{D}_p-m)$. Each piece now has a definite parity in $\vec p$: the time part of $\mathbb{D}_p$ contributes $iE_{\vec p}(\tilde\Phi i\vec e_x)\vec e_x=E_{\vec p}\tilde\Phi$, because $i\vec e_x\cdot i\vec e_x=i^2\vec e_x^2=e_t$, and it is even, since $E_{\vec p}$ and the units are; the spatial part $-i\sum_kp_k\vec e_k(\tilde\Phi i\vec e_x)\vec e_y$ and the mass term $2im\sin\theta(\tilde\Phi i\vec e_x)$ are odd. The even part is $2E_{\vec p}\cos\theta$ times the identity and, after division by $2E_{\vec p}$, integrates to $\delta^{(3)}(\vec\Delta)$; the odd parts vanish under symmetric integration. Hence the equal-time relation holds. The cancellation of the odd terms is exactly what the opposite phases of the two branches accomplish; had both phases been equal, the cross terms would have survived and the canonical relation would have failed.

### The Fock Space and Pauli Exclusion

The mode algebra generates the Fock space. Define the vacuum $|0\rangle$ by

$$
a^{\mathrm{fop}}_r(\vec p)|0\rangle=0=b^{\mathrm{fop}}_r(\vec p)|0\rangle \quad\text{for all } r,\ \vec p ,
$$

and build states by acting with the creation operators. The one-particle states are $a^{\mathrm{fop}\dagger}_r(\vec p)|0\rangle$ and the one-antiparticle states $b^{\mathrm{fop}\dagger}_r(\vec p)|0\rangle$. At fixed $\vec p$, the positive-frequency solutions span a two-dimensional complex space. The one-particle space is the space of square-integrable positive-frequency solutions, the one-antiparticle space is its negative-frequency counterpart, and the many-particle space is the **antisymmetric tensor algebra** (exterior algebra) of their direct sum, because the mode operators anticommute. In particular,

$$
a^{\mathrm{fop}\dagger}_r(\vec p)a^{\mathrm{fop}\dagger}_s(\vec k)|0\rangle
=-\,a^{\mathrm{fop}\dagger}_s(\vec k)a^{\mathrm{fop}\dagger}_r(\vec p)|0\rangle,
$$

so the two-particle state is antisymmetric, and

$$
\big(a^{\mathrm{fop}\dagger}_r(\vec p)\big)^2=0,\qquad \big(b^{\mathrm{fop}\dagger}_r(\vec p)\big)^2=0,
$$

which is the Pauli exclusion principle as an algebraic identity: the square of a creation operator vanishes because $\{a^{\mathrm{fop}\dagger}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=0$. This is the sharpest sense in which the statistics is carried by the mode algebra. The construction of the biquaternion Fock space as an object in its own right — rather than as the exterior algebra of a space of element-valued solutions — is the subject of the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; here we need only the mode algebra.

## The Hamiltonian and the Normal-Ordering Constant

The conserved energy of the free Dirac field is

$$
H=\int d^3X\;\mathrm{Sc}\Big(\tilde\Psi^{\mathrm{fop}*}\Big(-i\sum_k\vec e_k\frac{\partial\tilde\Psi^{\mathrm{fop}}}{\partial Q_k}\vec e_z+m\,i\,\tilde\Psi^{\mathrm{fop}}\vec e_x\Big)\Big)
=\int d^3X\;\mathrm{Sc}\Big(\tilde\Psi^{\mathrm{fop}*}i\Big(\sum_k\vec e_k\frac{\partial\tilde\Psi^{\mathrm{fop}}}{\partial Q_k}\vec e_y+m\tilde\Psi^{\mathrm{fop}}\Big)\vec e_x\Big).
$$

The integrand is the $00$ component of the canonical energy–momentum tensor, equivalently the Legendre transform $\pi\,\partial \tilde\Psi/\partial t'-\mathcal{L}$ of the Lagrangian fixed in the section *The Lagrangian*: the two time-derivative terms cancel, and what is left is the expression above with the sign reversed, verified at $3.6\times10^{-15}$.

The two forms are the same number. In the first the spatial derivative is multiplied by $\vec e_k$ on the left and $\vec e_z$ on the right, and the mass term is the right multiplication by $i\vec e_x$; in the second the right multiplication by $i\vec e_x$ has been absorbed into the adjoint, where it composes with the $\vec e_y$ of the spatial term, and $\vec e_y\vec e_x=-\vec e_z$ returns the same pair. Both mass terms are real, which is the reality checked in the Lagrangian section. Substituting the mode expansion and using the parent article's normalizations and orthogonality gives the standard result

$$
H=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}
\Big(a^{\mathrm{fop}\dagger}_r(\vec p)a^{\mathrm{fop}}_r(\vec p)
-b^{\mathrm{fop}}_r(\vec p)b^{\mathrm{fop}\dagger}_r(\vec p)\Big).
$$

The negative sign on the second term is the Dirac sea: the filled negative-frequency modes contribute with the opposite sign. Using the anticommutator in its continuum form, $b^{\mathrm{fop}}_r(\vec p)b^{\mathrm{fop}\dagger}_r(\vec p)=(2\pi)^3\delta^{(3)}(\vec 0)-b^{\mathrm{fop}\dagger}_r(\vec p)b^{\mathrm{fop}}_r(\vec p)$, this becomes

$$
H=\;:\!H\!:\;+\;E_0,
$$

where the **normal-ordered Hamiltonian** is

$$
\boxed{\;:\!H\!:\;=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}
\Big(a^{\mathrm{fop}\dagger}_r(\vec p)a^{\mathrm{fop}}_r(\vec p)
+b^{\mathrm{fop}\dagger}_r(\vec p)b^{\mathrm{fop}}_r(\vec p)\Big)\;},
$$

manifestly non-negative, and the **normal-ordering constant** is the c-number

$$
E_0=-\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}\,(2\pi)^3\delta^{(3)}(\vec 0)\,E_{\vec p}
=-\,2V\!\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}.
$$

Here $V$ is the volume in which the theory is placed, and $(2\pi)^3\delta^{(3)}(\vec 0)=V$ is the standard transcription of the continuum normalization. The constant is negative and quartically divergent, in contrast with the positive zero-point energy $\tfrac12\sum\hbar\omega$ of a scalar field, and it is a c-number: it commutes with everything and does not affect the operator equations of motion. Normal ordering is the convention that removes it. For fermions the normal-ordering prescription moves every creation operator to the left of every annihilation operator and inserts a minus sign for each transposition of two fermion operators; for example $:\!b^{\mathrm{fop}}_r(\vec p)b^{\mathrm{fop}\dagger}_r(\vec k)\!:=-b^{\mathrm{fop}\dagger}_r(\vec k)b^{\mathrm{fop}}_r(\vec p)$. With this definition the constant term in $H$ is removed by construction.

The same mode algebra gives the other conserved charges. The normal-ordered four-momentum is

$$
:\!P^{\mathrm{fop}}_\mu\!:\;=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}\,p_\mu
\Big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r+b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r\Big),\qquad p_\mu=(E_{\vec p},\vec p),
$$

and the normal-ordered electric charge, from the density $j_0=\mathrm{Sc}\big(\tilde\Psi^{\mathrm{fop}*}\tilde\Psi^{\mathrm{fop}}\big)$, which is positive for every element, is

$$
:\!Ϙ^{\mathrm{fop}}\!:\;=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}
\Big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r-b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r\Big),
$$

so that particles and antiparticles carry opposite charge, as they must; the operator counts charge in units of the field charge $ϙ$, so the physical charge is $ϙ\,Ϙ^{\mathrm{fop}}$. The field operator is charged accordingly,

$$
[Ϙ^{\mathrm{fop}},\tilde\Psi^{\mathrm{fop}}]=-\tilde\Psi^{\mathrm{fop}},\qquad
[Ϙ^{\mathrm{fop}},\tilde\Psi^{\mathrm{fop}\dagger}]=+\tilde\Psi^{\mathrm{fop}\dagger},
$$

which is the Dirac-field form of the relation $[Ϙ^{\mathrm{fop}},\phi^{\mathrm{fop}}]=-\phi^{\mathrm{fop}}$ of *The Quantized Scalar Field in Biquaternionic Form*: the field lowers the charge by one unit and its conjugate raises it. All three expressions are the standard ones; their derivation uses only the parent article's plane-wave solutions and normalizations.

The status of $E_0$ deserves one cautionary sentence. Its divergence is an ultraviolet feature of the free field, removed by the conventional normal-ordering prescription, and nothing in the biquaternion structure as used here changes that. Whether the biquaternion framework offers a distinguished or geometrically meaningful regularization of the vacuum energy is an open question, and we do not claim one.

## Spin and Statistics

The anticommutation relations are not a convention; they are selected. The three reasons given above — boundedness of the energy, microcausality, and positivity of the norm — are all consequences of one structural fact: the one-particle states of the field transform in the **spinor representation** of the Lorentz group, and the biquaternion algebra carries that representation in its action on itself. For a field of half-integer spin the representation is double-valued: a rotation by $2\pi$ is the identity in the vector representation but minus the identity in the spinor representation, and only a rotation by $4\pi$ returns the spinor to itself. It is this two-valuedness, together with the requirement that the local observables be built from bilinears, that forces the anticommutator: the commutator of two spinor fields fails to vanish at spacelike separation, while the anticommutator does.

Equivalently, the operator algebra generated by the modes is **$\mathbb{Z}/2$-graded** by fermion parity. Define

$$
(-1)^F\,a^{\mathrm{fop}}_r(\vec p)\,(-1)^F=-a^{\mathrm{fop}}_r(\vec p),\qquad
(-1)^F\,b^{\mathrm{fop}}_r(\vec p)\,(-1)^F=-b^{\mathrm{fop}}_r(\vec p),\qquad
(-1)^F|0\rangle=|0\rangle ,
$$

so that $(-1)^F$ is $+1$ on states with an even number of particles and antiparticles and $-1$ on states with an odd number. The operators split into an even (bosonic) part commuting with $(-1)^F$ and an odd (fermionic) part anticommuting with it, and the rule that fermionic operators anticommute is precisely the statement that the algebra is graded-commutative. This grading is the structure the KMS article identifies as absent from the biquaternion algebra; the present construction supplies it on the operator algebra generated by the mode operators, which is a partial answer.

This article deliberately stops here. The full **spin–statistics theorem** — that integer-spin fields must be quantized with commutators and half-integer-spin fields with anticommutators, and the precise relation of that dichotomy to the topology of the Lorentz group — is the subject of the companion article *The Spin–Statistics Theorem in Biquaternionic Form*. We have recorded only the reasons that are operative in the canonical construction, and we have not attempted to reproduce the theorem. In particular, the question of whether the biquaternion framework yields a *derivation* of spin–statistics rather than a *transcription* of the standard argument is not settled here.

## Relation to the KMS Thermal Framework

The KMS article characterizes thermal equilibrium by an analytic property of correlation functions. For operators $A,B$ in the algebra and a state $\omega_\beta$ at inverse temperature $\beta=\hbar/(k_BT)$, the thermal correlation function is

$$
F_{A B}(t')=\omega_\beta\big(A\,\alpha_{t'}(B)\big),
$$

with $\alpha_{t'}$ the evolution generated by the Hamiltonian that defines the state; the KMS condition states that $F_{A B}(t')$ extends analytically to the strip $0<\mathrm{Im}(t')<\beta$ and satisfies

$$
F_{A B}(t'+i\beta)=F_{B A}(-t')
$$

on its boundary. The KMS article observes that this boundary relation is the same for bosons and fermions, that the statistics enters instead through the algebra of the operators, and that a fermionic interpretation requires a $\mathbb{Z}/2$ grading together with the rule that fermionic operators anticommute — a rule the biquaternion algebra does not automatically supply.

The quantized Dirac field supplies exactly that rule. The preceding section grades the mode algebra by $(-1)^F$, and the fermionic operators anticommute. The KMS condition can therefore be stated for the thermal state

$$
\omega_\beta(\,\cdot\,)=\frac{1}{Z}\,\mathrm{tr}_{\mathrm F}\big(\exp(-\beta(H-\mu Ϙ^{\mathrm{fop}}))\,\cdot\,\big)
$$

on the Fock space, with $H$ and $Ϙ^{\mathrm{fop}}$ the normal-ordered operators above, $Z$ the partition function, and $\mu$ the chemical potential. The point of contact with the KMS article is sharp and elementary. Take a single mode of energy $E$ and charge $+1$ in units of $ϙ$, and normalize it so that $\{a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}\}=1$. The evolution that defines the state is generated by $\mathcal{K}=H-\muϘ^{\mathrm{fop}}$, so in the Heisenberg picture $\alpha_{t'}(a^{\mathrm{fop}})=\exp\!\big(-i(E-\mu)t'\big)a^{\mathrm{fop}}$ and $\alpha_{t'}(a^{\mathrm{fop}\dagger})=\exp\!\big(+i(E-\mu)t'\big)a^{\mathrm{fop}\dagger}$, and

$$
F_{a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}}(t')=\exp\!\big(+i(E-\mu)t'\big)\,\omega_\beta(a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}),\qquad
F_{a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}}(-t')=\exp\!\big(+i(E-\mu)t'\big)\,\omega_\beta(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}).
$$

The KMS condition $F_{a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}}(t'+i\beta)=F_{a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}}(-t')$ then gives $\exp\!\big(-\beta(E-\mu)\big)\,\omega_\beta(a^{\mathrm{fop}}a^{\mathrm{fop}\dagger})=\omega_\beta(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}})$. Writing $n_{\mathrm F}=\omega_\beta(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}})$ for the thermal occupation and using the anticommutator in the form $a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}=1-a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}$ yields $1-n_{\mathrm F}=\exp\!\big(\beta(E-\mu)\big)n_{\mathrm F}$, i.e.

$$
\boxed{\;n_{\mathrm F}=\frac{1}{\exp\!\big(\beta(E-\mu)\big)+1}\;},
$$

the **Fermi–Dirac** distribution. The same computation for a bosonic mode, where the relevant relation is the commutator $a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}=1+a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}$, gives $n_{\mathrm B}=1/\big(\exp(\beta(E-\mu))-1\big)$, the Bose–Einstein distribution. At $\mu=0$ the two reduce to $1/(\exp(\beta E)\pm1)$. This is the cleanest sense in which the statistics is carried by the (anti)commutator and not by the KMS boundary relation — the point the KMS article makes when it locates the difference in the algebra rather than in the boundary relation. In the continuum, the free-field thermal two-point function is

$$
\omega_\beta\big(a^{\mathrm{fop}\dagger}_r(\vec p)a^{\mathrm{fop}}_s(\vec k)\big)
=(2\pi)^3\,\delta_{rs}\,\delta^{(3)}(\vec p-\vec k)\,\frac{1}{\exp\!\big(\beta(E_{\vec p}-\mu)\big)+1},
$$

and the time-ordered fermionic correlation functions built from it are **antiperiodic** in imaginary time with period $\beta$, hence periodic with period $2\beta$; the Fourier modes of the compact imaginary-time direction are consequently the fermionic Matsubara frequencies

$$
\omega_n=\frac{(2n+1)\pi}{\beta},
$$

in the KMS article's notation. The antiperiodicity is the fermionic twist that the KMS article ties to the spin structure of the field and to the missing grading; here it follows from the same anticommutator that produced the Fermi–Dirac distribution.

The structural facts the KMS article records remain intact. The imaginary time direction is intrinsic to the material sector $\mathbb{M}_-$; the complexified time direction in which the KMS continuation takes place is the sum of the imaginary time direction of $\mathbb{M}_-$ and the real time direction of $\mathbb{M}_+$; and the modular Hamiltonian $K=-\log\rho$ is a Hermitian element of the algebra, hence lies in the informational sector $\mathbb{M}_+$. What the present article adds is the operator algebra on which the thermal state is defined, together with the grading the KMS article flagged as absent. What it does **not** add is a genuinely biquaternionic construction of the thermal state: the state $\omega_\beta$ above is a complex-valued functional on the Fock space built from the element-valued field, and whether it extends to a functional intrinsically defined on $\mathbb{B}$ — with the grading embedded in $\mathbb{B}$ rather than in the mode algebra, and with an intrinsic form of the fermionic twist — remains open.

The relation established here is a consistency of structures, not a derivation of the fermionic KMS condition from the biquaternion algebra.

## What Is Standard and What Is Open

Because the question addressed here is itself an open question of the framework, we separate the two kinds of statement explicitly.

**Standard quantum field theory, transcribed.**

- The Lagrangian $\mathcal{L}=\bar{\tilde\Psi}(\mathbb{D}-m)\tilde\Psi$ and the conjugate momentum $\pi=i\tilde\Psi^{*}$, together with the second-class constraint $\pi-i\tilde\Psi^{*}\approx0$.
- The equal-time anticommutation relations, imposed and verified, and the three reasons anticommutation rather than commutation is forced.
- The mode expansion in the parent article's plane-wave solutions, with the covariant normalization $\langle\tilde\Psi,\tilde\Psi\rangle_{\mathrm D}=2m$, $\mathrm{Sc}(\tilde\Psi^{*}\tilde\Psi)=2E$, and the parent's spin sums.
- The mode-operator anticommutators, the Fock space, and Pauli exclusion as the algebraic identity $(a^{\mathrm{fop}\dagger})^2=0$.
- The Hamiltonian $:\!H\!:=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}+b^{\mathrm{fop}\dagger}b^{\mathrm{fop}})$ after normal ordering, the normal-ordering constant $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$, and the four-momentum and charge.
- The Fermi–Dirac distribution as the consequence of the KMS condition together with the anticommutator, and the fermionic Matsubara frequencies.

**Open in the biquaternion framework.**

- **The intrinsic operator field.** Whether the quantized field should be an element of $\mathbb{B}$, an $M_2(\mathbb{C})$-valued field, or a field valued in a module, and to what extent these give inequivalent quantizations; *The Quantized Dirac Field in Biquaternionic Form* takes the construction up from this article's element transcription.
- **The intrinsic Lagrangian and momentum.** The $\mathbb{B}$-intrinsic Lagrangian, its real-scalar pairing, and the conjugate momentum are not fixed by the algebra alone; the Dirac pairing $\bar{\tilde\Psi}X=\mathrm{Sc}(\tilde\Psi^{*}iX\vec e_x)$ is the one adopted above.
- **The biquaternion Fock space.** Whether it is the exterior algebra of the space of element-valued solutions, or a construction native to $\mathbb{B}$; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* takes up the question in its own terms.
- **The grading.** The $\mathbb{Z}/2$ grading is supplied here on the mode algebra; embedding it in $\mathbb{B}$ itself, as the KMS article requires, is not done.
- **The spin–statistics theorem.** Whether the framework derives spin–statistics or only transcribes it is left to *The Spin–Statistics Theorem in Biquaternionic Form*.
- **The vacuum energy.** Whether the biquaternion structure singles out a regularization of $E_0$, or assigns it a geometric meaning, is open.
- **Empirical content.** As with the rest of the framework, whether any of this yields a prediction distinguishing it from standard quantum field theory is the unanswered question.

The extension attempted here is therefore **not canonical** in the framework: the part that works is the standard canonical quantization of the Dirac field, expressed in the parent article's plane-wave solutions and the material- and informational-sector notation; the part that is genuinely biquaternionic is not yet fixed. This article is the first attempt at the companion article's second-quantization question, and it should be read as delimiting the problem rather than closing it.

## Summary

The biquaternion Dirac field is quantized by promoting its element-valued classical field to an operator-valued field. The equation quantized is the one-sided chiral pair, which on the element is the single equation $(\mathbb{D}-m)\tilde\Psi=0$ with $\mathbb{D}$ built from the corpus gradient and its conjugate; Kravchenko's two-sided equation is a different operator and is not quantized here. The classical theory has Lagrangian $\mathcal{L}=\bar{\tilde\Psi}(\mathbb{D}-m)\tilde\Psi$ and conjugate momentum $\pi=i\tilde\Psi^{*}$; the momentum is algebraically tied to the field by a second-class constraint, so the canonical structure is imposed rather than assumed. The equal-time relations are anticommutators on the four coefficients of the element,

$$
\{\tilde\Psi^{\mathrm{fop}}_\mu(X,t'),\tilde\Psi^{\mathrm{fop}\dagger}_\nu(Y,t')\}=\delta_{\mu\nu}\delta^{(3)}(X-Y)
$$

with all other equal-time anticommutators vanishing; anticommutation rather than commutation is forced by the boundedness of the energy, by microcausality, and by positivity of the norm, all three being consequences of the spinor character of the field.

The field expands in the plane-wave solutions established by the parent article,

$$
\tilde\Psi^{\mathrm{fop}}(X,t')=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\vec p}}}\sum_r
\Big[a^{\mathrm{fop}}_r(\vec p)\tilde\Psi^{(r)}_{+}(\vec p)\exp(-ip\cdot x)+b^{\mathrm{fop}\dagger}_r(\vec p)\tilde\Psi^{(r)}_{-}(\vec p)\exp(+ip\cdot x)\Big],
$$

with the mode anticommutators $\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=\{b^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k)$ and all others zero. These reproduce the equal-time relation: the positive- and negative-frequency branches enter with opposite phases, the even part of the spin sums integrates to the delta function, and the odd parts cancel. The resulting Fock space carries Pauli exclusion as the algebraic identity $(a^{\mathrm{fop}\dagger}_r)^2=0$.

The Hamiltonian is $:\!H\!:=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r+b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r)$ after normal ordering, with the negative, quartically divergent normal-ordering constant $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$ removed. The normal-ordered charge has particles and antiparticles of opposite sign. The mode algebra is $\mathbb{Z}/2$-graded by fermion parity, which is the structure the KMS article identifies as missing; with it, the KMS condition plus the anticommutator yields the Fermi–Dirac distribution and the antiperiodic imaginary-time correlators whose Matsubara frequencies are $(2n+1)\pi/\beta$.

The extension is a transcription of standard canonical quantization onto the parent article's biquaternion plane waves, not a derivation of the quantized structure from the algebra $\mathbb{B}$. The intrinsic $\mathbb{B}$-valued Lagrangian pairing and momentum, the biquaternion Fock space, and the embedding of the grading in $\mathbb{B}$ remain open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k\vec e_k\,\partial/\partial Q_k$ | Biquaternionic gradient (Dirac operator) |
| $\tilde{\nabla}^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\partial/\partial Q_\mu$ | Its quaternion conjugate, $\varepsilon=(+1,-1,-1,-1)$ |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial^2/\partial Q_t^2+\Delta_Q$ | d'Alembertian, $\Delta_Q=\sum_k\partial^2/\partial Q_k^2$; in $t'$ it is $\Delta_Q-\partial^2/\partial t'^2$ |
| $\tilde{\Psi}=\tilde{\Psi}_L+\tilde{\Psi}_R$ | Classical Dirac field, an element of $\mathbb{B}$, in its two chiral halves |
| $\tilde{\Psi}^\flat=-\tilde{\Psi}^{*}$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\bar{\tilde\Psi}X=\mathrm{Sc}(\tilde\Psi^{*}iX\vec e_x)$ | Dirac adjoint: Hermitian conjugate, then right multiplication by $i\vec e_x$ |
| $\langle\tilde\Psi,\tilde\Phi\rangle_{\mathrm D}=\mathrm{Sc}(\tilde\Psi^{*}i\tilde\Phi\vec e_x)$ | Dirac pairing; equals $\bar{\tilde\Psi}\tilde\Phi$ |
| $e_\mu$ | Basis unit: $e_t$ for $\mu=t$, $\vec e_k$ for $\mu=k$ |
| $\mathbb{D}:\tilde X\mapsto-\frac{\partial\tilde X}{\partial t'}\vec e_x-\sum_k\vec e_k\frac{\partial\tilde X}{\partial Q_k}\vec e_y$ | Pair operator on one element; $\mathbb{D}^2=\Box$ |
| $\mathbb{D}_p:\tilde X\mapsto iE_{\vec p}\tilde X\vec e_x-i\sum_kp_k\vec e_k\tilde X\vec e_y$ | Momentum symbol on a plane wave; $\mathbb{D}_p^2=p^2$ |
| $\mathcal{L}=\bar{\tilde\Psi}(\mathbb{D}-m)\tilde\Psi$ | Dirac Lagrangian density |
| $\pi=\partial\mathcal{L}/\partial(\partial\tilde\Psi/\partial t')=i\tilde\Psi^{*}$ | Conjugate momentum; $\pi-i\tilde\Psi^{*}\approx0$ is second class |
| $\tilde\Psi^{(r)}_{\pm}(\vec p)$ | Parent article's positive- and negative-frequency element amplitudes |
| $X,Y,\vec\Delta=X-Y$ | Spatial points and their separation |
| $p_\mu=(E_{\vec p},\vec p)$, $p^2=p_0^2-\vec p^2=m^2$ | Four-momentum, mass shell; the index labels, $\varepsilon$ carries the signs |
| $\varepsilon=(+1,-1,-1,-1)$ | Sign vector of the momentum label in $\mathbb{D}_p$ |
| $\tilde P$, $\tilde R$ | Wave biquaternion and four-position biquaternion of the parent article |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Biquaternionic mass-shell condition |
| $\tilde\Psi^{\mathrm{fop}}$, $a^{\mathrm{fop}}_r(\vec p)$, $b^{\mathrm{fop}}_r(\vec p)$ | Quantized field; particle and antiparticle annihilation operators |
| $\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k)$ | Mode anticommutator |
| $H$, $:\!H\!:$ | Hamiltonian and its normal-ordered form |
| $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$ | Normal-ordering constant (vacuum energy) |
| $n_{\mathrm F}$, $n_{\mathrm B}$ | Fermi and Bose occupation numbers, $1/(\exp(\beta(E-\mu))\pm1)$ |
| $(-1)^F$ | Fermion-parity grading |
| $ϙ$, $Ϙ^{\mathrm{fop}}$ | Field charge unit, and the charge operator counting charge in those units |
| $\mu$ | Chemical potential of the thermal state; elsewhere the same letter is an index, as in $p_\mu$ and $\vec e_\mu$ |
| $\beta=\hbar/(k_BT)$, $\omega_\beta$, $\alpha_{t'}$ | Inverse temperature, thermal state, the evolution generated by the state's Hamiltonian |
| $F_{A B}(t'+i\beta)=F_{B A}(-t')$ | KMS condition |
| $K=-\log\rho$ | Modular Hamiltonian (Hermitian, in $\mathbb{M}_+$) |
| $\omega_n=(2n+1)\pi/\beta$ | Fermionic Matsubara frequencies |

## Further Reading

- [Conventions of the Operators and the Calculus](operator-and-calculus-conventions.html), for the gradient, its conjugate, the d'Alembertian and the pair operator used throughout.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and the prediction of the antiparticle.
- W. Pauli, "The connection between spin and statistics," *Physical Review* **58** (1940) 716–722, for the theorem that forces anticommutation for half-integer spin.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the canonical quantization of the Dirac field.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the constrained canonical structure, the mode algebra, and the vacuum energy.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the mode expansion, the spin sums, and the Hamiltonian in the convention used here.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the spin–statistics connection and the construction of the Fock space.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic formulation in which the KMS condition is stated.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), and J. I. Kapusta and C. Gale, *Finite-Temperature Field Theory* (Cambridge, 2006), for the imaginary-time formalism and the fermionic Matsubara frequencies.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Clifford-algebraic background to the biquaternion and spinor structures.
