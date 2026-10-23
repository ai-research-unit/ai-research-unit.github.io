# __Canonical Quantization of the Biquaternion Dirac Field__

## Introduction

The companion article *Quantum Physics in Biquaternionic Form* raises, as the second of its list of open questions, a precise one:

> "The formalism is first-quantized. To describe creation and annihilation of particles, one needs a Fock space and operator-valued fields. How does the biquaternion framework extend to this setting?"

The companion article *The Dirac Equation in Biquaternionic Form* asks the same question from the field side, and the article *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit* supplies the classical material a mode expansion needs: the positive- and negative-frequency plane-wave solutions, their covariant normalizations, and the spin sums. The article *The KMS Condition and the Biquaternion Framework* supplies the thermal motivation and identifies exactly what a fermionic extension must add: a $\mathbb{Z}/2$ grading under which fermionic operators anticommute, which the biquaternion algebra does not by itself provide.

This article is a first attempt at that extension. Its subject is the canonical quantization of the biquaternion Dirac field: the promotion of the classical field to an operator-valued field, the equal-time anticommutation relations, the expansion in the plane-wave solutions established by the parent article, the algebra of the mode operators, the Hamiltonian and its normal-ordering constant, the reason the modes anticommute rather than commute, and the relation of the resulting operator algebra to the thermal-state framework of the KMS article.

The article has to be read with a clear division in mind, and we state it at the outset because it governs everything that follows.

- **The standard part.** The spinor-module form of the biquaternion Dirac equation is the ordinary Dirac equation, $(i\gamma^\mu\partial/\partial Q_\mu-m)\psi=0$ in the notation of the companion articles. Its canonical quantization — the Lagrangian, the conjugate momentum, the equal-time anticommutators, the mode expansion, the mode algebra, the Hamiltonian, and the normal-ordering constant — is textbook quantum field theory, transcribed into the notation of this series. None of it is new, and none of it depends on the biquaternion structure beyond the kinematical conventions already fixed by the companion articles.
- **The open part.** What is *not* standard, and what this article cannot settle, is the intrinsic formulation of the quantization in the algebra $\mathbb{B}$ itself: whether the operator-valued field should be taken to be $\mathbb{B}$-valued or valued in the spinor module on which $\mathbb{B}\cong M_2(\mathbb{C})$ acts; what the correct $\mathbb{B}$-intrinsic Lagrangian and conjugate momentum are; what the biquaternion Fock space is; and how the $\mathbb{Z}/2$ grading required by fermionic statistics is to be embedded in $\mathbb{B}$.

We therefore make no claim that the extension is canonical in the biquaternion framework. The claim is narrower: the extension can be carried out on the spinor module with the parent article's solutions, and it supplies exactly the operator structure — anticommuting modes and a fermion-parity grading — that the KMS article identifies as missing. Whether that structure lifts to a genuinely biquaternionic one is the open question this article is meant to expose.

The article is organized as follows. The next section fixes the classical field and its conjugate momentum, and identifies the constraint that forces the canonical structure to be imposed rather than assumed. The following section states the equal-time anticommutation relations and the reasons they, rather than commutators, are the consistent choice. The next section carries out the expansion in the parent article's plane-wave solutions. The section after that derives the anticommutators of the mode operators and builds the Fock space. The next section gives the Hamiltonian, the normal-ordering constant, and the four-momentum and charge. A section on spin and statistics records why anticommutation is forced here, without developing the full spin–statistics theorem, which is the subject of a planned companion article. A section relates the result to the KMS thermal-state framework. The article closes with an explicit accounting of what is standard and what is open.

## The Classical Field and Its Conjugate Momentum

The biquaternion Dirac field of the companion article is the map $\tilde{\Psi}:\mathbb{R}^{1,3}\to\mathbb{B}$ satisfying the linear, chirality-off-diagonal pair

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R,
$$

with massless limit $\tilde{\nabla}\tilde{\Psi}=0$; here $\tilde{\Psi}=\tilde{\Psi}_L+\tilde{\Psi}_R$ carries one component per chirality.

The companion solutions article works with its spinor-module representative, the four-component complex Dirac spinor $\psi$, on whose underlying two-component spinor module the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ acts. There the equation is the standard Dirac equation

$$
(i\gamma^\mu\partial/\partial Q_\mu-m)\psi=0,
$$

whose solutions, normalizations, and spin sums are established in the parent article and are used below without rederivation.

### The Lagrangian

The classical field theory is defined by the Lagrangian density

$$
\mathcal{L}=\bar{\psi}\,(i\gamma^\mu\partial/\partial Q_\mu-m)\,\psi,
$$

a real Lorentz scalar. Variation with respect to $\bar{\psi}$ returns the Dirac equation $(i\gamma^\mu\partial/\partial Q_\mu-m)\psi=0$, and variation with respect to $\psi$ returns its adjoint; the two are equivalent under $\bar\psi=\psi^\dagger\gamma^0$. This is the standard Lagrangian of a free Dirac field, written in the gamma-matrix convention of the companion articles.

