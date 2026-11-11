# __The Modular Hamiltonian in Biquaternionic Form__

## Introduction

The Tomita–Takesaki theory attaches to a cyclic and separating vector $\Omega$ on a von Neumann algebra $M$ a canonical one-parameter group of automorphisms, the **modular flow**
$$
\sigma_{r'_{t}}(A)=\Delta^{ir'_t}A\Delta^{-ir'_t},
$$
built from the modular operator $\Delta=S^*S$ of the Tomita involution $S$. The companion article *The Hermitian Tomita–Takesaki Theory under the Biquaternion Framework* constructs $S$, $\Delta$ and $J$ in the biquaternion algebra $\mathbb{B}$ and verifies the resulting flow identities by recomputation. It records, but does not develop, the **operator that generates the flow**. The present article is about that operator, the **modular Hamiltonian** $\tilde H_{\Psi,\mathrm{modular}}$.

Writing $\Delta=\exp(-\tilde H_{\Psi,\mathrm{modular}})$ — equivalently $\tilde H_{\Psi,\mathrm{modular}}=-\log\Delta$ — the modular flow is Hamiltonian evolution under $\tilde H_{\Psi,\mathrm{modular}}$,
$$
\sigma_{r'_{t}}(\tilde Q_3)=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\,\tilde Q_3\,\exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t),
\qquad
\frac{d}{dr'_t}\sigma_{r'_{t}}(\tilde Q_3)\Big|_{r'_t=0}=-i[\tilde H_{\Psi,\mathrm{modular}},\tilde Q_3],
$$
and the KMS state of *The KMS Condition and the Biquaternion Framework* is the **thermal state of $\tilde H_{\Psi,\mathrm{modular}}$**: the state is Gibbs with respect to the modular Hamiltonian. This is the content of the Takesaki–Winnink theorem, quoted by the modular-theory parent and used here unchanged. The modular Hamiltonian is therefore to the modular flow what the Hamiltonian is to ordinary time evolution, and the two roles can be separated: the physical Hamiltonian $\tilde H_\Psi$ is what appears in the Gibbs weight, while $\tilde H_{\Psi,\mathrm{modular}}$ is the shifted and rescaled operator whose flow the state is KMS with respect to, $\tilde H_{\Psi,\mathrm{modular}}=\beta\tilde H_\Psi+(\log Z)e_t$ for a Gibbs state.

The article is deliberately narrow. It is the companion of one theorem and three article parents: the modular-theory article supplies $S$, $\Delta$ and the flow; the KMS article supplies the boundary relation whose generator $\tilde H_{\Psi,\mathrm{modular}}$ is; the partition-function article supplies the Gibbs form that ties $\tilde H_{\Psi,\mathrm{modular}}$ to $\tilde H_\Psi$. This article does three things the parents do not. It defines $\tilde H_{\Psi,\mathrm{modular}}$ from $\Delta$ and checks the two hypotheses on which that definition rests — the cyclic-and-separating hypothesis, inherited from the construction of $\Delta$, and the **strict positivity** of $\Delta$, without which $-\log\Delta$ does not exist. It fixes the **sign convention** in $\Delta=\exp(-\tilde H_{\Psi,\mathrm{modular}})$ and holds it, because the sign of $\tilde H_{\Psi,\mathrm{modular}}$ is the standard error in this subject and the opposite convention reverses which flow is KMS. And it isolates the structural question that the finite-dimensional model cannot settle: whether $\tilde H_{\Psi,\mathrm{modular}}$ is a **local** operator, which it is not in general, the exceptional cases being exactly the ones in which the modular flow is a geometric symmetry flow (Bisognano–Wichmann).

Three features organize what follows.

- **$\tilde H_{\Psi,\mathrm{modular}}$ exists only when $\Delta$ does.** Its construction inherits the whole hypothesis of the Tomita–Takesaki theorem — $\Omega$ cyclic and separating for $M$, equivalently the state faithful — and does not assume it afresh. Positivity of $\Delta$ is where that hypothesis reappears spectrally: $\Delta=S^*S\ge 0$ is automatic, but $\Delta>0$ is the faithfulness condition, and $-\log\Delta$ is defined precisely then.
- **$-\log\Delta$ is well defined only because $\Delta$ is positive.** The spectral theorem gives $\log\Delta$ for a positive self-adjoint operator; at an eigenvalue $0$ the logarithm diverges and no $\tilde H_{\Psi,\mathrm{modular}}$ exists. The check is not a formality, and the finite-dimensional model exhibits the failure.
- **Locality of $\tilde H_{\Psi,\mathrm{modular}}$ is a question with a known exceptional answer.** In a quantum field theory the modular Hamiltonian of a region is generically a nonlocal operator; it is local (a geometric generator) in the cases covered by Bisognano–Wichmann and its conformal extension. The biquaternion framework houses the wedge case, because the boost generator is a Hermitian element $G_1=i\vec e_x\in\mathbb{B}_{\Psi}$; it does not house the ball case, because the special conformal generators are not elements of $\mathbb{B}$.

The article proceeds as follows. The modular Hamiltonian is defined from $\Delta$, the hypotheses are checked, and the sign convention is fixed. The finite-dimensional realization in $\mathbb{B}$ is recalled from the parents and completed with $\tilde H_{\Psi,\mathrm{modular}}$'s spectral form. $\tilde H_{\Psi,\mathrm{modular}}$ is then verified to generate the same flow as $\Delta^{ir'_t}$. The trace formula is used to show that the Gibbs form is a scalar extraction. A closing section separates what is established from what is a gap.

## The Generator of the Modular Flow

### Definition from the Modular Operator

Let $M$ be a von Neumann algebra with a cyclic and separating vector $\Omega$, and let $S=J\Delta^{1/2}$ be the polar decomposition of the Tomita operator, so that $\Delta=S^*S$ is self-adjoint and $\Delta\ge 0$. The **modular Hamiltonian** is
$$
\tilde H_{\Psi,\mathrm{modular}}:=-\log\Delta,
$$
defined by the spectral theorem on the positive self-adjoint operator $\Delta$. The defining relation is
$$
\Delta=\exp(-\tilde H_{\Psi,\mathrm{modular}}),
\qquad\text{equivalently}\qquad
\tilde H_{\Psi,\mathrm{modular}}=-\log\Delta .
$$
Since the logarithm is taken on a positive operator, $\tilde H_{\Psi,\mathrm{modular}}$ is self-adjoint, and it is the generator of the modular group in the following precise sense:
$$
\Delta^{ir'_t}=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t),
\qquad
\sigma_{r'_{t}}(\tilde Q_3)=\Delta^{ir'_t}\tilde Q_3\Delta^{-ir'_t}=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\tilde Q_3 \exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t),
\qquad
\frac{d}{dr'_t}\sigma_{r'_{t}}(\tilde Q_3)\Big|_{r'_t=0}=-i[\tilde H_{\Psi,\mathrm{modular}},\tilde Q_3].
$$
The last identity is the statement that the modular flow is Hamiltonian evolution with generator $\tilde H_{\Psi,\mathrm{modular}}$. The flow is trivial, $\sigma_{r'_{t}}=\mathrm{id}$, exactly when $\Delta=1$, i.e. exactly when $\tilde H_{\Psi,\mathrm{modular}}$ is central; in the finite-dimensional model this is the tracial state, as the parent records.

### The Hypotheses Are Inherited, Not Assumed Afresh

Two hypotheses are load-bearing, and both are inherited from the construction of $\Delta$.

**Cyclic and separating.** The Tomita operator $S_0(A\Omega)=A^*\Omega$ is well defined precisely when $\Omega$ is separating, and densely defined precisely when $\Omega$ is cyclic. Without both, the polar decomposition $S=J\Delta^{1/2}$ — hence $\Delta$, hence $\tilde H_{\Psi,\mathrm{modular}}$ — does not exist. In the GNS representation, cyclic and separating is equivalent to the state being **faithful**. So defining a modular Hamiltonian is defining it for a faithful state, and nothing here weakens that requirement.

**Positivity of $\Delta$.** The identity $\Delta=S^*S$ makes $\Delta\ge0$ automatic, but $-\log\Delta$ exists only if $\Delta$ is **strictly** positive,
$$
\Delta>0 \quad\Longleftrightarrow\quad \ker\Delta=\{0\}.
$$
The kernel of $\Delta$ equals the kernel of $S$, so $\Delta>0$ is again the faithfulness hypothesis: a non-faithful state gives $\Delta$ a zero eigenvalue, and at that eigenvalue $-\log\Delta$ diverges. This is the sense in which positivity is not a technicality. It is the same hypothesis as cyclic and separating, read off the spectrum of $\Delta$ rather than off the vector. Section "Verification: $\tilde H_{\Psi,\mathrm{modular}}$ Generates the Modular Flow" exhibits the failure explicitly.

**Self-adjointness and unitarity.** Because $\Delta>0$, the spectral theorem gives a self-adjoint $\log\Delta$ and hence a self-adjoint $\tilde H_{\Psi,\mathrm{modular}}$; the $*$-unitary group $\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)=\Delta^{ir'_t}$ is then well defined for all real $r'_t$, and $\Delta^{ir'_t}$ is $*$-unitary. The flow $\sigma_{r'_{t}}$ is thus a one-parameter group of $*$-automorphisms of $M$, as the parent verifies, and $\tilde H_{\Psi,\mathrm{modular}}$ is the self-adjoint generator of the $*$-unitary group that implements it.

### The Sign Convention, Fixed and Held

The relation between $\Delta$ and $\tilde H_{\Psi,\mathrm{modular}}$ is a convention, and the two choices are inequivalent. This article uses
$$
\Delta=\exp(-\tilde H_{\Psi,\mathrm{modular}}),\qquad \Delta^{ir'_t}=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t),\qquad
\sigma_{r'_{t}}(\tilde Q_3)=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\tilde Q_3 \exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t).
$$
The opposite choice, $\Delta=\exp(+\tilde H_{\Psi,\mathrm{modular}})$ with $\Delta^{ir'_t}=\exp(+i\tilde H_{\Psi,\mathrm{modular}}r'_t)$, is the same equation with $\tilde H_{\Psi,\mathrm{modular}}\mapsto-\tilde H_{\Psi,\mathrm{modular}}$. It is not a relabelling: the Takesaki–Winnink theorem says that a faithful normal state satisfies the KMS condition with respect to $\sigma_{-r'_t}$, not $\sigma_{r'_{t}}$, and reversing the sign of $\tilde H_{\Psi,\mathrm{modular}}$ reverses the flow and exchanges the two. In the finite-dimensional model the convention is pinned by $\tilde{Ϛ}_{\Psi}=\exp(-\tilde H_{\Psi,\mathrm{modular}})$ and $\sigma_{r'_{t}}(\tilde Q_3)=\tilde{Ϛ}_{\Psi}^{ir'_t}\tilde Q_3\tilde{Ϛ}_{\Psi}^{-ir'_t}$, which is the parent's convention; the generator identity $\frac{d}{dr'_t}\sigma_{r'_{t}}(\tilde Q_3)|_{r'_t=0}=-i[\tilde H_{\Psi,\mathrm{modular}},\tilde Q_3]$ follows from it and is the form used throughout. A displayed formula that writes $\Delta^{ir'_t}=\exp(+i\tilde H_{\Psi,\mathrm{modular}}r'_t)$ together with $\tilde H_{\Psi,\mathrm{modular}}=-\log\Delta$ is internally inconsistent — it would give $\Delta^{ir'_t}=\Delta^{-ir'_t}$ — and the sign is fixed here once, in the direction above, and held.

### The State Is Thermal with Respect to $\tilde H_{\Psi,\mathrm{modular}}$

The KMS property gives $\tilde H_{\Psi,\mathrm{modular}}$ its **physical interpretation**. Normalized to $\beta=1$, a faithful normal state $\omega$ satisfies the KMS boundary relation with respect to the flow $\sigma_{-r'_t}$ of its modular group. In the finite-dimensional model, where the state is realized by a density $\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi}$ that is positive definite and of trace one,
$$
\omega(\tilde Q_3)=\mathrm{Tr}(\tilde{Ϛ}_{\Psi}\,\tilde Q_3^{*}),
\qquad
\tilde{Ϛ}_{\Psi}=\exp(-\tilde H_{\Psi,\mathrm{modular}}),
\qquad
\tilde H_{\Psi,\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi},
$$
so the state is the Gibbs state of $\tilde H_{\Psi,\mathrm{modular}}$ at unit temperature. The physical Hamiltonian is recovered by rescaling: for a Gibbs state at inverse temperature $\beta$,
$$
\tilde H_{\Psi,\mathrm{modular}}=\beta\tilde H_\Psi+(\log Z)e_t,
\qquad
Z=\mathrm{Tr}\big(\exp(-\beta H)\big),
$$
so $\tilde H_{\Psi,\mathrm{modular}}$ differs from $\beta\tilde H_\Psi$ by the additive scalar $\log Z$ that normalizes the state. The modular Hamiltonian is thus not the physical Hamiltonian; it is the operator whose unit-temperature Gibbs state is the given state, and the normalization $\log Z$ — hence the free energy $F=-\beta^{-1}\log Z$ — is carried by its scalar part.

## The Modular Hamiltonian in the Biquaternion Algebra

### The Finite-Dimensional Model, Recalled

The parents realize the construction in the algebra itself. Take
$$
M=\mathbb{B}\cong M_2(\mathbb{C}),\qquad \Omega=e_t,\qquad
\omega(\tilde Q_3)=\mathrm{Tr}(\tilde{Ϛ}_{\Psi}\,\tilde Q_3^{*}),
$$
with $\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi}$ positive definite and of trace one, and the GNS inner product
$$
\langle\tilde Q_3,\tilde Q_1\rangle_{\tilde{Ϛ}_{\Psi}}=\mathrm{Tr}\big(\tilde{Ϛ}_{\Psi}\,\tilde Q_3^{*}\tilde Q_1\big).
$$
The vector $\Omega=e_t$ is cyclic and separating exactly because $\tilde{Ϛ}_{\Psi}>0$; the state is faithful for the same reason. The modular-theory parent computes the polar decomposition of $S_0(\tilde Q_3)=\tilde Q_3^{*}$ in closed form:
$$
\Delta(\tilde Q_3)=e^{-\tilde H_{\Psi,\mathrm{modular}}}\,\tilde Q_3\,e^{\tilde H_{\Psi,\mathrm{modular}}},
\qquad
\Delta^{1/2}(\tilde Q_3)=e^{-\tilde H_{\Psi,\mathrm{modular}}/2}\tilde Q_3\,e^{\tilde H_{\Psi,\mathrm{modular}}/2},
\qquad
J(\tilde Q_3)=e^{-\tilde H_{\Psi,\mathrm{modular}}/2}\tilde Q_3^{*}e^{\tilde H_{\Psi,\mathrm{modular}}/2},
\qquad
\sigma_{r'_{t}}(\tilde Q_3)=e^{-ir'_t\tilde H_{\Psi,\mathrm{modular}}}\tilde Q_3\,e^{ir'_t\tilde H_{\Psi,\mathrm{modular}}}.
$$
Since $\tilde{Ϛ}_{\Psi}>0$, its logarithm is defined and
$$
\boxed{\;\tilde H_{\Psi,\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}\ \in\mathbb{B}_{\Psi}\;}
$$
is a Hermitian element of the algebra. The two displays are the same $\tilde H_{\Psi,\mathrm{modular}}$ seen twice: as an algebra element, $\tilde{Ϛ}_{\Psi}=\exp(-\tilde H_{\Psi,\mathrm{modular}})$; as the modular operator on the Hilbert space, $\Delta(\tilde Q_3)=\exp(-\tilde H_{\Psi,\mathrm{modular}})\tilde Q_3\,\exp(\tilde H_{\Psi,\mathrm{modular}})$, so that
$$
\Delta^{ir'_t}(\tilde Q_3)=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\tilde Q_3\,\exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t).
$$
That $\tilde H_{\Psi,\mathrm{modular}}$ lies in $\mathbb{B}_{\Psi}$ is the parent's algebraic fact, and it is the reason the corpus says the modular Hamiltonian is an object of the informational sector: the state $\tilde{Ϛ}_{\Psi}=\exp(-\tilde H_{\Psi,\mathrm{modular}})$ and the generator $\tilde H_{\Psi,\mathrm{modular}}$ are both Hermitian, while the material sector $\mathbb{B}_{\Phi}$ supplies the imaginary-time direction in which the KMS analyticity takes place.

### The Cartan Amplitude and the Modular State

A faithful state is positive, so its own Cartan pairing is trivial: $\tilde{Ϛ}_{\Psi}=\tilde{Ϛ}_{\Psi}\,e_t$, with amplitude $\tilde{Ϛ}_{\Psi}$ and phase $e_t$. The amplitude that carries the modular information is its square root. Write

$$
\tilde{Ϛ}_{\Psi}=\tilde Q_{\mathrm n}^{2},\qquad \tilde Q_{\mathrm n}=\tilde{Ϛ}_{\Psi}^{1/2}>0,
\qquad
\langle\tilde Q_{\mathrm n},\tilde Q_{\mathrm n}\rangle_{*}=\tfrac12,
$$

with $\tilde Q_{\mathrm n}$ the bracket-normalised Cartan amplitude. Then

$$
\tilde H_{\Psi,\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}=-2\log\tilde Q_{\mathrm n}
$$

exactly, with no additive constant. For an unnormalised positive amplitude $\tilde Q_H$, the state is $\tilde{Ϛ}_{\Psi}=\tilde Q_H^{2}/(2\langle\tilde Q_H,\tilde Q_H\rangle_{*})$ and the same statement reads

$$
\tilde H_{\Psi,\mathrm{modular}}=-2\log\tilde Q_H+\log\!\bigl(2\langle\tilde Q_H,\tilde Q_H\rangle_{*}\bigr)e_t,
$$

the last term being the central constant that a modular Hamiltonian always carries. The derivation is in *The General Polar Decomposition, the Amplitude and the Operator-to-State Map*, §*The Modular Reading*; it is repeated here because this article is where the flow is used.

**The spectrum.** If $\tilde{Ϛ}_{\Psi}$ has eigenvalues $\lambda_\pm$, then $\tilde Q_{\mathrm n}$ has eigenvalues $\sqrt{\lambda_\pm}$ and $\tilde H_{\Psi,\mathrm{modular}}$ has eigenvalues $-\log\lambda_\pm$. The amplitude's eigenvalues are the square roots of the Boltzmann weights; the modular Hamiltonian's are their logarithms. The factor $2$ is the exponent in $\tilde{Ϛ}_{\Psi}=\tilde Q_{\mathrm n}^{2}$: the state is the square of the amplitude.

**The flow.** The modular flow is generated by $\tilde H_{\Psi,\mathrm{modular}}$,

$$
\Delta^{ir'_t}=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)=\tilde Q_{\mathrm n}^{2ir'_t},
$$

which is the same conjugation as before. The amplitude is the operator whose logarithm generates the flow; the state has no Cartan phase, so the flow is the flow of the amplitude alone.

**The reading.** The modular Hamiltonian is minus twice the logarithm of the Cartan amplitude. A state has no Cartan phase; its amplitude is its square root, and its modular flow is the logarithm of that amplitude. This is the exact sense in which the Cartan amplitude is the modular square root, and it is the state-side counterpart of the operator-side statement that the amplitude is what remains when the phase is forgotten.

**The boundary.** The reading needs $\tilde{Ϛ}_{\Psi}>0$. At a pure state $\lambda_-=0$, $\tilde Q_{\mathrm n}$ is rank one and not invertible, $\log\tilde Q_{\mathrm n}$ diverges, and $\tilde H_{\Psi,\mathrm{modular}}$ does not exist; the amplitude is still defined, but its logarithm is not. The modular conjugation is anti-unitary and is not the Cartan phase; the two objects must not be identified.

### The Spectral Form of $\tilde H_{\Psi,\mathrm{modular}}$

Write the faithful state in Bloch form,
$$
\tilde{Ϛ}_{\Psi}=\tfrac12\big(e_t+i\vec r\cdot\mathbf e\big),
\qquad |\vec r|<1,
\qquad
\lambda_\pm=\tfrac12\big(1\pm|\vec r|\big)>0,
$$
with $\lambda_+,\lambda_-$ the eigenvalues of $\tilde{Ϛ}_{\Psi}$ and $\vec u_r=\vec r/|\vec r|$. Then
$$
\boxed{\;\tilde H_{\Psi,\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}
=a_0\,e_t+i\,\vec a\cdot\mathbf e,
\qquad
a_0=-\tfrac12\log\det\tilde{Ϛ}_{\Psi}=-\tfrac12\log\!\Big(\tfrac14\big(1-|\vec r|^2\big)\Big),
\qquad
\vec a=-\tfrac12\log\frac{\lambda_+}{\lambda_-}\,\vec u_r\;}.
$$
This is the explicit operator: a real scalar part fixed by the determinant of the state, and an imaginary vector part along the Bloch vector, with magnitude the logarithm of the eigenvalue ratio. Two limits are immediate. The tracial state $\vec r=0$ gives $\lambda_+=\lambda_-$, hence
$$
\tilde H_{\Psi,\mathrm{modular}}=(\log 2)e_t,\qquad \Delta=1,\qquad \sigma_{r'_{t}}=\mathrm{id},
$$
the trivial modular flow the parent identifies. A pure state $|\vec r|\to1$ gives $\lambda_-\to0$, so $\det\tilde{Ϛ}_{\Psi}\to0$ and $|\vec a|\to\infty$: the modular Hamiltonian diverges as faithfulness is lost. The divergence is the positivity hypothesis of the previous section appearing in the formula; a pure state on $M_2(\mathbb{C})$ is not faithful, $\Delta$ acquires the eigenvalue $0$, and $-\log\Delta$ does not exist.

The eigenvalues of $\Delta$ on the algebra are the ratios of the eigenvalues of $\tilde{Ϛ}_{\Psi}$,
$$
\operatorname{spec}\Delta=\Big\{\frac{\lambda_i}{\lambda_j}\Big\}
=\Big\{1,\ \frac{\lambda_+}{\lambda_-},\ \frac{\lambda_-}{\lambda_+}\Big\},
$$
all strictly positive because $\lambda_\pm>0$. This is the concrete form of $\Delta>0$.

### $\tilde H_{\Psi,\mathrm{modular}}$ Generates the Same Flow as $\Delta^{ir'_t}$

The two displays are equal, not merely analogous. From $\tilde{Ϛ}_{\Psi}=\exp(-\tilde H_{\Psi,\mathrm{modular}})$,
$$
\Delta^{ir'_t}(\tilde Q_3)=e^{-ir'_t\tilde H_{\Psi,\mathrm{modular}}}\tilde Q_3\,e^{ir'_t\tilde H_{\Psi,\mathrm{modular}}}
=\big(\exp(-\tilde H_{\Psi,\mathrm{modular}})\big)^{ir'_t}\tilde Q_3\big(\exp(-\tilde H_{\Psi,\mathrm{modular}})\big)^{-ir'_t}
=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\tilde Q_3\,\exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t),
$$
using $(\exp(-\tilde H_{\Psi,\mathrm{modular}}))^{ir'_t}=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)$. Differentiating at $r'_t=0$,
$$
\frac{d}{dr'_t}\Delta^{ir'_t}(\tilde Q_3)\Big|_{r'_t=0}
=\frac{d}{dr'_t}\Big(\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\tilde Q_3\,\exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t)\Big)\Big|_{r'_t=0}
=-i\tilde H_{\Psi,\mathrm{modular}}\tilde Q_3+i\tilde Q_3\tilde H_{\Psi,\mathrm{modular}}
=-i[\tilde H_{\Psi,\mathrm{modular}},\tilde Q_3],
$$
which is the generator identity of the definition. So the $\tilde H_{\Psi,\mathrm{modular}}$ constructed from the state is the same operator that generates the flow constructed from the Tomita operator, and the check is a recomputation rather than a quotation.

## Verification: $\tilde H_{\Psi,\mathrm{modular}}$ Generates the Modular Flow

The identities above were recomputed symbolically and numerically in the biquaternion algebra, using the matrix representation $\mathsf{M}_2(\vec e_\eta)=-i\sigma_\eta$, $\mathsf{M}_2(i)=iI_2$. The state was the parent's generic faithful state,
$$
\vec r=\big(\tfrac{3}{10},\tfrac{2}{5},-\tfrac15\big),
\qquad |\vec r|^2=\tfrac{29}{100},
\qquad
\lambda_\pm=\tfrac12\pm\frac{\sqrt{29}}{20},
$$
chosen — in the parent, and independently of the derivation here — to lie neither on a basis axis nor along a thermal direction, and a second, physical thermal state was used as the independent case.

| Check | Result |
|---|---|
| $\Delta$ eigenvalues $\lambda_+/\lambda_-$, $\lambda_-/\lambda_+$ | $3.333849$, $0.299954$, both $>0$ |
| $\tilde H_{\Psi,\mathrm{modular}}$ Hermitian, components real | $a_0=0.864392$, $\vec a=(-0.335401,-0.447202,0.223601)$ |
| $a_0=-\tfrac12\log\det\tilde{Ϛ}_{\Psi}$, $\vec a=-\tfrac12\log(\lambda_+/\lambda_-)\vec u_r$ | agreement to $10^{-15}$ |
| $\sigma_{r'_{t}}(\tilde Q_3)=\tilde{Ϛ}_{\Psi}^{ir'_t}\tilde Q_3\tilde{Ϛ}_{\Psi}^{-ir'_t}$ equals $\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\tilde Q_3 \exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t)$, 12 random $(\tilde Q_3,r'_t)$ | max error $0$ |
| $\frac{d}{dr'_t}\sigma_{r'_{t}}(\tilde Q_3)|_{r'_t=0}=-i[\tilde H_{\Psi,\mathrm{modular}},\tilde Q_3]$ (central difference, $h=10^{-6}$) | max error $2.4\times10^{-13}$ |
| $\mathrm{Tr}(\exp(-\tilde H_{\Psi,\mathrm{modular}}))=\mathrm{Tr}(\tilde{Ϛ}_{\Psi})=1$ | $1.0$ to $10^{-39}$ |

The second state is the single-mode thermal state of the partition-function article, $\tilde H_\Psi=\omega\tilde\Pi_-$ with $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$, $\omega=0.9$, $\beta=1.2$. Its modular Hamiltonian is
$$
\tilde H_{\Psi,\mathrm{modular}}=\beta\tilde H_\Psi+(\log Z)e_t,
\qquad
Z=1+\exp(-\beta\omega)=1.339596,
\qquad
\log Z=0.292368,
$$
reproducing the parents' $Z$ and $K$; more generally, for a Gibbs state with $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ at inverse temperature $\beta$, the same identity $\tilde H_{\Psi,\mathrm{modular}}=\beta\tilde H_\Psi+(\log Z)e_t$ was checked on the independent data $h_t=0.7$, $\vec h_\Psi=(0.3,-0.5,0.8)$, $\beta=1.2$, where
$$
Z=2\exp(-\beta h_t)\cosh(\beta|\vec h_\Psi|)=1.547753
$$
and $\tilde H_{\Psi,\mathrm{modular}}-(\beta\tilde H_\Psi+(\log Z)e_t)$ vanishes to $4\times10^{-39}$.

**The failure when positivity is dropped.** If $\tilde{Ϛ}_{\Psi}$ is not positive definite — say $\tilde{Ϛ}_{\Psi}=\mathrm{diag}(1,0)$ — then $\Omega=e_t$ is not separating: there is a nonzero $\tilde Q_3$ with $\langle\tilde Q_3,\tilde Q_3\rangle_{\tilde{Ϛ}_{\Psi}}=\mathrm{Tr}(\tilde{Ϛ}_{\Psi}\tilde Q_3^{*}\tilde Q_3)=0$, hence $\tilde Q_3\Omega=0$, and the Tomita rule $\tilde Q_3\Omega\mapsto\tilde Q_3^{*}\Omega$ is not single-valued. Equivalently, $\Delta=S^*S$ has a kernel and is not invertible, so $-\log\Delta$ diverges along that direction and **no modular Hamiltonian exists**; the GNS inner product is degenerate and the closed form $\Delta(\tilde Q_3)=e^{-\tilde H_{\Psi,\mathrm{modular}}}\tilde Q_3\,e^{\tilde H_{\Psi,\mathrm{modular}}}$ is not even available. This is the same failure the modular-theory parent exhibits for the non-separating vector $\Omega=\vec e_x$, seen from the positivity side: the state assigns zero expectation to the nonzero positive element $E_{22}$, and the logarithm has nothing to say about it. The hypothesis carried by $\tilde H_{\Psi,\mathrm{modular}}$ is exactly the hypothesis carried by $\Delta$.

The verification was run on the state that was chosen for its genericity and on a second, thermal state; no displayed identity was checked only on the case that suggested it.

## The Trace Formula and the Gibbs Form

The plain form, read as the trace formula, inherited from the read list,
$$
\mathrm{Tr}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})=2\langle\tilde{H}_{\Psi,1},\tilde{H}_{\Psi,2}\rangle_{*} = 2\,\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*}),
\qquad
\mathrm{Tr}(e_t)=2,
$$
is what makes the statement "the state is thermal with respect to $\tilde H_{\Psi,\mathrm{modular}}$" computable, for two reasons.

First, since $\tilde H_{\Psi,\mathrm{modular}}\in\mathbb{B}_{\Psi}$, the exponential $\exp(-\tilde H_{\Psi,\mathrm{modular}})=\tilde{Ϛ}_{\Psi}$ also lies in $\mathbb{B}_{\Psi}$, and its trace is a doubled scalar part:
$$
\mathrm{Tr}(\exp(-\tilde H_{\Psi,\mathrm{modular}}))=2\,\mathrm{Sc}(\exp(-\tilde H_{\Psi,\mathrm{modular}}))=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi})=1 .
$$
The state is therefore the Gibbs state of $\tilde H_{\Psi,\mathrm{modular}}$ at unit temperature with **unit** partition function, and every expectation is a scalar extraction:
$$
\omega(\tilde Q_3)=\frac{\mathrm{Tr}(\exp(-\tilde H_{\Psi,\mathrm{modular}})\tilde Q_3)}{\mathrm{Tr}(\exp(-\tilde H_{\Psi,\mathrm{modular}}))}
=\frac{2\,\mathrm{Sc}(\exp(-\tilde H_{\Psi,\mathrm{modular}})\tilde Q_3)}{2\,\mathrm{Sc}(\exp(-\tilde H_{\Psi,\mathrm{modular}}))}
=2\,\mathrm{Sc}\big(\exp(-\tilde H_{\Psi,\mathrm{modular}})\tilde Q_3\big).
$$
No matrix diagonalization is needed to evaluate the state; the doubled scalar part of a biquaternion product is the whole computation.

Second, the physical Gibbs form follows by the shift $\tilde H_{\Psi,\mathrm{modular}}=\beta\tilde H_\Psi+(\log Z)e_t$. With $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$,
$$
Z=\mathrm{Tr}\big(\exp(-\beta H)\big)=2\,\mathrm{Sc}\big(\exp(-\beta H)\big)
=2\exp(-\beta h_t)\cosh(\beta|\vec h_\Psi|),
$$
and the scalar and vector parts of $\tilde H_{\Psi,\mathrm{modular}}$ have direct thermodynamic interpretations:
$$
\mathrm{Sc}(\tilde H_{\Psi,\mathrm{modular}})=\beta h_t+\log Z,
\qquad
\vec a=\beta\vec h_\Psi,
$$
the scalar part carrying the normalization $\log Z$, hence the free energy through $\log Z=-\beta F$, and the imaginary vector part being the thermal polarization of the state, $\vec a=\beta\vec h_\Psi$. The trace formula is the bridge: it converts the abstract Gibbs weight $\exp(-\tilde H_{\Psi,\mathrm{modular}})$ into a scalar Boltzmann factor times a boost-type biquaternion in $\mathbb{B}_{\Psi}$, which is the partition-function article's thermal operator. The nonlinearity of the biquaternion exponential is tamed because the imaginary vector part squares to a positive scalar, $(i\vec h_\Psi)^2=|\vec h_\Psi|^2e_t$, so $\vec h_\Psi$ and $e_t$ commute and the exponential splits.

One feature of the trace is worth separating from the modular Hamiltonian itself. The trace keeps only the scalar part of $\exp(-\beta H)$ and discards its imaginary vector part, the coherence, as the partition-function article records. The modular Hamiltonian does not discard it: both parts of $\tilde H_{\Psi,\mathrm{modular}}$ are needed, the scalar part for the normalization and the vector part $\vec a=\beta\vec h_\Psi$ to generate the flow, which conjugates the algebra and rotates the vector parts of its elements about the axis $a_{\mathrm{fop}}$ while leaving the state $\tilde{Ϛ}_{\Psi}$ itself invariant. The partition function is blind to the thermal polarization; the modular flow is what moves it.

## Is the Modular Hamiltonian Local?

### Locality Is Not Visible in the Finite-Dimensional Model

In $\mathbb{B}\cong M_2(\mathbb{C})$ every element is a finite matrix; there is no spacetime, no region, and no notion of an operator's support. Every faithful $\tilde{Ϛ}_{\Psi}$ gives some $\tilde H_{\Psi,\mathrm{modular}}\in\mathbb{B}_{\Psi}$, and no $\tilde H_{\Psi,\mathrm{modular}}$ is more or less local than any other. The question of locality therefore has no content in the algebra itself. It becomes meaningful only when the algebra is attached to spacetime regions, $V\mapsto\mathcal A(V)$, as in quantum field theory, and it is asked of the modular Hamiltonian $\tilde H_{\Psi,\mathrm{modular},V}$ of the vacuum state restricted to a region $V$.

### The Generic Answer: Nonlocal

For a general region $V$ of Minkowski space, the modular Hamiltonian of the vacuum is **not** a local operator. Two equivalent symptoms are standard. First, it is not expressible as a smeared local field over $V$,
$$
\tilde H_{\Psi,\mathrm{modular},V}\ \not\approx\ \int_V f(x)\,\mathcal O(x)\,d^3r ,
$$
for any local operator $\mathcal O$ and weight $f$; for a free field it contains bilocal terms, quadratic in the field at two separated points, and the obstruction to removing them is physical rather than technical. Second, and more invariantly, the modular flow $\sigma_{r'_{t}}$ of a general region does **not** map $\mathcal A(V)$ to itself: it is not a geometric flow of the region, and an operator localized in $V$ is, under the flow, spread outside it. This is the precise sense in which $\tilde H_{\Psi,\mathrm{modular},V}$ is nonlocal — not that it fails to be an operator, but that it is not tied to the local algebra of $V$ the way a Hamiltonian density is.

The nonlocality is also why the Tomita–Takesaki theory is not a tool for computing a local energy: $\tilde H_{\Psi,\mathrm{modular},V}$ is defined for every region and state, but its content is generally as complicated as the entanglement structure of the state across the boundary of $V$.

### The Exceptional Answer: The Cases Where $\tilde H_{\Psi,\mathrm{modular},V}$ Is Geometric

There are cases in which the modular flow **is** a spacetime symmetry flow and $\tilde H_{\Psi,\mathrm{modular},V}$ is therefore a local geometric generator. They are the exceptions, and they are known.

- **Half-spaces and wedges: the Bisognano–Wichmann theorem.** For the vacuum of a Wightman field theory and a wedge region (in particular a half-space), the modular operator is
$$
\Delta=\exp(-2\pi G),
$$
where $G$ is the generator of the boosts that preserve the wedge, normalized to the boost parameter. The modular flow is the boost flow, by rapidity $2\pi s$ in the modular parameter; equivalently $\tilde H_{\Psi,\mathrm{modular},V}=2\pi G$. This is the one case in which $\tilde H_{\Psi,\mathrm{modular},V}$ is independently known, and the biquaternion framework houses it, as the next subsection shows.
- **Balls and spheres: the conformal extension.** For a conformal field theory and a ball, the modular Hamiltonian is the generator of the conformal transformations that preserve the ball — a combination of the dilation and a special conformal transformation — and is again a local geometric operator. This is the Hislop–Longo theorem. The biquaternion framework does **not** house this case, because only the Lorentz generators $\vec e_\eta$, $B_{\mathrm{boost},\eta}=i\vec e_\eta$ and the (non-unit) dilation are elements of $\mathbb{B}$, while the special conformal generators are not elements of the algebra at all, as the conformal-group companion establishes. The ball case's $\tilde H_{\Psi,\mathrm{modular},V}$ has a part that the algebra cannot represent.
- **Intervals in two dimensions.** For the vacuum of a chiral or massless field on an interval, the modular Hamiltonian is again local, an integral of the stress tensor against a specific weight vanishing at the endpoints. This is a one-dimensional geometric case and is consistent with the conformal picture above.

So "$\tilde H_{\Psi,\mathrm{modular}}$ is local exactly when the modular flow is geometric" is the structural statement, and the geometric cases are the wedges and balls (and their lower-dimensional analogues). The modular Hamiltonian is a local operator only in those cases; everywhere else it is the nonlocal modular Hamiltonian of the region.

### The Wedge Case in Biquaternion Form

The wedge case is the one the framework can state completely, and it is also the one that the companion article *The Unruh Effect in Biquaternionic Form* already derives; the account here is confined to what the modular Hamiltonian itself is. In the right Rindler wedge the boost flow is generated by the Hermitian element
$$
G_1=i\,\vec e_x\in\mathbb{B}_{\Psi} ,
\qquad
G_1^2=e_t,
\qquad
G_1^\dagger=G_1 ,
$$
which is the generator $K_1=i\vec e_x$ of the Lorentz-group companion in the spatial direction $\vec e_x$. Its exponential is the boost rotor $\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})$, the unit-norm biquaternion that implements the Lorentz transformation:
$$
\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})=\exp\!\Big(\frac{\theta_{\mathrm{rpd}}}{2}G_1\Big)
=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\,\vec e_x\ \in\mathbb{B}_{\Psi},
\qquad
\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})\tilde U_{\Psi,\mathrm b}^{\natural}(\theta_{\mathrm{rpd}})=e_t,
$$
and its action on the material sector is the rotor conjugation $\tilde R_\Phi\mapsto\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})\tilde R_\Phi\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})$ (the rotor is Hermitian). Because Bisognano–Wichmann gives $\Delta=\exp(-2\pi G_1)$, the modular Hamiltonian of the wedge is
$$
\boxed{\;\tilde H_{\Psi,\mathrm{modular},W}=2\pi\,G_1=2\pi\,i\,\vec e_x\;},
$$
and the modular flow is the boost by rapidity $2\pi s$ in the modular parameter $s$. The two wedges have opposite orientation: the boost generator whose flow is future-directed on the right wedge is past-directed on the left, so $\tilde H_{\Psi,\mathrm{modular},L}=-\tilde H_{\Psi,\mathrm{modular},R}$ and "the wedge modular Hamiltonian" is wedge-dependent, as the Unruh article records; the norm $|\tilde H_{\Psi,\mathrm{modular},W}|$ is what enters the temperature and is the same for both.

Three checks make this concrete, and all were recomputed symbolically in the algebra. First, the rotor really is the boost: on $\tilde R_\Phi=i r'_t e_t+r_x\vec e_x$ (with $r'_t=r'_t$, and the other components untouched),
$$
r'_t\longmapsto r'_t\cosh\theta_{\mathrm{rpd}}-r_x\sinh\theta_{\mathrm{rpd}},
\qquad
r_x\longmapsto r_x\cosh\theta_{\mathrm{rpd}}-r'_t\sinh\theta_{\mathrm{rpd}},
\qquad
\langle\tilde U_{\Psi,\mathrm b}\tilde R_\Phi\tilde U_{\Psi,\mathrm b}\rangle_{\natural}=\langle\tilde R_\Phi\rangle_{\natural}.
$$
Second, the generator of this action is $G_1$ through the **anticommutator**,
$$
\frac{d}{d\theta_{\mathrm{rpd}}}\Big(\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})\tilde R_\Phi\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})\Big)\Big|_{\theta_{\mathrm{rpd}}=0}
=\tfrac12\{G_1,\tilde R_\Phi\}=\tfrac12\big(G_1\tilde R_\Phi+\tilde R_\Phi\,G_1\big),
$$
and exponentiating this derivation reproduces the finite rotor action, $\exp(\theta_{\mathrm{rpd}}\,\delta_{G_1})\tilde R_\Phi=\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})\tilde R_\Phi\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})$, with $\delta_{G_1}=\tfrac12\{G_1,\cdot\,\}$. Third, the **commutator** $[G_1,\tilde R_\Phi]$ is *not* the boost: on the boost plane $r_y=r_z=0$ it vanishes, and in general it generates a rotation in the orthogonal plane,
$$
[G_1,\tilde R_\Phi]=\big(0,\,0,\,-2i\,r_z,\,2i\,r_y\big)
\quad\text{for}\quad \tilde R_\Phi=i r'_t e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z .
$$
So the modular Hamiltonian's action here is two-sided, not an inner commutator: writing $\tilde H_{\Psi,\mathrm{modular},W}=2\pi G_1$ identifies the algebra element, and the flow it generates on $\mathbb{B}_{\Phi}$ is the rotor conjugation above. This is the same warning the curved-spacetime and Lorentz-transformation companions give for boosts, and the wedge is a case where it is load-bearing — a reader who generates the flow by $-i[\tilde H_{\Psi,\mathrm{modular},W},\cdot]$ obtains a rotation about $\vec e_x$, not the boost.

