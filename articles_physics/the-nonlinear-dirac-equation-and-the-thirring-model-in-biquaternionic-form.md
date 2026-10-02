# __The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form__

## Introduction

A **nonlinear Dirac equation** is a Dirac equation with a self-interaction term. The free equation is linear in the field, so that solutions superpose; a term quadratic or cubic in the field destroys that superposability and makes the equation describe a fermion that acts on itself. The best-motivated case is not a guess. In the **Einstein–Cartan–Sciama–Kibble** extension of general relativity, the spin of matter is the source of the antisymmetric part of the connection, the torsion; that torsion couples to the spinor's axial current, and when it is eliminated from the field equations it leaves an effective **axial-axial spin–spin self-interaction** that is cubic in the spinor. The resulting equation is the standard example of a nonlinearly self-interacting Dirac field, and it is a toy model for the idea that the fermion's self-interaction regulates its own short-distance behaviour.

Two models dominate the literature and stand for the two channels. The **Thirring model** (Thirring 1958) is a $1+1$-dimensional theory whose interaction is the square of the vector current, $\left(\bar\psi\gamma^\mu\psi\right)^2$; it is exactly solvable and is the field-theory side of the bosonisation correspondence with the sine-Gordon model. The **Soler model** (Soler 1970) is a $3+1$-dimensional theory whose interaction is the square of the scalar bilinear, $\left(\bar\psi\psi\right)^2$; it is the mean-field relative of the Nambu–Jona-Lasinio four-fermion interaction, and it is the model in which exact closed-form solutions have been found.

This article states these equations, gives the Einstein–Cartan route that produces one of them from geometry, organises the possible interactions by the fermion bilinears they use, and gives the biquaternion reading. The framework's contribution is a **placement of the channels**: each quartic interaction is built from one of the local bilinears — the scalar density $S = \bar\psi\psi$, the vector current $V^\mu = \bar\psi\gamma^\mu\psi$, the axial current $A^\mu = \bar\psi\gamma^\mu\gamma_5\psi$ — and each of these has a definite place in the framework's structure. $S$ is the mass channel, the object whose expectation is the dynamical mass of the companion article on the chiral condensate. $V^\mu$ is the material-sector current, the object of the companion articles on minimal coupling and on the Gordon decomposition. $A^\mu$ is the axial current, and the framework's linear mass is precisely what breaks its conservation; an axial-axial self-interaction is therefore a coupling in the channel conjugate to the mass. A quartic interaction is also **bosonic**: it is even in the fermion field and carries zero fermion number, so it passes through the framework's central phase untouched, which is why a self-interaction is compatible with the exact vector symmetry.

What the framework does **not** supply is equally definite, and follows from the minimal-coupling article. Every one of the bilinears above is a spinor-module object: the Dirac adjoint $\bar\psi = \psi^\dagger\gamma^0$ carries the Clifford-odd $\gamma^0$ and the axial current carries $\gamma_5$ as well, and neither is in the even subalgebra $\mathbb{B}$. The framework names the channels and places them in its sectors; it does not derive the self-interaction from a product in the algebra, and it adds no solution, coupling or prediction of its own.

The article is organised as follows. The next section explains why a self-interaction is cubic and how geometry produces one. A section states the Thirring and Soler models. A section gives the Einstein–Cartan torsion route and the Hehl–Datta equation. A section lists the local bilinears and the channel each model uses. A section gives the biquaternion reading. A short section records the verified two-dimensional relations. The closing sections are the open questions, the summary, the notation table and the literature.

The conventions are those of the companion articles. The Clifford generators satisfy $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$ with $g = \mathrm{diag}(+1,-1,-1,-1)$, the chirality operator is $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ with $\gamma_5^2 = I_4$, and the Dirac adjoint is $\bar\psi = \psi^\dagger\gamma^0$. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_k^2 = -e_0$, central imaginary $i$, and the mass term is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R$.

## Why the Dirac Equation Becomes Nonlinear

### Self-interaction and the cubic form

The free Dirac equation is linear, and its solutions form a vector space. A self-interaction is a term in the equation that is built from the field itself, and the lowest non-trivial such term that is compatible with the symmetries is quadratic in the **bilinears**. Since a bilinear is quadratic in $\psi$, a product of two bilinears is quartic in the field; an equation obtained by adding such a term to the Dirac equation, or by varying an action containing it, is called nonlinear even though the resulting Euler–Lagrange equation is often cubic in the field once one factor is used as the source. This is the sense in which the axial-axial term below is "cubic": writing $B(\psi)$ for the bilinear built from the field, the equation is