### The Conjugate Momentum and Its Constraint

The canonical momentum conjugate to $\psi$ is

$$
\pi=\frac{\partial\mathcal{L}}{\partial(\partial/\partial Q_t\,\psi)}=i\,\psi^\dagger .
$$

The step is worth displaying, because it is the origin of the entire fermionic structure. The only term in $\mathcal{L}$ containing the time derivative is $\bar{\psi}\,i\gamma^0\partial/\partial Q_t\,\psi$. Since $\bar{\psi}\gamma^0=\psi^\dagger$ and $(\gamma^0)^2=I_4$, that term is $i\,\psi^\dagger\partial/\partial Q_t\,\psi$. Differentiating with respect to $\partial/\partial Q_t\,\psi_a$ therefore returns $i\psi^\dagger_a$, i.e. $\pi=i\psi^\dagger$.

The result is not $\partial\psi/\partial t'$, and this is the essential difference from a scalar field. The Dirac equation is first order in time, so the momentum is algebraically tied to the field by

$$
\chi=\pi-i\psi^\dagger\approx 0 .
$$

Equation $\chi\approx0$ is a **second-class constraint**: the Legendre transform is singular, the field and its momentum are not independent canonical variables, and the naive Poisson bracket must be replaced by the Dirac bracket. The standard resolution is not to quantize the brackets of the constrained system by hand but to impose the canonical (anti)commutation relations directly and verify that they are consistent with the field equation. The constraint is the technical reason a Dirac field is quantized by imposing relations on $\psi$ and $\pi$ rather than by the ordinary rule $[\phi,\pi]=i\delta$; it is also the reason the choice of bracket — commutator versus anticommutator — is not a free convention, as the next section explains. We do not reproduce the Dirac-bracket construction; it is textbook, and the companion articles do not need it.

### The Biquaternion Reading and the Open Point

Written on the spinor module, the Lagrangian and the canonical momentum are the standard ones. Written in the algebra, they are not yet fixed. The parent article's mass term is the linear, chirality-off-diagonal coupling, whose spinor-module representative is the ordinary mass term $m\psi$; the anti-Hermitian conjugation $\flat=-{}^{*}$ is the algebra's real structure, not the mass. The $\mathbb{B}$-intrinsic Lagrangian — the real scalar built from $\tilde{\nabla}\tilde{\Psi}$, $\tilde{\Psi}$, their conjugates, and the trace or norm pairing of the algebra — is not determined by the algebra alone, and neither is the intrinsic conjugate momentum. Two inequivalent transcriptions are available: one may treat the operator field as $\mathbb{B}$-valued and pair it with the real part of the trace, or one may treat it as valued in the spinor module and quantize there. We adopt the second, which is the parent article's working setting, and we return to the first in the closing section on what is open. The reader should keep in mind that the mode structure below is the standard one; what is being tested here is whether the biquaternion framework naturally reproduces it.

## Equal-Time Anticommutation Relations

Quantization promotes the classical field and its momentum to operators $\psi^{\mathrm{fop}}$, $\pi^{\mathrm{fop}}$ and imposes equal-time brackets. For the Dirac field the brackets are **anticommutators**:

$$
\boxed{\;\{\psi^{\mathrm{fop}}_a(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t'),{\psi^{\mathrm{fop}}_b}^\dagger(\vec y,t')\}=\delta_{ab}\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y)\;}$$

$$
\{\psi^{\mathrm{fop}}_a(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t'),\psi^{\mathrm{fop}}_b(\vec y,t')\}=0,\qquad
\{{\psi^{\mathrm{fop}}_a}^\dagger(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t'),{\psi^{\mathrm{fop}}_b}^\dagger(\vec y,t')\}=0$$

where $a,b$ are spinor indices. In terms of the conjugate momentum $\pi^{\mathrm{fop}}=i\psi^{\mathrm{fop}\dagger}$, the first relation reads

$$
\{\psi^{\mathrm{fop}}_a(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t'),\pi^{\mathrm{fop}}_b(\vec y,t')\}=i\,\delta_{ab}\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y),
$$

which is the fermionic analogue of the canonical relation $[\phi^{\mathrm{fop}},\pi^{\mathrm{fop}}]=i\delta^{(3)}$ of a scalar field. These are the standard canonical relations, and they are imposed rather than derived.

The choice of anticommutator over commutator is forced, and three reasons can be given at the level of this article. They are stated here because they are operative in the construction; the full spin–statistics theorem is the subject of a planned companion article and is not developed here.

