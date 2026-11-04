# __Canonical Quantization of the Biquaternion Dirac Field__

## Introduction

The companion article *Quantum Physics in Biquaternionic Form* raises, as the second of its list of open questions, a precise one:

> "The formalism is first-quantized. To describe creation and annihilation of particles, one needs a Fock space and operator-valued fields. How does the biquaternion framework extend to this setting?"

The companion article *The Dirac Equation in Biquaternionic Form* supplies the field-side setting, and the article *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit* supplies the classical material a mode expansion needs: the positive- and negative-frequency plane-wave solutions, their covariant normalizations, and the spin sums. The article *The KMS Condition and the Biquaternion Framework* supplies the thermal motivation and identifies exactly what a fermionic extension must add: a $\mathbb{Z}/2$ grading under which fermionic operators anticommute, which the biquaternion algebra does not by itself provide.

This article is a first attempt at that extension. Its subject is the canonical quantization of the biquaternion Dirac field: the promotion of the classical field to an operator-valued field, the equal-time anticommutation relations, the expansion in the plane-wave solutions established by the parent article, the algebra of the mode operators, the Hamiltonian and its normal-ordering constant, the reason the modes anticommute rather than commute, and the relation of the resulting operator algebra to the thermal-state framework of the KMS article.

The article has to be read with a clear division in mind, and we state it at the outset because it governs everything that follows.

- **The standard part.** The biquaternion Dirac equation is the one-sided chiral pair, and on the spinor module it is transcribed as the single cell equation $(\mathbb{D}-m)\psi=0$, where $\mathbb{D}$ is the pair operator of *Conventions of the Operators and the Calculus* read on the module in the chiral basis. The two-sided equation of Kravchenko — the spatial gradient acting from the left and the mass from the right through $\vec e_z$ — is a different operator and is not quantized here. The canonical quantization of the one-sided equation — the Lagrangian, the conjugate momentum, the equal-time anticommutators, the mode expansion, the mode algebra, the Hamiltonian, and the normal-ordering constant — is textbook quantum field theory, transcribed into the notation of this series. None of it is new, and none of it depends on the biquaternion structure beyond the kinematical conventions already fixed by the companion articles.
- **The open part.** What is *not* standard, and what this article cannot settle, is the intrinsic formulation of the quantization in the algebra $\mathbb{B}$ itself: whether the operator-valued field should be taken to be $\mathbb{B}$-valued or valued in the spinor module on which $\mathbb{B}\cong M_2(\mathbb{C})$ acts; what the correct $\mathbb{B}$-intrinsic Lagrangian and conjugate momentum are; what the biquaternion Fock space is; and how the $\mathbb{Z}/2$ grading required by fermionic statistics is to be embedded in $\mathbb{B}$.

We therefore make no claim that the extension is canonical in the biquaternion framework. The claim is narrower: the extension can be carried out on the spinor module with the parent article's solutions, and it supplies exactly the operator structure — anticommuting modes and a fermion-parity grading — that the KMS article identifies as missing. Whether that structure lifts to a genuinely biquaternionic one is the open question this article is meant to expose.

The article is organized as follows. The next section fixes the classical field and its conjugate momentum, and identifies the constraint that forces the canonical structure to be imposed rather than assumed. The following section states the equal-time anticommutation relations and the reasons they, rather than commutators, are the consistent choice. The next section carries out the expansion in the parent article's plane-wave solutions. The section after that derives the anticommutators of the mode operators and builds the Fock space.

The next section gives the Hamiltonian, the normal-ordering constant, and the four-momentum and charge. A section on spin and statistics records why anticommutation is forced here, without developing the full spin–statistics theorem, which the companion article *The Spin–Statistics Theorem in Biquaternionic Form* treats on its own. A section relates the result to the KMS thermal-state framework. The article then gives an explicit accounting of what is standard and what is open, followed by a reference section, *The Legacy Pauli Gamma Formulation*, that records the gamma-matrix dictionary; the body itself is written in cells, and the gammas appear only there. It closes with the summary, the notation table, and further reading.

## The Classical Field and Its Conjugate Momentum

The biquaternion Dirac field of the companion article is the map $\tilde{\Psi}:\mathbb{R}^{1,3}\to\Delta$, with $\Delta=S\oplus S^{\mathrm{c}}$ the Dirac module of the two chiral halves, satisfying the linear, chirality-off-diagonal pair

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R,
$$

where $\tilde{\Psi}=\tilde{\Psi}_L+\tilde{\Psi}_R$ with $\tilde{\Psi}_L\in S$ and $\tilde{\Psi}_R\in S^{\mathrm{c}}$. At $m=0$ the pair decouples into

$$
\tilde{\nabla}\tilde{\Psi}_R=0,\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=0,
$$

one equation per chirality. The single equation $\tilde{\nabla}\tilde{\Psi}=0$ is the right-handed member, not the whole massless field.

Two formulations now carry the name *Dirac equation*, and they must not be read as one. The pair above is the corpus's **one-sided** equation: both gradients act from the left, and the mass is the off-diagonal pairing of the two chiral halves. Kravchenko's **two-sided** equation, for a biquaternion field $F$,