$$
\left(i\gamma^\mu\partial_\mu - m\right)\psi + B(\psi)\,\psi = 0,
$$

in which the bilinear is quadratic in $\psi$ and the explicit field supplies the third power.

The physical requirement is Lorentz covariance and the absence of derivatives. The possible interactions are therefore the local quartic combinations of the Lorentz-covariant bilinears, and they are finite in number because the bilinears themselves are.

### The Einstein–Cartan route

The reason the axial-axial channel is the physically motivated one is geometric, and it is worth stating because it removes the arbitrariness of the model-building. In Einstein–Cartan theory the affine connection is not required to be symmetric. Its antisymmetric part is the **torsion** $T^\mu{}_{\nu\lambda}$, and it is an independent variable in the action, sourced algebraically by the spin tensor of the matter. Because the torsion appears in the covariant derivative of a spinor through the spin connection, a Dirac field minimally coupled to a torsionful connection acquires a direct coupling between its spin (its axial current) and the torsion. Eliminating the torsion through its own algebraic field equation leaves an effective four-fermion term, the **Hehl–Datta interaction** (Hehl and Datta 1971), which is exactly an axial-axial spin–spin contact term. No new coupling constant is introduced; the strength is fixed by the gravitational constant, which is why the effect is unobservably small at ordinary densities and interesting only in the extreme.

## The Two Standard Models

### The Thirring model

The Thirring model is defined in $1+1$ dimensions by the Lagrangian density

$$
\mathcal{L} = \bar\psi\left(i\not\partial - m\right)\psi
- \frac{g}{2}\left(\bar\psi\gamma^\mu\psi\right)\left(\bar\psi\gamma_\mu\psi\right),
$$

with $\psi = \left(\psi_+, \psi_-\right)$ a two-component spinor, $g$ the coupling, $m$ the mass, and $\gamma^\mu$ the two-dimensional gamma matrices. There is only one independent local quartic interaction in two dimensions: the spinor has four real components and the Pauli principle, together with the Fierz rearrangement identities of the two-dimensional Clifford algebra, makes the quartic terms equivalent. The vector-vector and axial-axial combinations are related by the two-dimensional Hodge duality of the currents, so a single coupling $g$ covers the model.

The **massless** Thirring model is exactly solvable: the multipoint correlation functions are known in closed form (Johnson; Hagen; Klaiber), and the theory satisfies the Osterwalder–Schrader axioms, so it is a genuine quantum field theory and not merely a Lagrangian. The **massive** model is solvable by the Bethe ansatz, which gives the exact mass spectrum and scattering matrix; multi-particle production cancels on shell. The massive Thirring model is exactly equivalent to the quantum **sine-Gordon** model, with the fundamental fermions of the one corresponding to the solitons of the other — the Coleman–Mandelstam equivalence, which the companion article on bosonisation develops in the framework's notation.

### The Soler model

The Soler model is defined in $3+1$ dimensions by

$$
\mathcal{L} = \bar\psi\left(i\not\partial - m\right)\psi
+ \frac{g}{2}\left(\bar\psi\psi\right)^2,
$$

with $\psi$ a four-component spinor and $\not\partial$ the four-dimensional slash. Its interaction is the square of the **scalar** bilinear, the same channel in which a fermion mass lives, and its sign convention makes a sufficiently strong coupling favour a nonzero $\langle\bar\psi\psi\rangle$. It is the single-particle relative of the Nambu–Jona-Lasinio model, in which the same quartic term is the interaction whose mean-field treatment produces a dynamical mass and a chiral condensate; the companion article on the chiral condensate owns the gap equation, the critical coupling and the Goldstone counting. A pseudoscalar variant replaces $S^2$ by $\left(i\bar\psi\gamma_5\psi\right)^2$, and the two together are the chirally invariant combination of the NJL interaction.

Recently, exact solutions of the Soler model in closed form have been found, which is why the model is of more than illustrative interest: it is one of the few interacting fermion equations with explicit non-perturbative solutions.

## The Hehl–Datta Interaction from Torsion

The geometric route of the earlier section gives the equation

$$
i\gamma^\mu\nabla_\mu\psi - m\psi
+ \frac{3\kappa}{8}\left(\bar\psi\gamma_\mu\gamma_5\psi\right)\gamma^\mu\gamma_5\psi = 0,
$$

where $\nabla_\mu$ is the general-relativistic covariant derivative of a spinor, $\kappa = 8\pi G/c^4$ is the Einstein gravitational constant, and the interaction is the axial-axial contact term produced by the torsion of the spinor's own spin. The coefficient $3\kappa/8$ is fixed by the geometry, not chosen. The cubic term becomes significant only at densities of order $m^2/\kappa$, which are far outside laboratory matter; the interaction is a high-density effect.