**1. Boundedness of the energy.** As shown in the section on the Hamiltonian, the mode expansion of the energy contains a negative-frequency contribution proportional to $b^{\mathrm{fop}}\,b^{\mathrm{fop}\dagger}$. If the modes commuted, $b^{\mathrm{fop}}b^{\mathrm{fop}\dagger}=b^{\mathrm{fop}\dagger}b^{\mathrm{fop}}+e_t$, and the energy would be $H=\sum_{\vec p,r}E_{\vec p}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}-b^{\mathrm{fop}\dagger}b^{\mathrm{fop}})+\text{const}$, unbounded below: adding antiparticles would lower the energy without limit, and no stable vacuum would exist. If the modes anticommute, $b^{\mathrm{fop}}b^{\mathrm{fop}\dagger}=e_t-b^{\mathrm{fop}\dagger}b^{\mathrm{fop}}$, and the same expression becomes a positive sum plus a c-number. The anticommutator is what makes the negative-frequency modes into positive-energy antiparticles. This is the operator content of the Dirac sea.

**2. Microcausality.** For a field of spin $\tfrac12$, the commutator $[\psi^{\mathrm{fop}}(x),\bar{\psi^{\mathrm{fop}}}(y)]$ does **not** vanish for spacelike separated $x,y$, so quantizing with commutators would correlate measurements in causally disconnected regions. The anticommutator $\{\psi^{\mathrm{fop}}(x),\bar{\psi^{\mathrm{fop}}}(y)\}$ does vanish there, and it is the quantity that must be local for a fermion field. This is the content of Pauli's 1940 argument: the requirement that the fields commute or anticommute outside the light cone, together with the transformation properties of the spinor representation, selects anticommutation for half-integer spin.

**3. Positivity of the inner product.** Quantizing a half-integer-spin field with commutators produces states of negative norm; the anticommutator is what makes the Fock inner product positive-definite. This is the Hilbert-space form of the same obstruction.

The three reasons are aspects of one theorem. We note only that they all point the same way for a field whose one-particle states transform in the spinor representation — which is the case here, since the biquaternion algebra $\mathbb{B}$ acts on a two-dimensional complex spinor module.

## Field Expansion in the Plane-Wave Solutions

The classical equation is linear, so its general solution is a superposition of the plane waves constructed in the parent article. Those solutions come in two branches: the positive-frequency branch spanned by the spinors $w^{(r)}(\vec p)\exp(-ip\cdot x)$ and the negative-frequency branch spanned by $v^{(r)}(\vec p)\exp(+ip\cdot x)$, with $r=1,2$,

$$
E_{\vec p}=+\sqrt{\vec p^2+m^2},\qquad p\cdot x=E_{\vec p}t'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),
$$

and with the covariant normalizations and spin sums established there:

$$
\bar w^{(r)}w^{(s)}=2m\,\delta^{rs},\quad \bar v^{(r)}v^{(s)}=-2m\,\delta^{rs},\quad w^{(r){}^{*}}w^{(s)}=v^{(r){}^{*}}v^{(s)}=2E_{\vec p}\,\delta^{rs},
$$

$$
\sum_{r=1}^{2}w^{(r)}(\vec p)\bar w^{(r)}(\vec p)=\not p+m,\qquad
\sum_{r=1}^{2}v^{(r)}(\vec p)\bar v^{(r)}(\vec p)=\not p-m .
$$

Quantization consists in replacing the constant coefficients of the classical expansion by operators:

$$
\boxed{\;\psi^{\mathrm{fop}}(x)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec p}}}
\sum_{r=1}^{2}\Big[a^{\mathrm{fop}}_r(\vec p)\,w^{(r)}(\vec p)\,\exp(-ip\cdot x)
+b^{\mathrm{fop}\dagger}_r(\vec p)\,v^{(r)}(\vec p)\,\exp(+ip\cdot x)\Big]\;}.
$$

The field and its adjoint,

$$
\psi^{\mathrm{fop}\dagger}(y)=\int\!\frac{d^3k}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec k}}}
\sum_{s=1}^{2}\Big[a^{\mathrm{fop}\dagger}_s(\vec k)\,w^{(s){}^{*}}(\vec k)\,\exp(+ik\cdot y)
+b^{\mathrm{fop}}_s(\vec k)\,v^{(s){}^{*}}(\vec k)\,\exp(-ik\cdot y)\Big],
$$

together define the operator-valued field. The **annihilation** operators $a^{\mathrm{fop}}_r(\vec p)$ multiply the positive-frequency solutions, and the **creation** operators $b^{\mathrm{fop}\dagger}_r(\vec p)$ multiply the negative-frequency solutions. The attribution of a creation operator to the negative-frequency branch is the operator form of the reinterpretation of the Dirac sea: the modes of "negative frequency" are the antiparticles of positive energy.

Two structural remarks belong here. First, $\psi^{\mathrm{fop}}$ is **not Hermitian**, and it should not be: a complex Dirac field carries a conserved charge, and particle and antiparticle are distinct. Second, the expansion is written on the spinor module, following the parent article. In the algebra, each mode function is the module representative of a biquaternion plane wave $\tilde{\Psi}_0\exp\!\left(i\,\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar\right)$; the two branches are the two roots of the single biquaternion mass-shell condition