$$
\bigl(i\partial/\partial t'+D_3\bigr)F-m\,i\,\overline{F}\,\vec e_z=0,
\qquad
D_3=\sum_k\vec e_k\frac{\partial}{\partial Q_k},
$$

is a different operator: the spatial gradient acts from the left, the mass from the right through $\vec e_z$, and the mass term carries the algebra's complex conjugation $\overline{\cdot}$ — a bar over the field, the coefficient conjugation, and it is not the Dirac adjoint $\psi^\dagger C_0$ of the sections below. The two are related by the dictionary $A$ of the parent article's section *An Explicit Dictionary with Conjugation in the Mass Term*, but they are not the same equation, and their mass terms are of different kinds. This article quantizes the one-sided pair; the two-sided equation is recorded only to keep the two apart.

The companion solutions article works with the spinor-module representative of the pair, the four-component complex Dirac spinor $\psi\in\Delta\cong\mathbb{C}^4$. The frame cells act on that four-dimensional space; its two chiral halves are the two-component spinor modules $S$ and $S^{\mathrm{c}}$, and it is on those that the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ acts. There the pair is transcribed as the single cell equation

$$
\Big(\mathbb{D}-\frac{mc}{\hbar}\Big)\psi=0,
$$

whose solutions, normalizations, and spin sums are established in the parent article and are used below without rederivation. From this point the article sets $c=\hbar=1$, so $mc/\hbar$ is written $m$ and every $m$ below means that combination; a dimensionful constant returns only where a dimensional statement is at issue, in the inverse temperature $\beta=\hbar/(k_BT)$, in the plane-wave phase $\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar$, and in the mass-shell condition $\tilde P\tilde P^{\natural}=-m^2c^2$.

### The Frame Cells and the Pair Operator

The body is written in the **frame cells** of the reference frame. Write

$$
C_0:=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}},\qquad
C_k:=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
iC_\mu=-L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\kappa(\mu)}}^{\mathrm{axf}},
$$

where $L_a\psi=a\psi$ and $R_b\psi=\psi b$ are the left and right multiplications, $e_\mu$ runs over the four basis units $e_t,\vec e_x,\vec e_y,\vec e_z$ — the scalar unit for $\mu=t$ and $\vec e_k$ for $\mu=k$ — and $\kappa(t)=x$, $\kappa(k)=y$ name the spatial unit that each cell multiplies on the right. $I_4=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ is the identity on the module. The solutions article writes the same cells with a capital letter and an index; the letter changes, the operators do not. The cells satisfy

$$
C_\mu C_\nu+C_\nu C_\mu=2g_{\mu\nu}I_4,\qquad
\varepsilon=(1,-1,-1,-1),
$$

so $C_0^2=I_4$ and $C_k^2=-I_4$. A product of two cells carries a single minus sign and no leftover imaginary unit, because $i^2=-1$ is already in the cell:

$$
C_\mu C_\nu=i^2\,L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\kappa(\mu)}}^{\mathrm{axf}}\,L_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\kappa(\nu)}}^{\mathrm{axf}}
=-\,L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\kappa(\mu)}}^{\mathrm{axf}}\,L_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\kappa(\nu)}}^{\mathrm{axf}} .
$$

On the algebra the pair operator carries no matrix generator; on the module it is represented by the cell operator that the solutions article writes as the position-space Dirac operator:

