# __Belinfante–Rosenfeld: Why the Canonical Stress Tensor Is Not Symmetric__

## Introduction

**The claim.** The energy–momentum tensor that translation invariance gives is not symmetric, and its antisymmetric part is not an error: it is the divergence of the spin current. Symmetrising it — Belinfante's and Rosenfeld's improvement of 1939–40 — moves the spin out of the stress and into the angular-momentum current, and the object that results is the one a fluid reads as its stress and gravity reads as its source. **The improvement is therefore not a tidying step; it is a decision about where the spin is carried.**

**What is established.** Four things. First, the antisymmetric part of the canonical tensor equals the divergence of the spin density, so the asymmetry is exactly the spin. Second, the improvement is a superpotential, and its conservation is one line: a double divergence of an object antisymmetric in two indices vanishes. Third, symmetry is a requirement from three independent readers — gravity, the fluid, and the algebra's component count — and the three agree. Fourth, a superpotential freedom survives every requirement, so **the stress at a point is not fixed by the field alone**, and a constitutive statement is what fixes it.

**What is not new.** The improvement is in every field-theory text, and the corpus already names it: [the Noether article](noethers-theorem-in-biquaternionic-form.html) states that the canonical tensor has sixteen independent entries and that *it is the Belinfante-improved tensor that is symmetric*. **What the corpus did not have is the article that derives it**, says why the fluid reading needs it, and states what the residual freedom means for a stress defined at a point. This article is that page, and the Noether article's sentence is its conclusion.

**Why it sits here.** It comes after the stress–energy article of this section, which writes the canonical tensor and its conservation law, and before the fluid block, which uses a stress. **The improvement is the one step between the two**, and a reader who takes the canonical tensor into the fluid will find an asymmetric stress and no pressure.

## What the Canonical Tensor Is, and What Fails

**One symmetry, one current.** Translation invariance gives the canonical tensor by the Noether construction, and for the corpus's scalar field it is

$$
T_{\imath\jmath}=\frac{\partial\xi^{*}}{\partial x_{\imath}}\frac{\partial\xi}{\partial x_{\jmath}}+\frac{\partial\xi}{\partial x_{\imath}}\frac{\partial\xi^{*}}{\partial x_{\jmath}}+\varepsilon_{\imath}\delta_{\imath\jmath}\,\mathcal L ,
$$