$$
\tilde P\tilde P^{\natural}=-m^2c^2\,e_t,
$$

and the polarization equation is the algebraic form of the momentum-space equation. Promoting the coefficients to operators is thus a transcription of the standard mode expansion onto the parent article's biquaternion plane waves; it is not, by itself, a derivation of the expansion from the algebra.

## Anticommutators of the Mode Operators

For the equal-time relations of Section 3 to hold, the mode operators must satisfy

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

It is worth verifying that these relations reproduce $\{\psi^{\mathrm{fop}}_a(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t'),{\psi^{\mathrm{fop}}_b}^\dagger(\vec y,t')\}=\delta_{ab}\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y)$, because the verification exposes a point of care about the relative phases of the two branches. Inserting the expansions and using the mode algebra gives, at equal times,

$$
\{\psi^{\mathrm{fop}}_a(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t'),{\psi^{\mathrm{fop}}_b}^\dagger(\vec y,t')\}
=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{2E_{\vec p}}
\Big[\sum_r w^{(r)}_a w^{(r){}^{*}}_b\,\exp(+i\vec p\cdot\vec\Delta)
+\sum_r v^{(r)}_a v^{(r){}^{*}}_b\,\exp(-i\vec p\cdot\vec\Delta)\Big],$$

where $\vec\Delta=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y$. The two phases are **opposite**: the positive-frequency term carries $\exp(+i\vec p\cdot\vec\Delta)$ and the negative-frequency term $\exp(-i\vec p\cdot\vec\Delta)$. From the spin sums one obtains the two useful combinations

$$
\sum_r w^{(r)}w^{(r){}^{*}}=E_{\vec p}I_4+m\gamma^0+\gamma^0\boldsymbol\gamma\cdot\vec p,\qquad
\sum_r v^{(r)}v^{(r){}^{*}}=E_{\vec p}I_4-m\gamma^0+\gamma^0\boldsymbol\gamma\cdot\vec p,
$$

so that, with $\theta=\vec p\cdot\vec\Delta$,

$$
\sum_r\Big[w^{(r)}w^{(r){}^{*}}\exp(+i\theta)+v^{(r)}v^{(r){}^{*}}\exp(-i\theta)\Big]
=E_{\vec p}\cos\theta\,I_4\cdot 2
+2\cos\theta\,\gamma^0\boldsymbol\gamma\cdot\vec p
+2im\sin\theta\,\gamma^0 .
$$

The first term is even in $\vec p$ and gives $2E_{\vec p}\delta^{(3)}(\vec\Delta)$ after dividing by $2E_{\vec p}$; the second and third terms are odd in $\vec p$ and vanish under symmetric integration. Hence the equal-time relation holds. The identity was checked numerically for a representative momentum ($m=1.3$, $|\vec p|=0.9$, $\vec p$ along $\vec e_z$): the spin sums above and their two combinations reproduce the right-hand sides to a maximum absolute error of $4.4\times10^{-16}$. The cancellation of the odd terms is exactly what the opposite phases of the two branches accomplish; had both phases been equal, the cross terms would have survived and the canonical relation would have failed.

### The Fock Space and Pauli Exclusion

The mode algebra generates the Fock space. Define the vacuum $|0\rangle$ by

$$
a^{\mathrm{fop}}_r(\vec p)|0\rangle=0=b^{\mathrm{fop}}_r(\vec p)|0\rangle \quad\text{for all } r,\ \vec p ,
$$

and build states by acting with the creation operators. The one-particle states are $a^{\mathrm{fop}\dagger}_r(\vec p)|0\rangle$ and the one-antiparticle states $b^{\mathrm{fop}\dagger}_r(\vec p)|0\rangle$. At fixed $\vec p$, the positive-frequency solutions span a two-dimensional complex space, and the full one-particle space is the $L^2$ completion of that solution space; the many-particle space is its **antisymmetric tensor algebra** (exterior algebra), because the mode operators anticommute. In particular,

$$
a^{\mathrm{fop}\dagger}_r(\vec p)a^{\mathrm{fop}\dagger}_s(\vec k)|0\rangle
=-\,a^{\mathrm{fop}\dagger}_s(\vec k)a^{\mathrm{fop}\dagger}_r(\vec p)|0\rangle,
$$

so the two-particle state is antisymmetric, and

$$
\big(a^{\mathrm{fop}\dagger}_r(\vec p)\big)^2=0,\qquad \big(b^{\mathrm{fop}\dagger}_r(\vec p)\big)^2=0,
$$