$$
\mathbb{D}:=iC_0\frac{\partial}{\partial t'}+i\sum_k C_k\frac{\partial}{\partial Q_k}
=-L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\frac{\partial}{\partial t'}-\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\frac{\partial}{\partial Q_k},
$$

with $Q_k$ running over the three spatial coordinates. Its symbol on a plane wave is the momentum cell

$$
\mathbb{D}_p:=C_0E_{\vec p}-\sum_k C_k p_k=\sum_{\mu}\varepsilon_\mu C_\mu p_\mu,
\qquad \varepsilon=(+1,-1,-1,-1),
$$

with $p_0=E_{\vec p}$ and $p_k$ the physical momentum components, so that $p^2=p_0^2-\vec p^2=m^2$. The lower index of $p_\mu$ is a label and not a metric contraction: the signs are carried by $\varepsilon$. That sign vector is what the plane wave produces. On $e^{-ip\cdot x}$ the time derivative gives $-iE_{\vec p}$ and the spatial derivatives $+ip_k$, so the timelike term of $\mathbb{D}$ contributes $E_{\vec p}C_0$ and the spacelike terms $-p_kC_k$.

Each term of $\mathbb{D}$ carries the product $i\cdot i=-1$: the explicit $i$ of the operator and the $i$ of the cell cancel with a minus sign, so the cell form has no imaginary unit left. On the material sector both objects satisfy $\mathbb{D}^2=\Box$, where the corpus's d'Alembertian is $\Box=\partial^2/\partial Q_t^2+\Delta_Q$, with $\Delta_Q:=\sum_k\partial^2/\partial Q_k^2$ the spatial Laplacian, which in $t'$ is $\Delta_Q-\partial^2/\partial t'^2$ because $\partial/\partial Q_t=-i\partial/\partial t'$; and $\mathbb{D}_p^2=p^2$, equal to $m^2$ on the mass shell.

### The Lagrangian

The classical field theory is defined by the Lagrangian density

$$
\mathcal{L}=\psi^{\dagger}C_0\,(\mathbb{D}-m)\,\psi
=\psi^\dagger\Big(i\frac{\partial}{\partial t'}+i\sum_kC_0C_k\frac{\partial}{\partial Q_k}-mC_0\Big)\psi ,
$$

in which the three coefficient matrices are visible: the identity on the time derivative, the cell $C_0C_k$ on each spatial derivative, and $-mC_0$ on the field itself. Variation with respect to $\psi^{\dagger}C_0$ returns the Dirac equation $(\mathbb{D}-m)\psi=0$; variation with respect to $\psi$ returns the conjugate equation $\psi^{\dagger}C_0(\mathbb{D}-m)=0$, in which the operator acts on $\psi^{\dagger}C_0$ from the left; it is the Hermitian conjugate of the first.

The Lagrangian is **real up to a four-divergence**. The mass term is Hermitian outright, because $C_0$ is Hermitian and $m$ real. Each derivative term carries an explicit $i$ and a Hermitian coefficient matrix, so each differs from its conjugate by a divergence, and

$$
\mathcal{L}-\mathcal{L}^\dagger
=\frac{\partial}{\partial t'}\big(i\psi^\dagger\psi\big)
+\sum_k\frac{\partial}{\partial Q_k}\big(i\psi^\dagger C_0C_k\psi\big).
$$

The Hermiticity of the coefficient matrices is the one identity

$$
C_\mu^\dagger=C_0C_\mu C_0,\qquad\text{equivalently}\qquad(C_0C_\mu)^\dagger=C_0C_\mu ,
$$

which says that the cell is self-adjoint for the $C_0$-twisted pairing and not for the ordinary one: $C_0C_\mu$ is Hermitian for every $\mu$, while $C_0$ is already Hermitian and the spatial cells $C_k$ are anti-Hermitian. Multiplying by $C_0$ therefore turns the anti-Hermitian cells into Hermitian ones, so $C_0\mathbb{D}_p$ is Hermitian while $\mathbb{D}_p$ is not. The Dirac adjoint is

$$
\psi^\dagger C_0,\qquad
C_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}},
$$

the Hermitian conjugate followed by the timelike frame cell. This is the Lagrangian of a free Dirac field, with the pair operator in place of the matrix contraction.

### The Conjugate Momentum and Its Constraint

The canonical momentum conjugate to $\psi$ is

$$
\pi=\frac{\partial\mathcal{L}}{\partial(\partial\psi/\partial t')}=i\,\psi^\dagger .
$$

The step is worth displaying, because it is the origin of the entire fermionic structure. The only term of $\mathcal{L}$ that carries a time derivative is the one with $\partial/\partial t'$. In the cells it is

$$
\psi^{\dagger}C_0\,iC_0\frac{\partial}{\partial t'}\psi
=\psi^\dagger C_0\,iC_0\frac{\partial}{\partial t'}\psi
=i\,\psi^\dagger\frac{\partial}{\partial t'}\psi,
$$

where $C_0^2=I_4$. Differentiating with respect to $\partial\psi_a/\partial t'$ therefore returns $i\psi^\dagger_a$, so $\pi=i\psi^\dagger$.

The momentum is not the time derivative of the field. The Dirac equation is first order in time, so the momentum is algebraically tied to the field by the primary constraint

$$
\pi-i\psi^\dagger\approx 0 .
$$

The constraint is **second class**: the Legendre transform is singular, and the field and its momentum are not independent canonical variables, so the naive Poisson bracket has to be replaced by the Dirac bracket. The standard route computes that bracket and then quantizes it; for the free field the outcome is the equal-time anticommutation relations. This article takes the route as read: it imposes the relations directly and verifies, in the section on the mode operators, that they reproduce the boxed equal-time relation. Nothing below depends on the Dirac-bracket computation itself.

The constraint is also why the ordinary rule $[\phi,\pi]=i\delta^{(3)}$ cannot be applied to a Dirac field: there is no independent pair for it to relate. It does not, by itself, say whether the bracket that replaces it is a commutator or an anticommutator; that question is settled by the positivity of the energy rather than by the constraint, and it is the subject of the next section.

### The Biquaternion Interpretation and the Open Point

Written on the spinor module, the Lagrangian and the canonical momentum are the standard ones. Written in the algebra, they are not yet fixed. The parent article's mass term is the linear, chirality-off-diagonal coupling, whose spinor-module representative is the ordinary mass term $m\psi$; the anti-Hermitian conjugation $\flat=-{}^{*}$ is the algebra's real structure, not the mass. The $\mathbb{B}$-intrinsic Lagrangian — the real scalar built from $\tilde{\nabla}\tilde{\Psi}$, $\tilde{\Psi}$, their conjugates, and the trace or norm pairing of the algebra — is not determined by the algebra alone, and neither is the intrinsic conjugate momentum.

Two inequivalent transcriptions are available: one may treat the operator field as $\mathbb{B}$-valued and pair it with the real part of the trace, or one may treat it as valued in the spinor module and quantize there. We adopt the second, which is the parent article's working setting, and we return to the first in the closing section on what is open. The reader should keep in mind that the mode structure below is the standard one; what is being tested here is whether the biquaternion framework naturally reproduces it.

## Equal-Time Anticommutation Relations

Quantization promotes the classical field and its momentum to operators $\psi^{\mathrm{fop}}$, $\pi^{\mathrm{fop}}$ and imposes equal-time brackets. Write

$$
X:=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,\qquad
Y:=x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z,
$$

for the two spatial points. For the Dirac field the brackets are **anticommutators**:

$$
\boxed{\;\{\psi^{\mathrm{fop}}_a(X,t'),\psi^{\mathrm{fop}\dagger}_b(Y,t')\}=\delta_{ab}\,\delta^{(3)}(X-Y)\;}
$$

together with

$$
\{\psi^{\mathrm{fop}}_a(X,t'),\psi^{\mathrm{fop}}_b(Y,t')\}=0,\qquad
\{\psi^{\mathrm{fop}\dagger}_a(X,t'),\psi^{\mathrm{fop}\dagger}_b(Y,t')\}=0,
$$

where $a,b$ are spinor indices. In terms of the conjugate momentum $\pi^{\mathrm{fop}}=i\psi^{\mathrm{fop}\dagger}$, the first relation reads

$$
\{\psi^{\mathrm{fop}}_a(X,t'),\pi^{\mathrm{fop}}_b(Y,t')\}=i\,\delta_{ab}\,\delta^{(3)}(X-Y),
$$

which is the fermionic analogue of the canonical relation $[\phi^{\mathrm{fop}},\pi^{\mathrm{fop}}]=i\delta^{(3)}$ of a scalar field. These are the standard canonical relations, and they are imposed rather than derived.

The choice of anticommutator over commutator is forced, and three reasons can be given at the level of this article. They are stated here because they are operative in the construction; the full spin–statistics theorem belongs to the companion article *The Spin–Statistics Theorem in Biquaternionic Form* and is not developed here.

**1. Boundedness of the energy.** As shown in the section on the Hamiltonian, the mode expansion of the energy contains a negative-frequency contribution proportional to $b^{\mathrm{fop}}_r(\vec p)b^{\mathrm{fop}\dagger}_r(\vec p)$. If the modes commuted, this product would be $b^{\mathrm{fop}\dagger}_r(\vec p)b^{\mathrm{fop}}_r(\vec p)+1$, and the energy would be

$$
H=\sum_r\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}
\Big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r-b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r\Big)+\text{constant},
$$

unbounded below: adding antiparticles would lower the energy without limit, and no stable vacuum would exist. If the modes anticommute, the same product is $1-b^{\mathrm{fop}\dagger}_r(\vec p)b^{\mathrm{fop}}_r(\vec p)$, and the same expression becomes a positive sum plus a constant. The anticommutator is what makes the negative-frequency modes into positive-energy antiparticles. This is the operator content of the Dirac sea.

**2. Microcausality.** For a field of spin $\tfrac12$, the commutator $[\psi^{\mathrm{fop}}(x),\psi^{\mathrm{fop}\dagger}(y)C_0]$ does **not** vanish for spacelike separated $x,y$, so quantizing with commutators would correlate measurements in causally disconnected regions. The anticommutator $\{\psi^{\mathrm{fop}}(x),\psi^{\mathrm{fop}\dagger}(y)C_0\}$ does vanish there, and it is the quantity that must be local for a fermion field. This is the content of Pauli's 1940 argument: the requirement that the fields commute or anticommute outside the light cone, together with the transformation properties of the spinor representation, selects anticommutation for half-integer spin.

**3. Positivity of the inner product.** Quantizing a half-integer-spin field with commutators produces states of negative norm; the anticommutator is what makes the Fock inner product positive-definite. This is the Hilbert-space form of the same obstruction.

The three reasons are aspects of one theorem. We note only that they all point the same way for a field whose one-particle states transform in the spinor representation — which is the case here, since the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ acts on a two-dimensional complex spinor module, of which the Dirac module holds two copies, one per chirality.

## Field Expansion in the Plane-Wave Solutions

The classical equation is linear, so its general solution is a superposition of the plane waves constructed in the parent article. Those solutions come in two branches: the positive-frequency branch spanned by the spinors $w^{(r)}(\vec p)\exp(-ip\cdot x)$ and the negative-frequency branch spanned by $v^{(r)}(\vec p)\exp(+ip\cdot x)$, with $r=1,2$ and

$$
E_{\vec p}=+\sqrt{\vec p^2+m^2},\qquad p\cdot x:=E_{\vec p}t'-\vec p\cdot X,
$$

for the point $x=(X,t')$. The covariant normalizations, orthogonality, and spin sums established there are

$$
\bar w^{(r)}w^{(s)}=2m\,\delta_{rs},\qquad
\bar v^{(r)}v^{(s)}=-2m\,\delta_{rs},\qquad
\bar w^{(r)}v^{(s)}=\bar v^{(r)}w^{(s)}=0,
$$

$$
w^{(r)\dagger}w^{(s)}=v^{(r)\dagger}v^{(s)}=2E_{\vec p}\,\delta_{rs},
$$

$$
\sum_{r=1}^{2}w^{(r)}(\vec p)\bar w^{(r)}(\vec p)=\mathbb{D}_p+m,\qquad
\sum_{r=1}^{2}v^{(r)}(\vec p)\bar v^{(r)}(\vec p)=\mathbb{D}_p-m .
$$

Quantization consists in replacing the constant coefficients of the classical expansion by operators:

$$
\boxed{\;\psi^{\mathrm{fop}}(X,t')=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec p}}}
\sum_{r=1}^{2}\Big[a^{\mathrm{fop}}_r(\vec p)\,w^{(r)}(\vec p)\,\exp(-ip\cdot x)
+b^{\mathrm{fop}\dagger}_r(\vec p)\,v^{(r)}(\vec p)\,\exp(+ip\cdot x)\Big]\;}.
$$

The field and its adjoint,

$$
\psi^{\mathrm{fop}\dagger}(Y,t')=\int\!\frac{d^3k}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec k}}}
\sum_{s=1}^{2}\Big[a^{\mathrm{fop}\dagger}_s(\vec k)\,w^{(s)\dagger}(\vec k)\,\exp(+ik\cdot y)
+b^{\mathrm{fop}}_s(\vec k)\,v^{(s)\dagger}(\vec k)\,\exp(-ik\cdot y)\Big],
$$

with $k\cdot y:=E_{\vec k}t'-\vec k\cdot Y$, together define the operator-valued field. The **annihilation** operators $a^{\mathrm{fop}}_r(\vec p)$ multiply the positive-frequency solutions, and the **creation** operators $b^{\mathrm{fop}\dagger}_r(\vec p)$ multiply the negative-frequency solutions. The attribution of a creation operator to the negative-frequency branch is the operator form of the reinterpretation of the Dirac sea: the modes of "negative frequency" are the antiparticles of positive energy.

Two structural remarks belong here. First, $\psi^{\mathrm{fop}}$ is **not Hermitian**, and it should not be: a complex Dirac field carries a conserved charge, and particle and antiparticle are distinct. Second, the expansion is written on the spinor module, following the parent article. In the algebra, each mode function is the module representative of a biquaternion plane wave $\tilde{\Psi}_0\exp\!\left(i\,\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar\right)$, with $\tilde P$ the wave biquaternion and $\tilde R$ the four-position biquaternion of the parent article — a tilde on $R$, to be read apart from the right multiplication $R_b$. The two branches are the two signs of the energy root of the single biquaternion mass-shell condition

$$
\tilde P\tilde P^{\natural}=-m^2c^2 ,
$$

and the polarization equation is the algebraic form of the momentum-space equation. Promoting the coefficients to operators is thus a transcription of the standard mode expansion onto the parent article's biquaternion plane waves; it is not, by itself, a derivation of the expansion from the algebra.

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

These are the standard anticommutation relations of the free Dirac field, in the continuum normalization inherited from the parent article's covariant spinors.

### Consistency with the Equal-Time Relations

It is worth verifying that these relations reproduce the boxed equal-time relation, because the verification exposes a point of care about the relative phases of the two branches. Write $\vec\Delta:=X-Y$ for the separation of the two points. Inserting the expansions and using the mode algebra gives, at equal times,

$$
\{\psi^{\mathrm{fop}}_a(X,t'),\psi^{\mathrm{fop}\dagger}_b(Y,t')\}
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\vec p}}
\Big[\sum_r w^{(r)}_a w^{(r)\dagger}_b\,e^{+i\vec p\cdot\vec\Delta}
+\sum_r v^{(r)}_a v^{(r)\dagger}_b\,e^{-i\vec p\cdot\vec\Delta}\Big].
$$

The two phases are **opposite**: the positive-frequency term carries $e^{+i\vec p\cdot\vec\Delta}$ and the negative-frequency term $e^{-i\vec p\cdot\vec\Delta}$. Multiplying the spin sums by $C_0$ on the right and using $\bar w=w^\dagger C_0$, $C_0^2=I_4$ and $C_kC_0=-C_0C_k$, one obtains

$$
\sum_r w^{(r)}w^{(r)\dagger}=E_{\vec p}I_4+mC_0+C_0\sum_k C_k p_k,
$$

$$
\sum_r v^{(r)}v^{(r)\dagger}=E_{\vec p}I_4-mC_0+C_0\sum_k C_k p_k,
$$

so that, with $\theta=\vec p\cdot\vec\Delta$,

$$
\sum_r\Big[w^{(r)}w^{(r)\dagger}e^{+i\theta}+v^{(r)}v^{(r)\dagger}e^{-i\theta}\Big]
=2E_{\vec p}\cos\theta\,I_4
+2\cos\theta\,C_0\sum_k C_k p_k
+2im\sin\theta\,C_0 .
$$

The first term is even in $\vec p$ and, after division by $2E_{\vec p}$, integrates to $\delta^{(3)}(\vec\Delta)\,I_4$; the second and third terms are odd in $\vec p$ and vanish under symmetric integration. Hence the equal-time relation holds. The cancellation of the odd terms is exactly what the opposite phases of the two branches accomplish; had both phases been equal, the cross terms would have survived and the canonical relation would have failed.

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

which is the Pauli exclusion principle as an algebraic identity: the square of a creation operator vanishes because $\{a^{\mathrm{fop}\dagger}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=0$. This is the sharpest sense in which the statistics is carried by the mode algebra. The construction of the biquaternion Fock space as an object in its own right — rather than as the exterior algebra of the spinor-module solution space — is the subject of the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; here we need only the mode algebra.

## The Hamiltonian and the Normal-Ordering Constant

The conserved energy of the free Dirac field is

$$
H=\int d^3X\;\psi^{\mathrm{fop}\dagger}\Big(-i\sum_k C_0C_k\frac{\partial}{\partial Q_k}+mC_0\Big)\psi^{\mathrm{fop}}
=\int d^3X\;\psi^{\mathrm{fop}\dagger}C_0\Big(-i\sum_k C_k\frac{\partial}{\partial Q_k}+m\Big)\psi^{\mathrm{fop}} .
$$

The integrand is the $00$ component of the canonical energy–momentum tensor, equivalently the Legendre transform $\pi\,\partial \psi/\partial t'-\mathcal{L}$ of the Lagrangian fixed in the section *The Lagrangian*: the two time-derivative terms cancel, and what is left is the expression above.

The two forms are the same operator. In the first the spatial derivative is multiplied by $C_0C_k$; in the second the $C_0$ has been absorbed into $\psi^{\dagger}C_0$, and since $C_0^2=I_4$ the operator standing between $\psi^\dagger$ and $\psi$ is again $C_0C_k$. That matrix is Hermitian,

$$
(C_0C_k)^\dagger=C_k^\dagger C_0^\dagger=(-C_k)C_0=C_0C_k ,
$$

because $C_0$ is Hermitian, $C_k$ is anti-Hermitian, and the two anticommute. It is the identity $C_\mu^\dagger=C_0C_\mu C_0$ of the Lagrangian section, read on the pair. Substituting the mode expansion and using the parent article's normalizations and orthogonality gives the standard result

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

and the normal-ordered electric charge, from $j_\mu=\psi^{\dagger}C_0C_\mu\psi$ with $j_0=\psi^\dagger C_0C_0\psi=\psi^\dagger\psi$, is

$$
:\!Ϙ^{\mathrm{fop}}\!:\;=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}
\Big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r-b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r\Big),
$$

so that particles and antiparticles carry opposite charge, as they must; the operator counts charge in units of the field charge $ϙ$, so the physical charge is $ϙ\,Ϙ^{\mathrm{fop}}$. The field operator is charged accordingly,

$$
[Ϙ^{\mathrm{fop}},\psi^{\mathrm{fop}}]=-\psi^{\mathrm{fop}},\qquad
[Ϙ^{\mathrm{fop}},\psi^{\mathrm{fop}\dagger}]=+\psi^{\mathrm{fop}\dagger},
$$

which is the Dirac-field form of the relation $[Ϙ^{\mathrm{fop}},\phi^{\mathrm{fop}}]=-\phi^{\mathrm{fop}}$ of *The Quantized Scalar Field in Biquaternionic Form*: the field lowers the charge by one unit and its conjugate raises it. All three expressions are the standard ones; their derivation uses only the parent article's spinor relations.

The status of $E_0$ deserves one cautionary sentence. Its divergence is an ultraviolet feature of the free field, removed by the conventional normal-ordering prescription, and nothing in the biquaternion structure as used here changes that. Whether the biquaternion framework offers a distinguished or geometrically meaningful regularization of the vacuum energy is an open question, and we do not claim one.

## Spin and Statistics

The anticommutation relations are not a convention; they are selected. The three reasons given above — boundedness of the energy, microcausality, and positivity of the norm — are all consequences of one structural fact: the one-particle states of the field transform in the **spinor representation** of the Lorentz group, and the biquaternion algebra realizes that representation on its module. For a field of half-integer spin the representation is double-valued: a rotation by $2\pi$ is the identity in the vector representation but minus the identity in the spinor representation, and only a rotation by $4\pi$ returns the spinor to itself. It is this two-valuedness, together with the requirement that the local observables be built from bilinears, that forces the anticommutator: the commutator of two spinor fields fails to vanish at spacelike separation, while the anticommutator does.

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
\omega_\beta(\,\cdot\,)=\frac{1}{Z}\,\mathrm{Tr}\big(\exp(-\beta(H-\mu Ϙ^{\mathrm{fop}}))\,\cdot\,\big)
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

The structural facts the KMS article records remain intact. The imaginary time direction is intrinsic to the material sector $\mathbb{M}_-$; the complexified time direction in which the KMS continuation takes place is the sum of the imaginary time direction of $\mathbb{M}_-$ and the real time direction of $\mathbb{M}_+$; and the modular Hamiltonian $K=-\log\rho$ is a Hermitian element of the algebra, hence lies in the informational sector $\mathbb{M}_+$. What the present article adds is the operator algebra on which the thermal state is defined, together with the grading the KMS article flagged as absent. What it does **not** add is a genuinely biquaternionic construction of the thermal state: the state $\omega_\beta$ above is a complex-valued functional on the Fock space built from the spinor-module field, and whether it extends to a functional intrinsically defined on $\mathbb{B}$ — with the grading embedded in $\mathbb{B}$ rather than in the mode algebra, and with a spinor-module form of the fermionic twist — remains open.

The relation established here is a consistency of structures, not a derivation of the fermionic KMS condition from the biquaternion algebra.

## What Is Standard and What Is Open

Because the question addressed here is itself an open question of the framework, we separate the two kinds of statement explicitly.

**Standard quantum field theory, transcribed.**

- The Lagrangian $\mathcal{L}=\psi^{\dagger}C_0(\mathbb{D}-m)\psi$ and the conjugate momentum $\pi=i\psi^\dagger$, together with the second-class constraint $\pi-i\psi^\dagger\approx0$.
- The equal-time anticommutation relations, imposed and verified, and the three reasons anticommutation rather than commutation is forced.
- The mode expansion in the parent article's plane-wave solutions, with the covariant normalization $\bar w w=2m$, $w^\dagger w=2E$, and the parent's spin sums.
- The mode-operator anticommutators, the Fock space, and Pauli exclusion as the algebraic identity $(a^{\mathrm{fop}\dagger})^2=0$.
- The Hamiltonian $:\!H\!:=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}+b^{\mathrm{fop}\dagger}b^{\mathrm{fop}})$ after normal ordering, the normal-ordering constant $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$, and the four-momentum and charge.
- The Fermi–Dirac distribution as the consequence of the KMS condition together with the anticommutator, and the fermionic Matsubara frequencies.

**Open in the biquaternion framework.**

- **The intrinsic operator field.** Whether the quantized field should be $\mathbb{B}$-valued, $M_2(\mathbb{C})$-valued, or spinor-module-valued, and to what extent these give inequivalent quantizations; *The Quantized Dirac Field in Biquaternionic Form* takes the construction up from this article's spinor-module transcription.
- **The intrinsic Lagrangian and momentum.** The $\mathbb{B}$-intrinsic Lagrangian, its real-scalar pairing, and the conjugate momentum are not fixed by the algebra alone; the spinor-module transcription is the one adopted above.
- **The biquaternion Fock space.** Whether it is the exterior algebra of the spinor-module solution space, or a construction native to $\mathbb{B}$; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* takes up the question in its own terms.
- **The grading.** The $\mathbb{Z}/2$ grading is supplied here on the mode algebra; embedding it in $\mathbb{B}$ itself, as the KMS article requires, is not done.
- **The spin–statistics theorem.** Whether the framework derives spin–statistics or only transcribes it is left to *The Spin–Statistics Theorem in Biquaternionic Form*.
- **The vacuum energy.** Whether the biquaternion structure singles out a regularization of $E_0$, or assigns it a geometric meaning, is open.
- **Empirical content.** As with the rest of the framework, whether any of this yields a prediction distinguishing it from standard quantum field theory is the unanswered question.

The extension attempted here is therefore **not canonical** in the framework: the part that works is the standard canonical quantization of the Dirac field, expressed in the parent article's plane-wave solutions and the material- and informational-sector notation; the part that is genuinely biquaternionic is not yet fixed. This article is the first attempt at the companion article's second-quantization question, and it should be read as delimiting the problem rather than closing it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are the frame cells of the body:

$$
\gamma_0[\mathbb{M}_-]=C_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1[\mathbb{M}_-]=C_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2[\mathbb{M}_-]=C_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3[\mathbb{M}_-]=C_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}.
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=C_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1[\mathbb{M}_-]=C_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2[\mathbb{M}_-]=C_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3[\mathbb{M}_-]=C_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}.
$$

The fifth gamma is not a fifth frame vector but their product, and $i^2=-1$ fixes its sign and its cell:

$$
\gamma_5[\mathbb{M}_-]:=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=iC_0C_1C_2C_3=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=-iR_{\vec e_z}^{\mathrm{pau}}.
$$

In the axis-free display:

$$
\gamma_5[\mathbb{M}_-]:=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=iC_0C_1C_2C_3=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}}.
$$