If the torsion is allowed to propagate rather than to be eliminated algebraically, the same nonlinear structure survives with the coefficient replaced by a term involving the spinor–torsion coupling $X$ and the torsion mass $M$, of the form $-X^2/M^2$. With the natural sign this self-interaction is **repulsive**, as in the Nambu–Jona-Lasinio model, and its scale is set by the torsion mass. The two routes — a non-propagating torsion fixed by gravity, and a propagating torsion with its own mass — therefore give the same axial-axial channel with different coefficients, which is the reason the channel is regarded as the generic one rather than a special choice.

## The Local Channels and Their Sectors

### The bilinears

A single Dirac field has five types of local bilinear, classified by their Lorentz transformation:

| Bilinear | Name | Lorentz type | Field parity |
|---|---|---|---|
| $S = \bar\psi\psi$ | Scalar | scalar | even |
| $P = i\bar\psi\gamma_5\psi$ | Pseudoscalar | scalar | odd |
| $V^\mu = \bar\psi\gamma^\mu\psi$ | Vector (current) | four-vector | even |
| $A^\mu = \bar\psi\gamma^\mu\gamma_5\psi$ | Axial vector | four-vector | odd |
| $T^{\mu\nu} = \bar\psi\sigma^{\mu\nu}\psi$ | Tensor | antisymmetric rank 2 | even |

Each is quadratic in the field. A local quartic interaction without derivatives is a Lorentz-covariant product of two of them, and only a few combinations are independent because the Fierz identities relate them.

### Which channel each model uses

| Model | Dimensions | Interaction | Channel | Framework home |
|---|---|---|---|---|
| Thirring | $1+1$ | $-\frac{g}{2}\left(\bar\psi\gamma^\mu\psi\right)^2$ | vector current | material sector $\mathbb{M}_-$ |
| Soler | $3+1$ | $+\frac{g}{2}\left(\bar\psi\psi\right)^2$ | scalar density | the mass channel |
| NJL / pseudoscalar variant | $3+1$ | $S^2 + P^2$ | scalar–pseudoscalar | the mass channel, chirally paired |
| Hehl–Datta (torsion) | $3+1$ | $+\frac{3\kappa}{8}\left(\bar\psi\gamma^\mu\gamma_5\psi\right)^2$ | axial current | the axial channel |

The table is the article's organising object. The Soler and NJL models act in the channel where the mass lives; the Thirring model acts in the channel where the current lives, which in two dimensions is the same channel as the axial one; the torsion-induced model acts in the axial channel, which is the channel the mass **breaks**.

## The Biquaternion Reading

### The interaction is bosonic, so the central phase passes through it

A quartic product of two bilinears is even in the fermion field, so it is invariant under the central phase $\tilde\Psi \mapsto e^{i\alpha}\tilde\Psi$ and carries fermion number zero. In the framework's terms it is built from the algebra's **central scalar invariants**, and it therefore does not disturb the exact vector $U(1)$ the companion articles emphasise: the symmetry the mass breaks is the axial one, and the phase symmetry survives even a strong self-interaction. This is why a self-interaction can generate a mass dynamically without conflicting with the conservation of fermion number, which is the whole content of the NJL mechanism.

### The three channels in the framework's sectors

The three channels of the table map onto three different structures the framework already carries, and the mapping is the article's main observation.

- **The scalar density $S$ is the mass channel.** The framework's mass term is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R$. An interaction in the $S$ channel adds to that term, so the Soler and NJL models are, in the framework's terms, models in which the mass is allowed to be a function of the state rather than a fixed parameter. The companion article on the chiral condensate states the consequence: the condensate $\langle S\rangle$ is the order parameter and the self-consistent mass is the gap equation.
- **The vector current $V^\mu$ is the material-sector current.** The companion articles on minimal coupling and on the Gordon decomposition place the conserved current in $\mathbb{M}_-$, the material sector; the Thirring interaction is the square of that object. Its being the same channel as the axial one in two dimensions is the two-dimensional accident (the Hodge duality of the currents) that makes the Thirring model a one-coupling theory.
- **The axial current $A^\mu$ is the channel conjugate to the mass.** The linear mass breaks the axial symmetry and gives the axial-current divergence $\partial_\mu j_5^\mu = 2im\,\bar\psi\gamma_5\psi$; the torsion-induced interaction is built from $A^\mu$ itself. An axial-axial attraction is therefore a coupling in the channel whose conserved charge the mass destroys, which is exactly the channel in which a strong coupling can restore the symmetry by generating a mass — the mechanism the condensate article treats.