which is the Pauli exclusion principle as an algebraic identity: the square of a creation operator vanishes because $\{a^{\mathrm{fop}\dagger}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=0$. This is the sharpest sense in which the statistics is carried by the mode algebra. The construction of the biquaternion Fock space as an object in its own right — rather than as the exterior algebra of the spinor-module solution space — is the subject of a planned companion article; here we need only the mode algebra.

## The Hamiltonian and the Normal-Ordering Constant

The conserved energy of the free Dirac field is

$$
H=\int d^3x\;\psi^{\mathrm{fop}\dagger}\big(-i\gamma^0\boldsymbol\gamma\cdot\nabla+m\gamma^0\big)\psi^{\mathrm{fop}}
=\int d^3x\;\bar{\psi^{\mathrm{fop}}}\big(-i\boldsymbol\gamma\cdot\nabla+m\big)\psi^{\mathrm{fop}},
$$

the integrand being the $00$ component of the canonical energy–momentum tensor, equivalently the Legendre transform of the Lagrangian of the preceding section. Substituting the mode expansion and using the parent article's normalizations and orthogonality gives the standard result

$$
H=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}
\Big(a^{\mathrm{fop}\dagger}_r(\vec p)a^{\mathrm{fop}}_r(\vec p)
-b^{\mathrm{fop}}_r(\vec p)b^{\mathrm{fop}\dagger}_r(\vec p)\Big).
$$

The negative sign on the second term is the operator trace of the Dirac sea. Using the anticommutator $b^{\mathrm{fop}}_r(\vec p)b^{\mathrm{fop}\dagger}_r(\vec p)=e_t-b^{\mathrm{fop}\dagger}_r(\vec p)b^{\mathrm{fop}}_r(\vec p)$ (more precisely, its continuum form) this becomes

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
E_0=-\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}\,(2\pi)^3\delta^{(3)}(\mathbf 0)\,E_{\vec p}
=-\,2V\!\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}.
$$

Here $V$ is the volume in which the theory is placed, and $(2\pi)^3\delta^{(3)}(\mathbf 0)=V$ is the standard transcription of the continuum normalization. The constant is negative and quartically divergent, in contrast with the positive half-integer zero-point energy of a scalar field, and it is a c-number: it commutes with everything and does not affect the operator equations of motion. Normal ordering is the convention that removes it. For fermions the normal-ordering prescription moves every creation operator to the left of every annihilation operator and inserts a minus sign for each transposition of two fermion operators; for example $:\!b^{\mathrm{fop}}_r(\vec p)b^{\mathrm{fop}\dagger}_r(\vec k)\!:=-b^{\mathrm{fop}\dagger}_r(\vec k)b^{\mathrm{fop}}_r(\vec p)$. With this definition the constant term in $H$ is removed by construction.

The same mode algebra gives the other conserved charges. The normal-ordered four-momentum is

$$
:\!P^{\mathrm{fop}\mu}\!:\;=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}\,p^\mu
\Big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r+b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r\Big),\qquad p^\mu=(E_{\vec p},\vec p),
$$

and the normal-ordered electric charge, from $j^\mu=\bar\psi\gamma^\mu\psi$ with $j^0=\psi^\dagger\psi$, is

$$
:\!Ϙ^{\mathrm{fop}}\!:\;=\sum_{r}\int\!\frac{d^3p}{(2\pi)^3}
\Big(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r-b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r\Big),
$$

so that particles and antiparticles carry opposite charge, as they must. All three expressions are the standard ones; their derivation uses only the parent article's spinor relations.

The status of $E_0$ deserves one cautionary sentence. Its divergence is an ultraviolet feature of the free field, removed by the conventional normal-ordering prescription, and nothing in the biquaternion structure as used here changes that. Whether the biquaternion framework offers a distinguished or geometrically meaningful regularization of the vacuum energy is an open question, and we do not claim one.

## Spin and Statistics

The anticommutation relations are not a convention; they are selected. The three reasons given in Section 3 — boundedness of the energy, microcausality, and positivity of the norm — are all consequences of one structural fact: the one-particle states of the field transform in the **spinor representation** of the Lorentz group, and the biquaternion algebra realizes that representation on its module. For a field of half-integer spin the representation is double-valued: a rotation by $2\pi$ is the identity in the vector representation but minus the identity in the spinor representation, and only a rotation by $4\pi$ returns the spinor to itself. It is this two-valuedness, together with the requirement that the local observables be built from bilinears, that forces the anticommutator: the commutator of two spinor fields fails to vanish at spacelike separation, while the anticommutator does.

Equivalently, the operator algebra generated by the modes is **$\mathbb{Z}/2$-graded** by fermion parity. Define

$$
(-1)^F\,a^{\mathrm{fop}}_r(\vec p)\,(-1)^F=-a^{\mathrm{fop}}_r(\vec p),\qquad
(-1)^F\,b^{\mathrm{fop}}_r(\vec p)\,(-1)^F=-b^{\mathrm{fop}}_r(\vec p),\qquad
(-1)^F|0\rangle=|0\rangle ,
$$

