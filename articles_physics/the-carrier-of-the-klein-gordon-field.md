# __The Carrier of the Klein–Gordon Field__

## Introduction

The Klein–Gordon equation is a central operator acting on a biquaternion-valued field, and that is exactly why it cannot say where the field lives. The operator multiplies the four coefficients of the field by the same scalar, so it treats all four alike and preserves every real subspace of the algebra. The equation is therefore satisfied by a field with four independent complex coefficients, and by a field with one. Nothing in the equation prefers either.

The **spin** prefers one. A spin-zero field is a single complex number at each event, and the carrier that holds one complex number is the centre of the algebra. The claim of this article is that the carrier of the Klein–Gordon field is the centre $\mathbb{B}_C$, that the restriction costs nothing in the equation, and that it changes what the field is.

The argument runs in four steps. The centrality of the operator is shown to make the restriction free. The centre is shown to be the carrier that spin zero requires. The two sectors are shown to meet the centre in one real line each, so that "the Klein–Gordon field is material" is a choice of phase and not a statement of physics. And the charge is shown to survive the restriction, which is the property that separates this carrier from the carrier of the vector field.

## The Operator Does Not Choose

The equation of the companion article is

$$
\left(\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}-k_m^{2}\right)\tilde\Xi=0,
\qquad
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r^{\prime}_t}^{2},
$$

and $\Box_\Phi$ is a **central scalar with real coefficients**. The centrality is not a convenience, and it is a cancellation. In the product $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ the four diagonal terms return $+e_t$, and the six mixed terms arrive in pairs that cancel: for two spatial directions the two orderings contribute $-\vec e_\mu\vec e_\nu$ and $-\vec e_\nu\vec e_\mu=+\vec e_\mu\vec e_\nu$, and for one temporal and one spatial direction they contribute $-\vec e_\nu$ and $+\vec e_\nu$. Nothing carries a direction, so on a plane wave the operator is the quaternionic norm of the wave element, $\langle\tilde K_\Phi\rangle_\natural=-(k'_t)^{2}+\lvert\vec k_\Phi\rvert^{2}$, a real number and not an element.

Since the operator is central, it commutes with left multiplication by every element, and it acts coefficient by coefficient:

$$
\Box_\Phi\tilde\Xi=\sum_{\mu\in\{t,x,y,z\}}(\Box_\Phi\Xi_\mu)\,e_\mu .
$$

So every subspace of $\mathbb{B}$ that is closed under multiplication by real scalars is invariant under $\Box_\Phi$, and the field equation on $\mathbb{B}$ is four decoupled copies of the one scalar equation. **The equation has no preference, and a general biquaternion field is four scalar fields, not one.**

## The Carrier Is the Centre

The centre of the algebra is the set of elements that commute with everything,

$$
\mathbb{B}_C=\{q\,e_t\ :\ q\in\mathbb{C}\},
$$

of complex dimension one and real dimension two. It is the smallest subspace of $\mathbb{B}$ that contains the unit, and it is a module over the algebra in the weakest sense: it is preserved by multiplication by its own elements.

**The claim.** A spin-zero field is one complex number at each event, and the algebra's copy of one complex number is $\mathbb{B}_C$. The carrier is fixed by the dimension of the field's value, not by the equation.

**The warrant.** The value of a spin-zero field has one complex component, so its carrier has complex dimension one. Inside $\mathbb{B}$, the subspaces of complex dimension one are the complex lines, and the one distinguished by the algebra itself is the set of elements fixed by the whole algebra under commutation — the centre. Any other complex line is a rotated copy, and a rotation of the carrier is a change of basis rather than a statement about the field.

## The Restriction Is Free

Take $\tilde\Xi=\xi e_t$ with $\xi$ a complex scalar function. Then

$$
\Box_\Phi(\xi e_t)=(\Box_\Phi\xi)\,e_t\in\mathbb{B}_C,
$$

because $\Box_\Phi$ is central and real. The centre is invariant, and the restricted equation is the ordinary complex Klein–Gordon equation. Closure is not an extra condition; it follows from the centrality in one line.

**What is lost, and what is not.** The general field has four complex coefficients and the restricted field has one, so three complex coefficients are discarded. Those three are not spin-zero content: they are three further independent scalar fields, each of which would solve the same equation. A biquaternion-valued Klein–Gordon field is four scalars sharing one mass, and the restriction to the centre is the statement that there is one.

## The Two Sectors Meet the Centre in a Line Each

The centre and the sector decomposition meet in a definite way:

$$
\mathbb{B}_C\cap\mathbb{B}_{\Psi}=\mathbb{R}\,e_t,
\qquad
\mathbb{B}_C\cap\mathbb{B}_{\Phi}=i\,\mathbb{R}\,e_t .
$$

A **real** scalar is Hermitian, hence informational; an **imaginary** scalar is anti-Hermitian, hence material. Multiplication by the central $i$ carries the line $\mathbb{R}e_t$ onto the line $i\,\mathbb{R}e_t$, and it carries the whole centre onto itself.

**This is the answer to a natural question.** One may ask whether the Klein–Gordon field lives in the material sector, on the ground that the gradient does. The answer is that the question has no invariant content here: the material and informational copies of a scalar field are the same field with the label of $i$ moved, since $i$ is central and $\mathbb{B}_\Phi=i\mathbb{B}_\Psi$. The carrier of spin zero is the centre, and the centre is split by the sectors into two real lines that $i$ exchanges. A declaration that the scalar field is material is a declaration that its value is imaginary, and complex conjugation — which is what makes a charge — then acts as a reflection on that line.

## The Charge Survives, and That Is the Difference

A central phase $\exp(i\theta)$ multiplies the field and commutes with everything, so it preserves the centre for **every** value of $\theta$:

$$
\exp(i\theta)\,\xi e_t\in\mathbb{B}_C
\qquad\text{for all }\theta\in\mathbb{R}.
$$

The scalar carrier therefore carries the phase, and the phase is what a charge is. The contrast with the vector field is exact: the same test on a material four-vector keeps it material only for $\theta\equiv0$ and $\theta\equiv\pi$, that is only for $\pm1$, and every other phase leaves the sector. **The centre carries a continuous phase and the material sector does not**, and that is the structural reason why the scalar and the vector behave differently under a coupling.

## Where the Carrier Fails, and What That Selects

The restriction fails for one operator, and the failure is informative. With the covariant derivative $\tilde\nabla_{\mathrm{gco},\mu}=\partial_\mu+\frac{i\,ϙ}{\hbar}A_\mu$, whose coefficients are central scalars in the slots of one material element, the second-order operator of the algebra gives

$$
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}(\xi e_t)
=\Big(\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}\xi\Big)e_t+\frac{i\,ϙ}{\hbar}\,\xi\,\tilde F ,
$$