There is a structural reason the wedge case looks different from the finite-dimensional model, and it should be stated rather than smoothed over. The wedge algebra of a quantum field theory is a type III von Neumann algebra, and its modular flow is **outer**: no element of the algebra implements it as an inner automorphism, and no trace, hence no density matrix, exists. The finite-dimensional $\mathbb{B}$ is a type I$_2$ factor, semifinite, and its modular flow is inner, implemented by $\tilde{Ϛ}_{\Psi}^{ir'_t}\in\mathbb{B}$; that is why $\tilde H_{\Psi,\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}$ generates the flow by a commutator there. In the wedge case the modular Hamiltonian $2\pi G_1$ is a **geometric** generator — a local object, a boost — and not an inner element of the algebra, even though its biquaternion representative $G_1=i\vec e_x$ is an element of $\mathbb{B}$. The two statements "$\tilde H_{\Psi,\mathrm{modular}}\in\mathbb{B}_{\Psi}$" and "$\tilde H_{\Psi,\mathrm{modular}}$ generates the modular flow" therefore hold in both cases, but their mechanisms differ: inner commutator in the finite-dimensional model, geometric outer flow in the wedge. The parent's type gap — that $\mathbb{B}$ lies on the semifinite side and cannot host an outer modular flow — is exactly the gap that separates the two.

## What Is Established and What Is a Gap

**Established (theorem).**

- The Tomita–Takesaki construction of $\Delta$ and the modular group, and the equivalence of cyclic and separating with faithful (modular-theory parent).
- The Takesaki–Winnink theorem: a faithful normal state is a KMS state for its modular flow, normalized to $\beta=1$; the rescaled width is $\beta$ (KMS parent).
- The spectral theorem, which makes $-\log\Delta$ a self-adjoint operator for every strictly positive self-adjoint $\Delta$.
- Bisognano–Wichmann, for wedges and half-spaces, and the conformal (Hislop–Longo) extension to balls; both imported, not derived.

**Established (recomputed here).**

- $\tilde H_{\Psi,\mathrm{modular}}=-\log\Delta$ is defined by $\Delta=\exp(-\tilde H_{\Psi,\mathrm{modular}})$; with this convention $\Delta^{ir'_t}=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)$ and $d\sigma_{r'_{t}}/dr'_t|_{r'_t=0}=-i[\tilde H_{\Psi,\mathrm{modular}},\tilde Q_3]$, and the opposite sign convention reverses which flow is KMS.
- In $\mathbb{B}\cong M_2(\mathbb{C})$, $\tilde H_{\Psi,\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi}$, with the spectral form $a_0=-\tfrac12\log\det\tilde{Ϛ}_{\Psi}$, $\vec a=-\tfrac12\log(\lambda_+/\lambda_-)\vec u_r$; $\Delta>0$ for every faithful state, and $\tilde H_{\Psi,\mathrm{modular}}$ does not exist for a non-faithful one.
- $\tilde H_{\Psi,\mathrm{modular}}$ generates the same flow as $\Delta^{ir'_t}$: verified symbolically and numerically on a generic rotated state and a thermal state.
- $\mathrm{Tr}(\exp(-\tilde H_{\Psi,\mathrm{modular}}))=1$, and the trace formula makes the Gibbs state a doubled scalar extraction, with $\mathrm{Sc}(\tilde H_{\Psi,\mathrm{modular}})=\beta h_t+\log Z$ and $\vec a=\beta\vec h_\Psi$.
- $\tilde H_{\Psi,\mathrm{modular}}=-2\log\tilde Q_{\mathrm n}$ for the bracket-normalised amplitude $\tilde Q_{\mathrm n}=\tilde{Ϛ}_{\Psi}^{1/2}$, with a central additive constant for an unnormalised amplitude; checked on a generic rotated state.
- In the wedge, $\tilde H_{\Psi,\mathrm{modular},W}=2\pi G_1$ with $G_1=i\vec e_x\in\mathbb{B}_{\Psi}$; the rotor action is the boost, its generator is the anticommutator $\tfrac12\{G_1,\cdot\,\}$, and the commutator is a rotation in the orthogonal plane.

**Interpretation.**

- Reading $\tilde H_{\Psi,\mathrm{modular}}\in\mathbb{B}_{\Psi}$ as the informational-sector object whose unit-temperature Gibbs state is the given state, and the modular flow as Hamiltonian evolution under it.
- Reading the modular Hamiltonian as minus twice the logarithm of the Cartan amplitude, hence the state as the square of its amplitude.
- Reading the nonlocality of $\tilde H_{\Psi,\mathrm{modular},V}$ as the statement that the modular flow is not geometric outside the Bisognano–Wichmann and conformal cases.

**Gap.**

- The framework admits a modular Hamiltonian for every faithful state of $\mathbb{B}$ but does not select a state, so it does not select a $\tilde H_{\Psi,\mathrm{modular}}$; the tracial state gives the central $\tilde H_{\Psi,\mathrm{modular}}=(\log 2)e_t$.
- Locality of $\tilde H_{\Psi,\mathrm{modular}}$ is not testable inside $\mathbb{B}$; the finite-dimensional model has no regions. The nonlocal generic case and the conformal ball case are standard field-theoretic results that the framework imports or cannot express.
- The ball case cannot be housed: the special conformal generators are not elements of $\mathbb{B}$, so the wedge is the only geometric modular Hamiltonian the algebra realizes completely.
- The wedge flow is outer and lives on a type III algebra that is not $\mathbb{B}$; the framework's finite-dimensional algebra cannot host it, and the type III extension remains open as in the parents.
- No empirical consequence is derived.

## Summary

The modular Hamiltonian is the operator that generates the modular flow. Writing $\Delta=\exp(-\tilde H_{\Psi,\mathrm{modular}})$, equivalently $\tilde H_{\Psi,\mathrm{modular}}=-\log\Delta$, the flow is Hamiltonian evolution,
$$
\sigma_{r'_{t}}(\tilde Q_3)=\Delta^{ir'_t}\tilde Q_3\Delta^{-ir'_t}=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\tilde Q_3\,\exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t),
\qquad
\frac{d}{dr'_t}\sigma_{r'_{t}}(\tilde Q_3)\Big|_{r'_t=0}=-i[\tilde H_{\Psi,\mathrm{modular}},\tilde Q_3],
$$
and the KMS state is the thermal state of $\tilde H_{\Psi,\mathrm{modular}}$ at unit temperature. The definition inherits the whole hypothesis of the Tomita–Takesaki construction — $\Omega$ cyclic and separating, equivalently the state faithful — and strict positivity of $\Delta$ is that same hypothesis read off the spectrum: $\Delta=S^*S\ge0$ is automatic, but $-\log\Delta$ exists only when $\Delta>0$, and a non-faithful state leaves an eigenvalue $0$ at which the logarithm diverges. The sign in $\Delta=\exp(-\tilde H_{\Psi,\mathrm{modular}})$ is a convention that reverses which flow is KMS; it is fixed here as in the parents and held.

In the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ the parents' finite-dimensional model gives $\tilde{Ϛ}_{\Psi}=\exp(-\tilde H_{\Psi,\mathrm{modular}})$ and
$$
\tilde H_{\Psi,\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi},
\qquad
\tilde H_{\Psi,\mathrm{modular}}=a_0e_t+i\vec a\cdot\mathbf e,
\qquad
a_0=-\tfrac12\log\det\tilde{Ϛ}_{\Psi},
\qquad
\vec a=-\tfrac12\log\frac{\lambda_+}{\lambda_-}\vec u_r,
$$
so the modular Hamiltonian is a Hermitian element of the informational sector, with the scalar part fixed by the determinant of the state and the vector part by its Bloch polarization. It was verified symbolically and numerically — on a generic rotated state and on a thermal state, not only on the case that suggested the formulas — that $\tilde H_{\Psi,\mathrm{modular}}$ generates the same flow as $\Delta^{ir'_t}$, that $\mathrm{Tr}(\exp(-\tilde H_{\Psi,\mathrm{modular}}))=1$, and that the trace formula $\mathrm{Tr}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})=2\langle\tilde{H}_{\Psi,1},\tilde{H}_{\Psi,2}\rangle_{*} = 2\,\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})$ makes the Gibbs form computable, with $\mathrm{Sc}(\tilde H_{\Psi,\mathrm{modular}})=\beta h_t+\log Z$ and $\vec a=\beta\vec h_\Psi$.

The one structural question the finite-dimensional model cannot settle is locality. For a general spacetime region the modular Hamiltonian of the vacuum is nonlocal, and the modular flow is not geometric; it is local exactly in the exceptional cases where the flow is a symmetry flow — the Bisognano–Wichmann wedge, where $\tilde H_{\Psi,\mathrm{modular},W}=2\pi G_1$ with $G_1=i\vec e_x\in\mathbb{B}_{\Psi}$ and the flow is the boost by rapidity $2\pi s$, and the conformal ball, which the framework cannot fully express because the special conformal generators are not elements of $\mathbb{B}$. In the wedge the flow is outer and the action is the two-sided rotor conjugation, not the commutator $[\tilde H_{\Psi,\mathrm{modular},W},\cdot\,]$; in the finite-dimensional model the flow is inner and the commutator is correct. Both cases have $\tilde H_{\Psi,\mathrm{modular}}\in\mathbb{B}_{\Psi}$, by different mechanisms, and the gap between them is the type gap of the modular-theory parent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Psi},\mathbb{B}_{\Phi}$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| ${}^{*}$ | Hermitian conjugation; the Tomita involution $A^*$ |
| $\mathrm{Tr}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})=2\langle\tilde{H}_{\Psi,1},\tilde{H}_{\Psi,2}\rangle_{*} = 2\,\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2}^{*})$ | Trace reading of the plain form; $\mathrm{Tr}(e_t)=2$ |
| $S=J\Delta^{1/2}$ | Tomita operator and its polar decomposition |
| $\Delta=S^*S\ge0$ | Modular operator; $\Delta>0$ iff the state is faithful |
| $\tilde H_{\Psi,\mathrm{modular}}=-\log\Delta$ | Modular Hamiltonian; $\Delta=\exp(-\tilde H_{\Psi,\mathrm{modular}})$ |
| $\sigma_{r'_{t}}(\tilde Q_3)=\Delta^{ir'_t}\tilde Q_3\Delta^{-ir'_t}=\exp(-i\tilde H_{\Psi,\mathrm{modular}}r'_t)\tilde Q_3 \exp(i\tilde H_{\Psi,\mathrm{modular}}r'_t)$ | Modular flow |
| $d\sigma_{r'_{t}}/dr'_t|_{r'_t=0}=-i[\tilde H_{\Psi,\mathrm{modular}},\tilde Q_3]$ | Generator identity (sign convention fixed here) |
| $\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi}$ | Faithful state, positive definite, trace one |
| $\tilde Q_{\mathrm n}=\tilde{Ϛ}_{\Psi}^{1/2}$ | Bracket-normalised Cartan amplitude of the state, $\langle\tilde Q_{\mathrm n},\tilde Q_{\mathrm n}\rangle_*=\tfrac12$ |
| $\tilde H_{\Psi,\mathrm{modular}}=-2\log\tilde Q_{\mathrm n}$ | Modular Hamiltonian from the amplitude; $\tilde H_{\Psi,\mathrm{modular}}=-2\log\tilde Q_H+\log(2\langle\tilde Q_H,\tilde Q_H\rangle_*)e_t$ for an unnormalised $\tilde Q_H$ |
| $\tilde H_{\Psi,\mathrm{modular}}=-\log\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi}$ | Modular Hamiltonian in the finite-dimensional model |
| $\lambda_\pm=\tfrac12(1\pm|\vec r|)$ | Eigenvalues of $\tilde{Ϛ}_{\Psi}$ |
| $a_0=-\tfrac12\log\det\tilde{Ϛ}_{\Psi}$ | Scalar part of $\tilde H_{\Psi,\mathrm{modular}}$ |
| $\vec a=-\tfrac12\log(\lambda_+/\lambda_-)\vec u_r$ | Vector part of $\tilde H_{\Psi,\mathrm{modular}}$ |
| $\tilde H_{\Psi,\mathrm{modular}}=\beta\tilde H_\Psi+(\log Z)e_t$ | Gibbs-state modular Hamiltonian |
| $G_1=i\vec e_x\in\mathbb{B}_{\Psi}$ | Boost generator ($=K_1$ in the Lorentz-group companion) |
| $\tilde U_{\Psi,\mathrm b}(\theta_{\mathrm{rpd}})=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec e_x$ | Boost rotor (Hermitian, unit norm) |
| $\tilde H_{\Psi,\mathrm{modular},W}=2\pi G_1$ | Wedge modular Hamiltonian (Bisognano–Wichmann) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- Companion article [The Hermitian Tomita–Takesaki Theory under the Biquaternion Framework](the-hermitian-tomita-takesaki-theory-under-the-biquaternion-framework.html), for the construction of $S$, $\Delta$ and $J$, the modular flow, and the type classification.
- Companion article [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html), for the KMS boundary relation, the imaginary-time strip, and the thermal interpretation of $\tilde H_{\Psi,\mathrm{modular}}$.
- Companion article [The Partition Function in Biquaternionic Form](the-partition-function-in-biquaternionic-form.html), for the Gibbs state, the thermal operator, and $\tilde H_{\Psi,\mathrm{modular}}=\beta\tilde H_\Psi+(\log Z)e_t$.
- Companion article [The Unruh Effect in Biquaternionic Form](the-unruh-effect-in-biquaternionic-form.html), for the wedge, the Bisognano–Wichmann identification, and the temperature derived from the two-point function.
- Companion article [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the Hermitian subspace, the trace formula, and states as elements of $\mathbb{B}_{\Psi}$.
- Companion article [The General Polar Decomposition, the Amplitude and the Operator-to-State Map](the-general-polar-decomposition-the-amplitude-and-the-operator-to-state-map.html), for the amplitude as the square root of the state and the modular reading.
- Companion article [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the material sector, the four-vectors, and the zero-divisor cone.
- Companion article [The Conformal Group in Biquaternionic Form](the-conformal-group-in-biquaternionic-form.html), for the boundary that the special conformal generators are not elements of $\mathbb{B}$.
- Companion article [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html), for the boost generators $B_{\mathrm{boost},\eta}=i\vec e_\eta$ whose $k=1$ case is the wedge modular Hamiltonian.
- Companion article [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html), for the boost rotor and the subspaces its generators lie in.
- Companion article [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the two-sided rotor action that the boost requires.
- Companion article [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html), for the single fermionic mode and the parity $(-1)^F$.
- Companion article [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html), for the algebra and its two sectors.