so that $(-1)^F$ is $+1$ on states with an even number of particles and antiparticles and $-1$ on states with an odd number. The operators split into an even (bosonic) part commuting with $(-1)^F$ and an odd (fermionic) part anticommuting with it, and the rule that fermionic operators anticommute is precisely the statement that the algebra is graded-commutative. This grading is the structure the KMS article identifies as absent from the biquaternion algebra; the present construction supplies it on the operator algebra generated by the mode operators, which is a partial answer.

This article deliberately stops here. The full **spin–statistics theorem** — that integer-spin fields must be quantized with commutators and half-integer-spin fields with anticommutators, and the precise relation of that dichotomy to the topology of the Lorentz group — is the subject of a dedicated companion article. We have recorded only the reasons that are operative in the canonical construction, and we have not attempted to reproduce the theorem. In particular, the question of whether the biquaternion framework yields a *derivation* of spin–statistics rather than a *transcription* of the standard argument is not settled here.

## Relation to the KMS Thermal Framework

The KMS article characterizes thermal equilibrium by an analytic property of correlation functions. For operators $A,B$ in the algebra and a state $\omega_\beta$ at inverse temperature $\beta=\hbar/(k_BT)$, the thermal correlation function is

$$
F_{A B}(t')=\omega_\beta\big(A\,\alpha_{t'}(B)\big),
$$

with $\alpha_{t'}$ the Heisenberg evolution; the KMS condition states that $F_{A B}(t')$ extends analytically to the strip $0<\mathrm{Im}(t')<\beta$ and satisfies

$$
F_{A B}(t'+i\beta)=F_{B A}(-t')
$$

on its boundary. The KMS article observes that this boundary relation is the same for bosons and fermions, that the statistics enters instead through the algebra of the operators, and that a fermionic interpretation requires a $\mathbb{Z}/2$ grading together with the rule that fermionic operators anticommute — a rule the biquaternion algebra does not automatically supply.

The quantized Dirac field supplies exactly that rule. The mode algebra of Section 5 is graded by $(-1)^F$, and the fermionic operators anticommute. The KMS condition can therefore be stated for the thermal state

$$
\omega_\beta(\,\cdot\,)=\frac{1}{Z}\,\mathrm{Tr}\big(\exp(-\beta(H-\mu Ϙ^{\mathrm{fop}}))\,\cdot\,\big)
$$

on the Fock space, with $H$ and $Ϙ^{\mathrm{fop}}$ the normal-ordered operators above, $Z$ the partition function, and $\mu$ the chemical potential. The point of contact with the KMS article is sharp and elementary. Take a single mode of energy $E$ and normalize it so that $\{a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}\}=e_t$. In the Heisenberg picture $\alpha_{t'}(a^{\mathrm{fop}})=\exp(-iEt')a^{\mathrm{fop}}$ and $\alpha_{t'}(a^{\mathrm{fop}\dagger})=\exp(+iEt')a^{\mathrm{fop}\dagger}$, so

$$
F_{a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}}(t')=\exp(+iEt')\,\omega_\beta(a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}),\qquad
F_{a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}}(-t')=\exp(+iEt')\,\omega_\beta(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}).
$$

The KMS condition $F_{a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}}(t'+i\beta)=F_{a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}}(-t')$ then gives $\exp(-\beta E)\,\omega_\beta(a^{\mathrm{fop}}a^{\mathrm{fop}\dagger})=\omega_\beta(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}})$. Writing $n=\omega_\beta(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}})$ and using the anticommutator in the form $a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}=e_t-a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}$ yields $1-n=\exp(\beta E)n$, i.e.

$$
\boxed{\;n=\frac{1}{\exp(\beta E)+1}\;},
$$

the **Fermi–Dirac** distribution. The same computation for a bosonic mode, where the relevant relation is the commutator $a^{\mathrm{fop}}a^{\mathrm{fop}\dagger}=e_t+a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}$, gives $n=1/(\exp(\beta E)-1)$, the Bose–Einstein distribution. This is the cleanest sense in which the statistics is carried by the (anti)commutator and not by the KMS boundary relation, exactly as the KMS article states. In the continuum, the free-field thermal two-point function is

$$
\omega_\beta\big(a^{\mathrm{fop}\dagger}_r(\vec p)a^{\mathrm{fop}}_s(\vec k)\big)
=(2\pi)^3\,\delta_{rs}\,\delta^{(3)}(\vec p-\vec k)\,\frac{1}{\exp(\beta E_{\vec p})+1},
$$

and the time-ordered fermionic correlation functions built from it are **antiperiodic** in imaginary time with period $\beta$, hence periodic with period $2\beta$; the Fourier modes of the compact imaginary-time direction are consequently the fermionic Matsubara frequencies

$$
\omega_\nu=\frac{(2n+1)\pi}{\beta},
$$

in the KMS article's notation. The antiperiodicity is the fermionic twist that the KMS article ties to the spin structure of the field and to the missing grading; here it follows from the same anticommutator that produced the Fermi–Dirac distribution.