### What the framework does not supply

The identification above is a placement, not a derivation, and the boundary should be stated in the same terms as the companion articles. Each bilinear in the table is a spinor-module object. The scalar and vector bilinears require the Clifford-odd $\gamma^0$ of the Dirac adjoint; the pseudoscalar and axial bilinears require $\gamma_5$ as well; neither element is in the even subalgebra $\mathbb{C}\ell_{1,3}^+ \cong \mathbb{B}$. The consequence is the one recorded in the minimal-coupling article: a bilinear built only from $\tilde\Psi$ and $\tilde\Psi^{*}$ inside $\mathbb{B}$ cannot supply these objects, and the self-interaction, like the current, is irreducibly a spinor-module statement. The framework transcribes the models, verifies the two-dimensional algebra of their channels, and locates each channel in its sectors. It supplies no coupling, no solution, no spectrum, and no prediction.

Two further limits are inherited from other gaps. The Einstein–Cartan route needs a torsionful connection with a field equation; the companion article on curved spacetime records that the framework can carry the connection as an object of its own Lie subspace but generates no dynamics for it, so a biquaternion torsion is in that agenda and not in the constructed part. And the exact solubility of the massless Thirring model is a property of two-dimensional quantum field theory with no biquaternion counterpart; the framework's two-component reduction explains why two dimensions are special (a two-component spinor and a scalar have the same number of degrees of freedom), but it does not reproduce the solution.

## Verified Two-Dimensional Relations

The two-dimensional identities on which the Thirring model's "one coupling" rests were checked directly. With the mostly-minus two-dimensional generators $\gamma^0 = \sigma_z$, $\gamma^1 = i\sigma_y$, so that $\left(\gamma^0\right)^2 = I_2$, $\left(\gamma^1\right)^2 = -I_2$, $\{\gamma^0,\gamma^1\} = 0$, and with $\gamma_5 = \gamma^0\gamma^1$ (so $\gamma_5^2 = I_2$), the following held exactly over $100$ random two-component spinors — that is, with residual $0$ and not merely to numerical precision:

- the Clifford relations $\left(\gamma^0\right)^2 = I_2$, $\left(\gamma^1\right)^2 = -I_2$, $\{\gamma^0,\gamma^1\} = 0$ and $\gamma_5^2 = I_2$;
- the current duality $A^\mu \propto \epsilon^{\mu\nu}V_\nu$ — the axial current is the Hodge dual of the vector current;
- consequently $A^\mu A_\mu = -V^\mu V_\mu$, so the vector–vector and axial–axial quartic terms differ only by sign, and a single coupling exhausts the local quartic interactions.

The duality is the exact reason the two-dimensional model has one coupling, and it is a property of the Clifford algebra and not of the framework.

## Open Questions

1. **A biquaternion-natural self-interaction.** Is there a functional of $\mathbb{B}$-valued bilinears whose variation reproduces the Soler or Thirring interaction without the Clifford-odd $\gamma^0$ and $\gamma_5$? This is the current question of the minimal-coupling article met from the interaction side.

2. **Torsion in the framework's own notation.** The curved-spacetime article carries the connection in the Lie subspace but gives it no equation. The antisymmetric (torsion) part of that connection, and the algebraic elimination that produces the Hehl–Datta term, are not written in the framework's notation.

3. **The condensate and the nonlinear equation.** A strong axial-axial or scalar self-interaction generates a mass. Is the biquaternion form of the self-consistent (gap) equation the same statement as the framework's linear mass term with $m$ promoted to an expectation, and can the two be written as one equation?

4. **Two dimensions and the central charge.** The bosonisation article matches the central charges $c_{\mathrm{Dirac}} = 1 = c_{\mathrm{boson}}$. Does the nonlinear (massive Thirring) case add a biquaternion statement about the interacting central charge, or is it entirely the bosonic side's renormalisation?

5. **The exact solutions.** Closed-form solutions of the Soler model exist, and the massive Thirring model is Bethe-ansatz solvable. Neither has been transcribed into the framework's notation, and it is not known whether the biquaternion form of the equations makes either more transparent.

## Summary