The four cells in the product carry $i^4=1$, so the single $i$ of the definition survives; the cell that results is $-iR_{\vec e_z}^{\mathrm{pau}}$, the chirality cell of the solutions article.

The pair operator of the body is the same cell operator, written in gammas:

$$
\mathbb{D}=i\gamma_0[\mathbb{M}_-]\frac{\partial}{\partial t'}+i\sum_k\gamma_k[\mathbb{M}_-]\frac{\partial}{\partial Q_k},
\qquad
\mathbb{D}_p=\gamma_0[\mathbb{M}_-]E_{\vec p}-\sum_k\gamma_k[\mathbb{M}_-]p_k,
$$

with $p_0=E_{\vec p}$ and $p_k$ the physical momentum components. Written in cells, each term $i\gamma_\mu[\mathbb{M}_-]=iC_\mu=-L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\kappa(\mu)}}^{\mathrm{pau}}$ has already spent the product $i\cdot i=-1$, so the operator is

$$
\mathbb{D}=-L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}\frac{\partial}{\partial t'}-\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\frac{\partial}{\partial Q_k},
$$

The same identities in the axis-free display:

$$
\mathbb{D}=-L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\frac{\partial}{\partial t'}-\sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\frac{\partial}{\partial Q_k},
$$

with no imaginary unit left in any term. The collapse removes the $i$, not the cell: $i\gamma_0[\mathbb{M}_-]=-R_{\vec e_x}^{\mathrm{pau}}\ne-I_4$, so the time derivative is multiplied by the right multiplication by $\vec e_x$, not by a number.

In the matrix representation of the frame, a single product of basis units is a pure tensor. Writing $c(M)$ for the coefficient matrix of $M$ in the basis of the sixteen products, the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$; a general element is a sum of at most four of them, and $\ell(M)=\operatorname{rank}c(M)$.

The cell $\gamma_5[\mathbb{M}_-]=-iR_{\vec e_z}^{\mathrm{pau}}$ is also the module representative of the central chirality sign $\chi=i\tilde\Xi_{\mathrm{ad}}$, with $\tilde\Xi_{\mathrm{ad}}$ the central root of $-e_t$: $\chi$ is the difference of the two central idempotents of the complexified algebra, so $\chi^2=i^2\tilde\Xi_{\mathrm{ad}}^2=(-1)(-e_t)=e_t$. The sign $\chi$ is central and lies outside $\mathbb{B}_{\mathbb{R}}$; the cell is its representative on the Dirac module, not its definition.

The map from the sixteen products of the biquaternion basis to the gamma frame is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, and the real left–right products $L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\kappa(\mu)}}^{\mathrm{pau}}$, without the central $i$, span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5[\mathbb{M}_-]^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.
## Summary