The structural facts the KMS article records remain intact. The imaginary time direction is intrinsic to the material sector $\mathbb{M}_-$; the complexified time direction in which the KMS continuation takes place is the sum of the imaginary time direction of $\mathbb{M}_-$ and the real time direction of $\mathbb{M}_+$; and the modular Hamiltonian $K=-\log\rho$ is a Hermitian element of the algebra, hence lies in the informational sector $\mathbb{M}_+$. What the present article adds is the operator algebra on which the thermal state is defined, together with the grading the KMS article flagged as absent. What it does **not** add is a genuinely biquaternionic construction of the thermal state: the state $\omega_\beta$ above is a complex-valued functional on the Fock space built from the spinor-module field, and whether it extends to a functional intrinsically defined on $\mathbb{B}$ — with the grading embedded in $\mathbb{B}$ rather than in the mode algebra, and with a spinor-module form of the fermionic twist — remains open. The relation established here is a consistency of structures, not a derivation of the fermionic KMS condition from the biquaternion algebra.

## What Is Standard and What Is Open

Because the question addressed here is itself an open question of the framework, we separate the two kinds of statement explicitly.

**Standard quantum field theory, transcribed.**

- The Lagrangian $\mathcal{L}=\bar\psi(i\gamma^\mu\partial/\partial Q_\mu-m)\psi$ and the conjugate momentum $\pi=i\psi^\dagger$, together with the second-class constraint $\pi-i\psi^\dagger\approx0$.
- The equal-time anticommutation relations, imposed and verified, and the three reasons anticommutation rather than commutation is forced.
- The mode expansion in the parent article's plane-wave solutions, with the covariant normalization $\bar w w=2m$, $w^\dagger w=2E$, and the parent's spin sums.
- The mode-operator anticommutators, the Fock space, and Pauli exclusion as the algebraic identity $(a^{\mathrm{fop}\dagger})^2=0$.
- The Hamiltonian $H=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}+b^{\mathrm{fop}\dagger}b^{\mathrm{fop}})$ after normal ordering, the normal-ordering constant $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$, and the four-momentum and charge.
- The Fermi–Dirac distribution as the consequence of the KMS condition together with the anticommutator, and the fermionic Matsubara frequencies.

**Open in the biquaternion framework.**

- **The intrinsic operator field.** Whether the quantized field should be $\mathbb{B}$-valued, $M_2(\mathbb{C})$-valued, or spinor-module-valued, and to what extent these give inequivalent quantizations.
- **The intrinsic Lagrangian and momentum.** The $\mathbb{B}$-intrinsic Lagrangian, its real-scalar pairing, and the conjugate momentum are not fixed by the algebra alone; the spinor-module transcription is the one adopted above.

- **The biquaternion Fock space.** Whether it is the exterior algebra of the spinor-module solution space, or a construction native to $\mathbb{B}$; the planned companion article on the Fock space is the natural place to settle this.
- **The grading.** The $\mathbb{Z}/2$ grading is supplied here on the mode algebra; embedding it in $\mathbb{B}$ itself, as the KMS article requires, is not done.
- **The spin–statistics theorem.** Whether the framework derives spin–statistics or only transcribes it is left to the dedicated article.
- **The vacuum energy.** Whether the biquaternion structure singles out a regularization of $E_0$, or assigns it a geometric meaning, is open.
- **Empirical content.** As with the rest of the framework, whether any of this yields a prediction distinguishing it from standard quantum field theory is the unanswered question.

The extension attempted here is therefore **not canonical** in the framework: the part that works is the standard canonical quantization of the Dirac field, expressed in the parent article's plane-wave solutions and the material- and informational-sector notation; the part that is genuinely biquaternionic is not yet fixed. This article is the first attempt at the companion article's second-quantization question, and it should be read as delimiting the problem rather than closing it.

## Summary

The biquaternion Dirac field is quantized by promoting its spinor-module representative to an operator-valued field. The classical theory has Lagrangian $\mathcal{L}=\bar\psi(i\gamma^\mu\partial/\partial Q_\mu-m)\psi$ and conjugate momentum $\pi=i\psi^\dagger$; the momentum is algebraically tied to the field by a second-class constraint, so the canonical structure is imposed rather than assumed. The equal-time relations are anticommutators,

$$
\{\psi^{\mathrm{fop}}_a(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t'),{\psi^{\mathrm{fop}}_b}^\dagger(\vec y,t')\}=\delta_{ab}\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y)$$

with all other equal-time anticommutators vanishing; anticommutation rather than commutation is forced by the boundedness of the energy, by microcausality, and by positivity of the norm, all three being consequences of the spinor character of the field.

The field expands in the plane-wave solutions established by the parent article,