and the second term is a **pure vector**. The centre is not invariant under that operator whenever the field strength does not vanish.

The component equation

$$
\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}\tilde\Xi=k_m^{2}\tilde\Xi
$$

does preserve the centre, because each $\tilde\nabla_{\mathrm{gco},\mu}$ is central. So the free theory's two writings, which agree identically when no connection is present, are separated by the coupling, and the carrier keeps one of them. **The carrier is a criterion on the writing of the equation**: the coupled scalar field is central in the component form that the action produces, and it is not central in the operator-square form.

That is a genuine consequence and not a bookkeeping remark. It says that the covariant square of the gradient is not the operator of a spin-zero field: the extra term is a spin-one object, the field strength, and a scalar field cannot carry it.

## Summary

The Klein–Gordon operator is central and real, so it preserves every subspace closed under real scalars and cannot choose among them. The spin chooses: a spin-zero field has one complex value at each event, and its carrier is the centre $\mathbb{B}_C$, of complex dimension one. Closure on the centre is free and exact. The restriction discards three complex coefficients, each of which would have been a further independent scalar field.

The two sectors meet the centre in one real line each: real scalars are informational and imaginary scalars are material, and the central $i$ exchanges the two lines. The material declaration for a scalar field is therefore a choice of phase, not a physical distinction, because $i\mathbb{B}_\Psi=\mathbb{B}_\Phi$ and $i$ is central.

The centre carries a continuous phase, so the charge survives the restriction; this is where it differs from the material sector, which keeps only $\pm1$. The restriction fails for the covariant square of the gradient, whose extra term is the field strength, and holds for the component equation. The carrier therefore selects which of the two coupled writings is the equation of a scalar field.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_C=\{q\,e_t\}$ | The centre, complex dimension one |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| ${}^{*}$, ${}^{\natural}$, $\mathrm{Sc}$ | Hermitian conjugation, quaternion conjugation, scalar part |
| $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ | The d'Alembertian, central and real |
| $\tilde\nabla_{\mathrm{gco},\mu}=\partial_\mu+\frac{i\,ϙ}{\hbar}A_\mu$ | Covariant derivative, central in each slot |
| $\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)$ | Field strength, the obstruction to the covariant square |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html), for the equation, the four-copy theorem and the conjugate pair.
- [The Carrier of the Dirac Field](the-carrier-of-the-dirac-field.html), for the carrier of a spin-one-half field and the minimal left ideal.
- [The Carrier of the Proca Field](the-carrier-of-the-proca-field.html), for the carrier of a spin-one field and the material sector.
- [The Carriers, the Spin and the Closure](the-carriers-the-spin-and-the-closure.html), for the classification of the three carriers and their relation to the sectors.
- [The Coupled Klein–Gordon Equation in Biquaternionic Form](the-coupled-klein-gordon-equation-in-biquaternionic-form.html), for the coupling prescription and the two writings of the coupled equation.
- [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the collapse of the polar word on a central field.
- [Higher Spin from Tensor Products: The Three Carriers and the Absence of a Fourth](higher-spin-from-tensor-products-the-three-carriers-and-the-absence-of-a-fourth.html), for the module category that fixes the carrier.
- [Algebra and Element Conventions](algebra-and-element-conventions.html), for the algebra, the units and the conjugations.