A nonlinear Dirac equation adds a self-interaction built from the field's bilinears to the free equation. The physically motivated case is geometric: in Einstein–Cartan theory the torsion sourced by the spinor's own spin, eliminated through its field equation, leaves the axial-axial Hehl–Datta term $\frac{3\kappa}{8}\left(\bar\psi\gamma_\mu\gamma_5\psi\right)\gamma^\mu\gamma_5\psi$ with a coefficient fixed by the gravitational constant. The two standard models use the other two channels: the Thirring model in $1+1$ dimensions uses the square of the vector current and is exactly solvable, with the massive case equivalent to sine-Gordon; the Soler model in $3+1$ dimensions uses the square of the scalar bilinear and is the mean-field relative of the NJL interaction.

The biquaternion reading places the channels. The scalar density is the mass channel, whose expectation is the dynamical mass of the chiral-condensate article. The vector current is the material-sector current of the minimal-coupling and Gordon articles. The axial current is the channel the linear mass breaks, so an axial-axial interaction is a coupling in the channel conjugate to the mass — the channel in which a strong coupling restores the symmetry by generating a mass. Every quartic interaction is bosonic, so it passes through the framework's central phase and leaves the exact vector symmetry intact. Each bilinear, however, requires the Clifford-odd $\gamma^0$ and $\gamma_5$, outside the even subalgebra $\mathbb{B}$; the framework transcribes the models and locates their channels, and supplies no coupling, solution or prediction. The one exact algebraic fact the article verifies is two-dimensional: the axial current is the Hodge dual of the vector current, so $A^\mu A_\mu = -V^\mu V_\mu$ and the Thirring model has a single coupling.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; $e_k^2 = -e_0$, central $i$ |
| $\bar\psi = \psi^\dagger\gamma^0$ | Dirac adjoint (carries the Clifford-odd $\gamma^0$) |
| $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, $\gamma_5^2 = I_4$ | Chirality operator |
| $S = \bar\psi\psi$ | Scalar density (mass channel) |
| $P = i\bar\psi\gamma_5\psi$ | Pseudoscalar density |
| $V^\mu = \bar\psi\gamma^\mu\psi$ | Vector current (material sector in the framework) |
| $A^\mu = \bar\psi\gamma^\mu\gamma_5\psi$ | Axial current (channel broken by the mass) |
| $T^{\mu\nu} = \bar\psi\sigma^{\mu\nu}\psi$ | Tensor bilinear |
| $g$ | Self-coupling of the Thirring and Soler models |
| $\kappa = 8\pi G/c^4$ | Einstein gravitational constant |
| $\frac{3\kappa}{8}\left(\bar\psi\gamma^\mu\gamma_5\psi\right)^2$ | Hehl–Datta torsion-induced axial-axial interaction |
| $X$, $M$ | Spinor–torsion coupling and torsion mass (propagating-torsion case) |
| $A^\mu A_\mu = -V^\mu V_\mu$ | Two-dimensional current duality (verified exactly) |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational and material sectors |

## Further Reading

- W. E. Thirring, "A soluble relativistic field theory," *Annals of Physics* **3** (1958) 91–112, for the original two-dimensional model.
- M. Soler, "Classical, stable, nonlinear spinor field with positive rest energy," *Physical Review D* **1** (1970) 2760–2765, for the scalar-interaction model in four dimensions.
- F. W. Hehl and B. K. Datta, "Nonlinear spinor equation and asymmetric connection in general relativity," *Journal of Mathematical Physics* **12** (1971) 1334–1339, for the torsion-induced axial-axial interaction.
- F. W. Hehl, P. von der Heyde, G. D. Kerlick and J. M. Nester, "General relativity with spin and torsion: foundations and prospects," *Reviews of Modern Physics* **48** (1976) 393–416, for the Einstein–Cartan–Sciama–Kibble theory and its matter couplings.
- S. Coleman, "Quantum sine-Gordon equation as the massive Thirring model," *Physical Review D* **11** (1975) 2088–2097, for the equivalence of the massive Thirring and sine-Gordon models.
- C. R. Hagen, "Quantum sine-Gordon equation and the Thirring model," and B. Klaiber, "The Thirring model," in *Lectures in Theoretical Physics* (Gordon and Breach, 1968), for the exact solution of the massless model.
- Y. Nambu and G. Jona-Lasinio, "Dynamical model of elementary particles based on an analogy with superconductivity," *Physical Review* **122** (1961) 345–358, for the four-fermion interaction whose mean field gives a dynamical mass.
- L. H. Ryder, *Quantum Field Theory* (Cambridge, 2nd ed. 1996), and W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for the nonlinear spinor equations and their soliton-like solutions.
- The companion articles of this series: *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, *The Gordon Decomposition of the Dirac Current in Biquaternionic Form*, *The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form*, *Bosonization in Biquaternionic Form*, and *Curved Spacetime and the Biquaternion Framework*.