$$
\psi^{\mathrm{fop}}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\vec p}}}\sum_r
\Big[a^{\mathrm{fop}}_r(\vec p)w^{(r)}(\vec p)\exp(-ip\cdot x)+b^{\mathrm{fop}\dagger}_r(\vec p)v^{(r)}(\vec p)\exp(+ip\cdot x)\Big],
$$

with the mode anticommutators $\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=\{b^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k)$ and all others zero. These reproduce the equal-time relation: the positive- and negative-frequency branches enter with opposite phases, the even part of the spin sums integrates to the delta function, and the odd parts cancel. The resulting Fock space carries Pauli exclusion as the algebraic identity $(a^{\mathrm{fop}\dagger}_r)^2=0$.

The Hamiltonian is $H=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}_ra^{\mathrm{fop}}_r+b^{\mathrm{fop}\dagger}_rb^{\mathrm{fop}}_r)$ after normal ordering, with the negative quartically divergent normal-ordering constant $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$ removed. The normal-ordered charge has particles and antiparticles of opposite sign. The mode algebra is $\mathbb{Z}/2$-graded by fermion parity, which is the structure the KMS article identifies as missing; with it, the KMS condition plus the anticommutator yields the Fermi–Dirac distribution and the antiperiodic imaginary-time correlators whose Matsubara frequencies are $(2n+1)\pi/\beta$.

The extension is a transcription of standard canonical quantization onto the parent article's biquaternion plane waves, not a derivation of the quantized structure from the algebra $\mathbb{B}$. The intrinsic $\mathbb{B}$-valued Lagrangian and momentum, the biquaternion Fock space, and the embedding of the grading in $\mathbb{B}$ remain open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_\mu \vec e_\mu\,\partial/\partial Q_\mu$ | Biquaternionic gradient (Dirac operator) |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\tilde{\Psi}$ | Classical biquaternion Dirac field |
| $\tilde{\Psi}^\flat=-\tilde{\Psi}^{*}$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\psi=(\psi_L,\psi_R)$, $\bar\psi=\psi^\dagger\gamma^0$ | Dirac spinor (spinor module) and its adjoint |
| $\gamma^\mu$, $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$ | Gamma matrices and chirality operator |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the $\gamma^\mu$; $g=-\eta$ |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | Spacetime metric of the $ict'$ gradient |
| $\mathcal{L}=\bar\psi(i\gamma^\mu\partial/\partial Q_\mu-m)\psi$ | Dirac Lagrangian density |
| $\pi=\partial\mathcal{L}/\partial(\partial/\partial Q_t\,\psi)=i\psi^\dagger$ | Conjugate momentum; $\pi-i\psi^\dagger\approx0$ is second class |
| $w^{(r)}(\vec p),v^{(r)}(\vec p)$ | Parent article's positive- and negative-frequency spinors |
| $\bar w w=2m$, $w^\dagger w=2E_{\vec p}$ | Covariant and Hermitian normalizations |
| $p^\mu=(E_{\vec p},\vec p)$, $\not p=\gamma^0E_{\vec p}-\boldsymbol\gamma\cdot\vec p$ | Four-momentum and Feynman slash |
| $\tilde P\tilde P^{\natural}=-m^2c^2\,e_t$ | Biquaternionic mass-shell condition |
| $\psi^{\mathrm{fop}}$, $a^{\mathrm{fop}}_r(\vec p)$, $b^{\mathrm{fop}}_r(\vec p)$ | Quantized field; particle and antiparticle annihilation operators |
| $\{a^{\mathrm{fop}}_r(\vec p),a^{\mathrm{fop}\dagger}_s(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k)$ | Mode anticommutator |
| $H$, $:\!H\!:$ | Hamiltonian and its normal-ordered form |
| $E_0=-2V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$ | Normal-ordering constant (vacuum energy) |
| $(-1)^F$ | Fermion-parity grading |
| $\beta=\hbar/(k_BT)$, $\omega_\beta$, $\alpha_{t'}$ | Inverse temperature, thermal state, Heisenberg evolution |
| $F_{A B}(t'+i\beta)=F_{B A}(-t')$ | KMS condition |
| $K=-\log\rho$ | Modular Hamiltonian (Hermitian, in $\mathbb{M}_+$) |
| $\omega_\nu=(2n+1)\pi/\beta$ | Fermionic Matsubara frequencies |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and the prediction of the antiparticle.
- W. Pauli, "The connection between spin and statistics," *Physical Review* **58** (1940) 716–722, for the theorem that forces anticommutation for half-integer spin.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the canonical quantization of the Dirac field.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the constrained canonical structure, the mode algebra, and the vacuum energy.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the mode expansion, the spin sums, and the Hamiltonian in the convention used here.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the spin–statistics connection and the construction of the Fock space.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic formulation in which the KMS condition is stated.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), and J. I. Kapusta and C. Gale, *Finite-Temperature Field Theory* (Cambridge, 2006), for the imaginary-time formalism and the fermionic Matsubara frequencies.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), and Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Clifford-algebraic background to the biquaternion and spinor structures.