The biquaternion Dirac field is quantized by promoting its spinor-module representative to an operator-valued field. The equation quantized is the one-sided chiral pair, written on the module as $(\mathbb{D}-m)\psi=0$; Kravchenko's two-sided equation is a different operator and is not quantized here. The classical theory has Lagrangian $\mathcal{L}=\psi^{\dagger}C_0(\mathbb{D}-m)\psi$ and conjugate momentum $\pi=i\psi^\dagger$; the momentum is algebraically tied to the field by a second-class constraint, so the canonical structure is imposed rather than assumed. The equal-time relations are anticommutators,

$$
\{\psi^{\mathrm{fop}}_a(X,t'),\psi^{\mathrm{fop}\dagger}_b(Y,t')\}=\delta_{ab}\delta^{(3)}(X-Y)
$$

with all other equal-time anticommutators vanishing; anticommutation rather than commutation is forced by the boundedness of the energy, by microcausality, and by positivity of the norm, all three being consequences of the spinor character of the field.

The field expands in the plane-wave solutions established by the parent article,

$$
\psi^{\mathrm{fop}}(X,t')=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\vec p}}}\sum_r
\Big[a^{\mathrm{fop}}_r(\vec p)w^{(r)}(\vec p)\exp(-ip\cdot x)+b^{\mathrm{fop}\dagger}_r(\vec p)v^{(r)}(\vec p)\exp(+ip\cdot x)\Big],
$$

with the mode anticommutators $\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=\{b^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k)$ and all others zero. These reproduce the equal-time relation: the positive- and negative-frequency branches enter with opposite phases, the even part of the spin sums integrates to the delta function, and the odd parts cancel. The resulting Fock space carries Pauli exclusion as the algebraic identity $(a^{\mathrm{fop}\dagger}_r)^2=0$.

The Hamiltonian is $:\!H\!:=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r+b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r)$ after normal ordering, with the negative, quartically divergent normal-ordering constant $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$ removed. The normal-ordered charge has particles and antiparticles of opposite sign. The mode algebra is $\mathbb{Z}/2$-graded by fermion parity, which is the structure the KMS article identifies as missing; with it, the KMS condition plus the anticommutator yields the Fermi–Dirac distribution and the antiperiodic imaginary-time correlators whose Matsubara frequencies are $(2n+1)\pi/\beta$.