with $x_{\imath}=(r'_t,r_x,r_y,r_z)$ the real coordinates and both indices low. **This one is symmetric**, because the two derivative terms are symmetric under $\imath\leftrightarrow\jmath$ and the last is diagonal. A scalar field has no spin, and the canonical tensor of a spinless field needs no improvement: **the improvement's work starts where the spin does.**

**What a spin term does to the same display.** Let the field carry an index and let the density carry a first derivative of it — a Dirac spinor, a Proca vector, or a connection. The derivative terms now come with a matrix between them, and the matrix need not be symmetric in its pair of derivative slots. **The result is the corpus's count: sixteen independent entries before the improvement**, not ten.

**Why the asymmetry is not a defect.** The angular-momentum current of Lorentz invariance is

$$
L_{\imath\jmath\rho}=x_{\jmath}T_{\imath\rho}-x_{\rho}T_{\imath\jmath}+S_{\imath\jmath\rho},
$$

with $S$ the spin density, antisymmetric in its last two indices. Its conservation, the vanishing of $\sum_\imath\partial_\imath L_{\imath\jmath\rho}$, is one line of differentiation:

$$
\sum_\imath\partial_\imath L_{\imath\jmath\rho}
=\underbrace{T_{\jmath\rho}-T_{\rho\jmath}}_{\text{the }x\text{-derivatives}}
+\underbrace{\sum_\imath\bigl(x_{\jmath}\partial_\imath T_{\imath\rho}-x_{\rho}\partial_\imath T_{\imath\jmath}\bigr)}_{\,=0\text{ on shell}}
+\sum_\imath\partial_\imath S_{\imath\jmath\rho},
$$

so, using $\sum_\imath\partial_\imath T_{\imath\jmath}=0$,

$$
\boxed{\;T_{\jmath\rho}-T_{\rho\jmath}=-\sum_\imath\partial_\imath S_{\imath\jmath\rho}\;}
$$

**The antisymmetric part of the canonical tensor is minus the divergence of the spin density.** The two facts are one fact: the total angular momentum is conserved, the orbital part alone is not, and the difference is carried by the spin's divergence. **A theory whose canonical tensor is symmetric is a theory whose spin current has vanishing divergence — that is, a theory with no spin.**

**The physical reading, in one sentence.** The orbital angular momentum $x\wedge T$ is conserved only if $T$ is symmetric; when it is not, the shortfall is exactly the torque the spin density exerts as it flows. **The asymmetry is a torque density, and that is why the fluid block will care.**

## The Improvement

**One superpotential, and the two properties it must have.** Add to the canonical tensor the divergence of a three-index object $X$,

$$
T^{(\mathrm B)}_{\imath\jmath}:=T_{\imath\jmath}+\sum_\rho\partial_\rho X_{\imath\rho\jmath},
\qquad X_{\imath\rho\jmath}=-X_{\rho\imath\jmath},
$$

with $X$ built linearly from the spin density. **Two properties follow from the antisymmetry alone.**

- *Conservation is preserved.* The added term's divergence is $\sum_{\imath,\rho}\partial_\imath\partial_\rho X_{\imath\rho\jmath}$, a double divergence of an object antisymmetric in $(\imath,\rho)$; the two derivatives are symmetric and the contraction vanishes identically.
- *The total four-momentum is preserved.* The added term is a total divergence, so its integral over a surface at infinity of a localised field vanishes.

**Symmetry fixes the coefficient.** Requiring $T^{(\mathrm B)}_{\imath\jmath}=T^{(\mathrm B)}_{\jmath\imath}$, and using the identity above for the antisymmetric part of $T$, gives one algebraic equation for $X$ in terms of $S$; the solution is the Belinfante–Rosenfeld expression, and its coefficient is $\tfrac12$ with index symmetrisations. **The improvement is uniquely determined by its two demands** — that it be built from the spin and that it symmetrise — once one forbids terms with more derivatives.

**What happened to the spin, stated as a choice.** After the improvement the antisymmetric part of the stress is zero, so the identity above reads $\sum_\imath\partial_\imath S_{\imath\jmath\rho}=0$: **the spin current is now conserved by itself.** Before the improvement the spin could exchange with the orbital angular momentum; after it, the exchange has been absorbed into a redefinition of the stress. **The physics has not changed — the total current is the same — but the bookkeeping has: the stress now carries what the spin used to carry.**

**Why that is the right bookkeeping and not merely a convenient one.** The choice is forced by three readers, and their agreement is the article's central table.

| reader | what it requires | why the canonical tensor fails it |
| --- | --- | --- |
| gravity | the source of the Einstein equation is symmetric, because the Einstein tensor is | an asymmetric source would make the field equations inconsistent: the antisymmetric part of $T$ has nowhere to go |
| the fluid | the stress across a surface is symmetric, and its isotropic part is the pressure | an antisymmetric stress is a couple stress, felt as a torque on a volume element and not as a pressure |
| the algebra | a symmetric rank-two tensor has ten components; the biquaternion carries eight | only the time row — four components, one biquaternion in $\mathbb{B}_{\Psi}$ — can be displayed, and that row is well defined only for the symmetric tensor |

**The third reader is the corpus's own reason for packaging as it does.** $\tilde\Sigma_{\Psi}=\mathcal H e_t+\frac{i}{c}\vec S$ is the time row of the symmetric tensor: $T_{00}=\mathcal H$ and $T_{0\imath}=S_{\imath}/c$. **The reason a single biquaternion suffices for the field's energy is that the row has four independent entries, and the reason the row is the right object is that the tensor is symmetric.** [The Noether article's](noethers-theorem-in-biquaternionic-form.html) table of sixteen, ten, eight and four is this paragraph in numbers.

## The Ambiguity That Survives

**Symmetry and conservation do not fix the stress.** Any further superpotential with the right antisymmetries can be added,

$$
T_{\imath\jmath}\longmapsto T_{\imath\jmath}+\sum_\rho\partial_\rho\bigl(X_{\imath\rho\jmath}+\sum_\sigma\partial_\sigma Y_{\imath\rho\sigma\jmath}\bigr),
$$

and the total momentum, the conservation law and the symmetry are all preserved. **The stress at a point is therefore not an observable of the field alone.** Only its divergence, and its integral, are.

**The standard illustration is the conformal improvement.** For a scalar field the symmetric tensor is still not unique: the term

$$
\frac{1}{6}\bigl(\partial_\imath\partial_\jmath-\varepsilon_{\imath}\delta_{\imath\jmath}\Box_\Phi\bigr)\bigl(\xi^{*}\xi\bigr)
$$

is a superpotential, it is symmetric, and adding it makes the trace of the stress vanish for a massless field — which is what a conformal theory requires and what the canonical tensor does not deliver. **So even the symmetric tensor has a physically meaningful ambiguity**, and the choice among its members is fixed by the symmetry one wants the stress to manifest, not by the field equations.

**What this means for a stress defined at a point, and it is the honest statement the corpus needs.** A fluid's stress is defined operationally: it is what a surface element transmits. **In field theory that operational definition is available only after a superpotential is fixed**, because a superpotential changes the local flux while leaving the total momentum alone. The corpus's positions are therefore:

- the total four-momentum of a localised field is unambiguous;
- the local energy density and flux are ambiguous up to a superpotential;
- **the fluid's pressure at a point is unambiguous only relative to a constitutive statement**, which is to say only after the improvement and the state have both been fixed.

**This is not a defect of the corpus; it is the reason the fluid block has a constitutive section.** A stress that were fixed by the field alone would need no equation of state; the fact that it is not is part of why one is needed.

## The Fluid's Stress Is the Improved One

**What a surface element feels.** Consider a small surface with normal $\vec n$ inside the fluid. The force it transmits per unit area is $\sum_\jmath T_{\imath\jmath}n_{\jmath}$. **The symmetric part is a pressure and a shear; the antisymmetric part is a torque per unit area**, which an ordinary fluid does not transmit. So an ordinary fluid's stress is symmetric, and the canonical tensor of a spinning field is not the ordinary fluid's stress.

**A fluid that does transmit the torque has a name in this corpus.** [Spin Fluid Physics](spin-fluid-physics-in-biquaternionic-form.html) and [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html) treat a fluid with a spin density and a couple stress, and the canonical tensor is *its* stress rather than the ordinary fluid's. **The two fluid classes are distinguished by whether the antisymmetric part of the stress is kept**, which is exactly the distinction between the canonical and the improved tensor.

**The Frenkel condition, read against the superpotential.** A spin fluid must state how its spin is distributed between the orbital and the intrinsic parts — the spin supplementary condition — and Frenkel's, $\sum_\rho S_{\imath\jmath\rho}u_{\rho}=0$, is the corpus's choice. **It plays the role the superpotential choice plays in the field:** both remove a redundancy in where the angular momentum is booked, and neither changes the total. A reader who has understood the improvement will recognise the supplementary condition as the fluid's version of it.

**What the Korteweg stress is not.** The gradient corrections of the quantum fluid — the Korteweg stress, the quantum potential's pressure — are **not** superpotential ambiguities. They are physical terms: they come from a gradient energy in the density and they change the total energy, not merely its distribution. **Telling the two apart is the practical use of this article**: a term that changes the energy is constitutive; a term that does not is a choice of bookkeeping.

## What It Does Not Give

**It does not give a unique local stress.** Stated above and repeated because it is the most likely over-reading: the improvement fixes the stress up to a superpotential, and physics fixes the rest only through a constitutive statement.

**It does not derive the equation of state.** The improved tensor supplies the flux; the relation between pressure and density is a separate functional, and [the equation of state](the-equation-of-state-in-biquaternion-form.html) is where it lives.

**It does not settle the primordial rung in closed form.** The spin density of a general biquaternion field is one of the Noether article's open questions: whether it can be written as a single algebra-valued object, and how it relates to the bivector representation of angular momentum. **At the matrix rung the improved tensor exists and its construction is the same superpotential**, but its expression in the corpus's letters is not written, and this article does not write it.

**It does not change any conservation law.** Every current is the same before and after; only the distribution of the spin between the stress and the angular momentum moves. **A reader looking for new physics here will not find it** — the article's content is that a choice the corpus had made tacitly is forced and is not unique.

## Summary

The canonical energy–momentum tensor of a field with spin is not symmetric, and the antisymmetric part is exactly minus the divergence of the spin density: $T_{\jmath\rho}-T_{\rho\jmath}=-\sum_\imath\partial_\imath S_{\imath\jmath\rho}$. The asymmetry is a torque density and not an error.

Belinfante's and Rosenfeld's improvement adds the divergence of a superpotential built from the spin, antisymmetric in two indices, so conservation and the total four-momentum are preserved while the tensor is symmetrised. **After it the spin current is conserved separately, and the stress carries what the spin carried.** Three readers demand the symmetric object and agree: gravity, whose source must be symmetric; the fluid, whose surface transmitted no torque; and the algebra, whose biquaternion can carry exactly the four-component time row of a symmetric tensor.

A superpotential freedom survives, so the stress at a point is not fixed by the field alone, and even the symmetric tensor has a physically meaningful ambiguity — the conformal improvement's trace term. **The fluid's pressure is therefore unambiguous only relative to a constitutive statement**, which is why the fluid block has one.

A fluid that keeps the antisymmetric part is a spin fluid with a couple stress, and its stress is the canonical one. The Frenkel condition plays the role for it that the superpotential choice plays for the field. The Korteweg and quantum stresses are not of this kind: they change the energy, and so they are constitutive and not bookkeeping.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $T_{\imath\jmath}$ | The canonical energy–momentum tensor of translations, sixteen independent entries for a field with spin |
| $T^{(\mathrm B)}_{\imath\jmath}$ | The Belinfante–Rosenfeld improved tensor, symmetric, ten independent entries |
| $S_{\imath\jmath\rho}$ | The spin density, the spin part of the angular-momentum current, antisymmetric in the last two indices |
| $L_{\imath\jmath\rho}=x_{\jmath}T_{\imath\rho}-x_{\rho}T_{\imath\jmath}+S_{\imath\jmath\rho}$ | The angular-momentum current of Lorentz invariance |
| $\sum_\imath\partial_\imath S_{\imath\jmath\rho}=T_{\jmath\rho}-T_{\rho\jmath}$ | The identity that makes the asymmetry the spin's divergence |
| $X_{\imath\rho\jmath}=-X_{\rho\imath\jmath}$ | The superpotential of the improvement, antisymmetric in its first two indices |
| $\tfrac16(\partial_\imath\partial_\jmath-\varepsilon_{\imath}\delta_{\imath\jmath}\Box_\Phi)(\xi^{*}\xi)$ | The conformal improvement of the scalar stress, a symmetric superpotential |
| $\tilde\Sigma_{\Psi}=\mathcal H e_t+\frac{i}{c}\vec S$ | The time row of the symmetric tensor, the four components a biquaternion can carry |
| $\sum_\rho S_{\imath\jmath\rho}u_{\rho}=0$ | The Frenkel spin supplementary condition, the fluid's version of the superpotential choice |
| $\sum_\jmath T_{\imath\jmath}n_{\jmath}$ | The force per unit area across a surface with normal $n$; symmetric for an ordinary fluid |

## Further Reading

- F. J. Belinfante, "On the spin angular momentum of mesons," *Physica* 6 (1939), 887–898, and "On the current and the density of the electric charge, the energy, the linear momentum and the angular momentum of arbitrary fields," *Physica* 7 (1940), 449–474, the improvement's original papers.
- Leon Rosenfeld, "Sur le tenseur d'impulsion-énergie," *Mémoires de l'Académie Royale des Sciences de Belgique* 18 (1940), the independent statement.
- Steven Weinberg, *The Quantum Theory of Fields*, vol. I (Cambridge University Press, 1995), §5.4, for the canonical tensor, the spin current and the improvement in the modern notation.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (4th ed., Pergamon, 1975), §32–33, for the symmetric tensor of the electromagnetic field and the superpotential ambiguity.
- Curtis G. Callan, Sidney Coleman and Roman Jackiw, "A new improved energy-momentum tensor," *Annals of Physics* 59 (1970), 42–73, for the conformal improvement and why even the symmetric tensor is not unique.
- Friedrich W. Hehl, "On the energy tensor of spinning massive matter in classical field theory and general relativity," *Reports on Mathematical Physics* 9 (1976), 55–82, for the spin fluid's stress and the couple stress.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), for the canonical tensor, the angular-momentum bivector and the component count this article expands.
- [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), for the density and flux that the symmetric tensor's time row packages.
- [Spin Fluid Physics in Biquaternionic Form](spin-fluid-physics-in-biquaternionic-form.html) and [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html), for the fluid class that keeps the antisymmetric part.
- [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html), for the constitutive statement that fixes the pressure the improvement leaves free.