The extension is a transcription of standard canonical quantization onto the parent article's biquaternion plane waves, not a derivation of the quantized structure from the algebra $\mathbb{B}$. The intrinsic $\mathbb{B}$-valued Lagrangian and momentum, the biquaternion Fock space, and the embedding of the grading in $\mathbb{B}$ remain open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_k\vec e_k\,\partial/\partial Q_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial^2/\partial Q_t^2+\Delta_Q$ | d'Alembertian, $\Delta_Q=\sum_k\partial^2/\partial Q_k^2$; in $t'$ it is $\Delta_Q-\partial^2/\partial t'^2$ |
| $\tilde{\Psi}$ | Classical Dirac field, valued in $\Delta=S\oplus S^{\mathrm{c}}$ |
| $\tilde{\Psi}^\flat=-\tilde{\Psi}^{*}$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\psi=(\psi_L,\psi_R)$, $\psi^\dagger C_0$ | Dirac spinor (spinor module) and its adjoint |
| $e_\mu$ | Basis unit: $e_t$ for $\mu=t$, $\vec e_k$ for $\mu=k$ |
| $\kappa(\mu)$ | Right multiplier of the cell: $\kappa(t)=x$, $\kappa(k)=y$ |
| $C_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}$, $C_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Frame cells, acting on the spinor module |
| $C_\mu C_\nu+C_\nu C_\mu=2g_{\mu\nu}I_4$ | Cell Clifford algebra, $I_4=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $g_{\mu\nu}[\mathbb{M}_-]=\mathrm{diag}(-1,+1,+1,+1)$ | sign vector of the cells |
| $g_{\mu\nu}[\mathbb{M}_-]$ | Spacetime metric of the $ict'$ gradient |
| $\mathbb{D}=iC_0\partial/\partial t'+i\sum_kC_k\partial/\partial Q_k=-R_{\vec e_x}^{\mathrm{axf}}\partial/\partial t'-\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial/\partial Q_k$ | Pair operator on the module; $\mathbb{D}^2=\Box$ |
| $\mathbb{D}_p=C_0E_{\vec p}-\sum_kC_kp_k$ | Momentum symbol of $\mathbb{D}$ on a plane wave; $\mathbb{D}_p^2=p^2$ |
| $\mathcal{L}=\psi^{\dagger}C_0(\mathbb{D}-m)\psi$ | Dirac Lagrangian density |
| $\pi=\partial\mathcal{L}/\partial(\partial\psi/\partial t')=i\psi^\dagger$ | Conjugate momentum; $\pi-i\psi^\dagger\approx0$ is second class |
| $w^{(r)}(\vec p),v^{(r)}(\vec p)$ | Parent article's positive- and negative-frequency spinors |
| $\bar w w=2m$, $w^\dagger w=2E_{\vec p}$ | Covariant and Hermitian normalizations |
| $X,Y,\vec\Delta=X-Y$ | Spatial points and their separation |
| $p_\mu=(E_{\vec p},\vec p)$, $p^2=p_0^2-\vec p^2=m^2$ | Four-momentum, mass shell; the index labels, $\varepsilon$ carries the signs |
| $\varepsilon=(+1,-1,-1,-1)$ | Sign vector of the momentum label in $\mathbb{D}_p$ |
| $\tilde P$, $\tilde R$ | Wave biquaternion and four-position biquaternion of the parent article |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Biquaternionic mass-shell condition |
| $\psi^{\mathrm{fop}}$, $a^{\mathrm{fop}}_r(\vec p)$, $b^{\mathrm{fop}}_r(\vec p)$ | Quantized field; particle and antiparticle annihilation operators |
| $\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k)$ | Mode anticommutator |
| $H$, $:\!H\!:$ | Hamiltonian and its normal-ordered form |
| $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$ | Normal-ordering constant (vacuum energy) |
| $n_{\mathrm F}$, $n_{\mathrm B}$ | Fermi and Bose occupation numbers, $1/(\exp(\beta(E-\mu))\pm1)$ |
| $(-1)^F$ | Fermion-parity grading |
| $ϙ$, $Ϙ^{\mathrm{fop}}$ | Field charge unit, and the charge operator counting charge in those units |
| $\mu$ | Chemical potential of the thermal state; elsewhere the same letter is a Lorentz index, as in $C_\mu$ |
| $\beta=\hbar/(k_BT)$, $\omega_\beta$, $\alpha_{t'}$ | Inverse temperature, thermal state, the evolution generated by the state's Hamiltonian |
| $F_{A B}(t'+i\beta)=F_{B A}(-t')$ | KMS condition |
| $K=-\log\rho$ | Modular Hamiltonian (Hermitian, in $\mathbb{M}_+$) |
| $\omega_n=(2n+1)\pi/\beta$ | Fermionic Matsubara frequencies |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and the prediction of the antiparticle.
- W. Pauli, "The connection between spin and statistics," *Physical Review* **58** (1940) 716–722, for the theorem that forces anticommutation for half-integer spin.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the canonical quantization of the Dirac field.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the constrained canonical structure, the mode algebra, and the vacuum energy.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the mode expansion, the spin sums, and the Hamiltonian in the convention used here.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the spin–statistics connection and the construction of the Fock space.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic formulation in which the KMS condition is stated.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), and J. I. Kapusta and C. Gale, *Finite-Temperature Field Theory* (Cambridge, 2006), for the imaginary-time formalism and the fermionic Matsubara frequencies.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Clifford-algebraic background to the biquaternion and spinor structures.
