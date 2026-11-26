# __The Path Integral and the Coupled Klein–Gordon Equation in Biquaternionic Form__

## Introduction

This article puts the coupled scalar action into the functional integral. *The Path Integral and the Klein–Gordon Equation in Biquaternionic Form* defines the integral over central-valued fields and evaluates the free Gaussian. *The Lagrangian and the Coupled Klein–Gordon Equation* supplies the action with the covariant derivative in every slot. Joining the two costs one substitution and produces one new structure, and the structure is the subject of the article.

The substitution. Minimal coupling replaces $\tilde\nabla_\Phi$ by $\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{2\pi iϙ}{h}\tilde A_\Phi$ in the kinetic term. Nothing else changes: the field stays in the centre, the measure stays flat, the mass term stays $\nu_m^{2}\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$, and the phase stays central and $*$-unitary.

The finding is one sentence, and the article is its unfolding. The exponent splits into three terms — the free one, a term linear in the potential times the current, and a term quadratic in the potential with no derivative — and the third term is what makes the sum invariant, so the integral cannot be built from the current alone.

Four consequences follow, and each is stated exactly or checked.

- The split is an algebraic identity, exact for every connection and every field, checked to $6\times10^{-15}$.
- The local transformation of the integration variable is a rotation of the two real components at each point, so the measure is invariant with no Jacobian, and on a lattice the invariance requires the phase to be carried in an exponential link and not in a linear one.
- The Gaussian inverts the paired operator $\sum_{\imath}(\partial_{\imath}-\bar c_{\imath})(\partial_{\imath}+c_{\imath})-\nu_m^{2}$, which is the equation's operator for a purely vector connection and is not the equation's operator for a scalar potential.
- The current is the first variation of the integral with respect to the connection, and its conservation is the differentiated form of the measure's invariance.

It does not produce a new prediction: the integral is the standard charged scalar's. It does not construct the continuum measure. It does not resolve the sign question that the variational companion records; it locates that question at the pole of the propagator, where it is observable, and stops there.

## Conventions

The algebra and the pairing are the free companion's: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $e_t=1$, $\vec e_{\imath}^{2}=-e_t$, $i$ central, $\mathrm{Sc}(\cdot^{*}\cdot)$ Hermitian. The covariant derivative and its conjugate are

$$
\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{2\pi i\,ϙ}{h}\tilde A_\Phi,
\qquad
(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{2\pi i\,ϙ}{h}\tilde A_\Phi^{\natural},
$$

with $\natural$ on the invertibles and never on the connection's coefficients, which are scalars. Write $c_{\imath}=\frac{2\pi iϙ}{h}A_{\imath}$ for the slot's coefficient, so that the covariant derivative is $\partial_{\imath}+c_{\imath}$ acting coefficient-wise. The material convention of the coupled companions is $A_t=i a'_t$ with $a'_t$ real and $\vec A$ real, so $c_t$ is real and the three $c_{\imath}$ are imaginary.

The action and the weight. The variational companion's matter action,

$$
S_{\mathrm{gco}}[\tilde\Xi,\tilde A]=\frac{h}{4\pi}\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\Bigl[\bigl(\tilde\nabla_{\mathrm{gco},\Phi,t}\tilde\Xi\bigr)^{*}\tilde\nabla_{\mathrm{gco},\Phi,t}\tilde\Xi\Bigr]-\sum_{\imath\in\{x,y,z\}}\mathrm{Sc}\Bigl[\bigl(\tilde\nabla_{\mathrm{gco},\Phi,k}\tilde\Xi\bigr)^{*}\tilde\nabla_{\mathrm{gco},\Phi,k}\tilde\Xi\Bigr]-4\pi^{2}\nu_m^{2}\,\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\Bigr\},
$$

is the exponent, in the free companion's normalisation and with the covariant derivative in every slot, with the weight $\exp(\frac{2\pi iS_{\mathrm{gco}}}{h})$. The temporal slot enters with $+$ and the three spatial ones with $-$, which is the material metric written out. The connection is held fixed in the integral over the field, and the field is held fixed in the integral over the connection; this article treats the first.

Which operator the exponent gives. The variational companion shows that the covariant square of a central field is not central: $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}\tilde\nabla_{\mathrm{gco},\Phi}(\xi e_t)=\bigl(\sum_{\imath} D_{\imath}^{2}\xi\bigr)e_t+\frac{2\pi iϙ}{h}\xi\tilde F$, with a vector part that no central field can carry. The action's kinetic term avoids that difficulty by being a sum of squared moduli of one slot each, $\sum_{\imath}\mathrm{Sc}\bigl[(\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde\Xi)^{*}\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde\Xi\bigr]$, and this is the form the exponent carries. The exponent's form fixes the quadratic form, and a Gaussian inverts its quadratic form: by parts that is the paired operator of §*The Quadratic Form and the Operator It Inverts*, whereas the companion's stated equation is built on $\Box_{\mathrm{gco},\Phi}=\sum_{\imath}\tilde\nabla_{\mathrm{gco},\Phi,\imath}^{2}$, and the two operators differ whenever $\bar c_{\imath}\ne-c_{\imath}$. The article follows the exponent and records the difference.

## The Exponent Splits into Three Terms

The identity. For one slot and one central coefficient,

$$
\bigl\lvert\partial_{\imath}\Xi+c_{\imath}\Xi\bigr\rvert^{2}
=\bigl\lvert\partial_{\imath}\Xi\bigr\rvert^{2}
+2\,\mathrm{Re}\bigl(\bar c_{\imath}\,\Xi^{*}\partial_{\imath}\Xi\bigr)
+\lvert c_{\imath}\rvert^{2}\lvert\Xi\rvert^{2},
$$

which is the expansion of a squared modulus and holds for every field and every connection. Summed over the four slots it gives

$$
S_{\mathrm{gco}}=S_{0}+\int\mathrm{d}^{4}x\;\Bigl[2\,\mathrm{Re}\sum_{\imath}\bar c_{\imath}\,\Xi^{*}\partial_{\imath}\Xi+\sum_{\imath}\lvert c_{\imath}\rvert^{2}\lvert\Xi\rvert^{2}\Bigr],
$$

with $S_0$ the free action. **The three terms are the free action, the current times the potential, and the potential squared.**

The split is checked as an identity. On a seven-site chain with a random complex field and random coefficients of the material signs, the difference of the two sides, slot by slot and summed over the four slots, is $4\times10^{-16}$ relative to the sum, which is the arithmetic of the same quantity computed twice. The identity is exact and the number only locates it.

The middle term is the current. The variational companion writes the current as $J_{\imath}=2\,\mathrm{Re}\,\mathrm{Sc}\bigl[i\tilde\Xi^{*}\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde\Xi\bigr]$, and for a central field with the covariant derivative's coefficient $c_{\imath}$ the comparison gives

$$
2\,\mathrm{Re}\bigl(\bar c_{\imath}\Xi^{*}\partial_{\imath}\Xi\bigr)=-\frac{2\pi ϙ}{h}A_{\imath} J_{\imath}
$$

up to the term that carries $c_{\imath}$ twice, which is the third. The interaction is therefore the current times the potential plus the potential squared, and no other object appears.

The third term has no derivative, and that is its function. It is the term a "current times potential" presentation omits. It is also the term that makes the exponent invariant: the current's term alone changes by a total derivative under a local transformation, and the potential-squared term is what supplies the rest. The local invariance of the exponent is a cancellation between the second and third terms, and the article states the cancellation before it states the consequence, because the consequence is the next section.

For fixed connection the exponent is quadratic in the field. Every term of the split is quadratic in $\Xi$ and the coefficients are fixed numbers, so the functional integral is a Gaussian for every connection, with a quadratic form that carries the $A^{2}$ term as part of its coefficient. The coupling does not spoil the Gaussian; it moves the quadratic form.

## The Measure and Local Invariance

The transformation is a rotation at each point. Write $\tilde\Xi\mapsto e^{iϑ_{\mathrm{cph}}}\tilde\Xi$ with $ϑ_{\mathrm{cph}}=\frac{2\pi ϙ\Lambda}{h}$ and $\Lambda$ real. At one point the field is two real numbers, and the transformation rotates the pair by the angle $ϑ_{\mathrm{cph}}(x)$. A rotation has unit determinant, so the flat measure $\prod_x\mathrm{d}\Xi_1\mathrm{d}\Xi_2$ is invariant with no Jacobian at all. The measure's invariance is the statement that a local phase is orthogonal.

The lattice version, and the one technical requirement. On a lattice the covariant difference between neighbouring sites must carry the phase as an exponential and not as a linear term. A link $U_{j}=e^{i(\Lambda_{j}-\Lambda_{j+1})}$ makes the determinant of the quadratic form equal to the free one exactly: the ratio of determinants for a random pure gradient link field on six sites is $1.00000000000000$. The linearised link $U_j=1+i(\Lambda_j-\Lambda_{j+1})$ gives a ratio of $22.15$ on the same configuration. **The invariance is exact for the Wilson link and approximate for the linear one**, and the difference is the difference between a local transformation of the lattice and its first-order shadow.

What the invariance buys. The matter action, the mass term and the measure are each invariant, so the integral is a functional of the connection's orbit and not of the connection. The variational companion says the same thing about the action; the integral adds the measure, and the measure's invariance is what makes the statement a statement about the integral and not only about the integrand.

What it does not buy. The integral is not invariant under a transformation that moves the field and leaves the connection fixed, and that is the definition of a local symmetry rather than a symmetry. The article keeps the two apart throughout, because the current's conservation below is a consequence of the first and would be a false statement under the second.

## The Quadratic Form and the Operator It Inverts

The operator. Integrating by parts once per slot moves the derivative onto the first factor and leaves

$$
S_{\mathrm{gco}}=\frac{h}{4\pi}\int\mathrm{d}^{4}x\;\mathrm{Sc}\Bigl[\tilde\Xi^{*}\Bigl(\sum_{\imath}\bigl(\partial_{\imath}-\bar c_{\imath}\bigr)\bigl(\partial_{\imath}+c_{\imath}\bigr)-4\pi^{2}\nu_m^{2}\Bigr)\tilde\Xi\Bigr]
$$

up to a boundary term, so the Gaussian's inverse is the paired operator's Green's function. The free companion's statement that the two-point function is the inverse of the quadratic form survives the coupling with the paired operator in place of the d'Alembertian.

The two operators differ, and by one term. The paired operator and the square of the covariant derivative are related by

$$
\sum_{\imath}\bigl(\partial_{\imath}-\bar c_{\imath}\bigr)\bigl(\partial_{\imath}+c_{\imath}\bigr)
-\sum_{\imath}\bigl(\partial_{\imath}+c_{\imath}\bigr)^{2}
=-\sum_{\imath}\bigl(\bar c_{\imath}+c_{\imath}\bigr)\bigl(\partial_{\imath}+c_{\imath}\bigr),
$$

which is exact as a composition of operators. **The two coincide exactly when $\bar c_{\imath}=-c_{\imath}$ in every slot**, which is the case of a purely imaginary coefficient.

Which slots satisfy the condition. The three spatial slots satisfy it for a real vector potential, because $\bar c_{\imath}=-i\frac{2\pi ϙ}{h}A_{\imath}=-c_{\imath}$. The temporal slot does not, because $c_t=-\frac{2\pi ϙ}{h}a'_t$ is real and $\bar c_t=c_t$. A purely vector connection gives one operator and a scalar potential gives two, and this is the variational companion's bookkeeping point reached from the integral's side.

The symbols, measured. Applying each operator to a plane wave on a periodic grid of $256$ points with wave number $3$, the squared operator's symbol for a real coefficient $0.31$ is $-8.8876+1.86i$ and the paired operator's is $-9.0798$, real; for an imaginary coefficient $1.30i$ both are $-18.4667$ and they agree to machine zero. The free value at the same wave number is $-8.9837$. The imaginary coefficient shifts the pair together and the real one separates them, and the separation has an imaginary part that the paired form does not have.

The pole, in the two cases. For a purely vector connection the shell is the free one at the shifted wave number, $\vec\kappa=2\pi\vec\nu_{\Phi}+\frac{ϙ}{h}\vec A$, exactly and with no residual. For a constant scalar potential the two operators give two different shells:

$$
\text{squared:}\quad\bigl(\omega-c_t\bigr)^{2}-\lvert\vec\kappa\rvert^{2}-4\pi^{2}\nu_m^{2}=0,
\qquad
\text{paired:}\quad\omega^{2}-\lvert\vec\kappa\rvert^{2}-4\pi^{2}\nu_m^{2}-c_t^{2}=0 .
$$

The first is the variational companion's $E\mapsto E+ϙ c\,a'_t$, the linear shift of the energy. The second has no linear shift and moves the mass squared by $c_t^{2}$. **The two are different physics and they are produced by two different operators from the same coupling.**

What this does to the open question. The variational companion records the discrepancy between its action and its equation in the temporal slot and leaves it open. The integral does not close it; it changes its status. A functional integral does not choose an operator by convention: it inverts the one the action gives it, and the pole of the propagator is where the choice is measured. The article therefore states the paired shell as the integral's and the squared shell as the equation's, and records that a measurement of the scalar potential's effect on the propagator's pole would decide between them.

## The Current Is the First Variation, and Its Conservation Is an Identity

The derivative of the integral. Because the connection appears in the exponent, differentiating the generating functional with respect to $A_{\imath}(x)$ brings down the current. For a fixed source,

$$
\frac{\delta}{\delta A_{\imath}(x)}\ln Z[J,\tilde A]=i\,\frac{2\pi ϙ}{h}\,\bigl\langle J_{\imath}(x)\bigr\rangle ,
$$

with $J_{\imath}$ the variational companion's current. **The current is not a separate construction in the integral's language: it is the response of the integral to the connection.**

The conservation is the measure's invariance, differentiated. Rotate the integration variable locally and use the measure's invariance; the exponent's change is a total divergence plus the field equation's terms, and the identity that survives is

$$
\partial_{\imath}\bigl\langle J_{\imath}(x)\bigr\rangle=0 ,
$$

in every correlation function and not only on the solutions. This is the Ward identity of the central phase symmetry, and it is the integral's form of the variational companion's second-Noether argument. The companion derives the conservation from the equations; the integral derives it from the measure, and the integral's version is the stronger one because it does not require the field to be on shell.

The check already quoted is the check of this section. The determinant of the quadratic form is unchanged by a pure gradient link to machine precision, and that invariance is the differentiated identity's source. A generating functional whose determinant does not move under a pure gradient link is a generating functional whose current is conserved.

What the identity is not. It is not the statement that the current is the source of the connection's equation; that is the second variation of the total action, and it belongs to the variational companion. The integral states one half of the pair — that the current is conserved in every correlation function — and the other half is a classical statement about the connection.

## The Two Readings of the Covariant Square, in the Integral

The fork, restated as a choice of measure. The coupled equation article distinguishes two theories: the scalar projection, which keeps the field central and drops the curvature's vector part, and the full equation in $\mathbb{B}$, which lets the field acquire vector components and couples the four coefficients through the field strength. The integral makes the fork a choice of integration domain.

The measure over the centre inverts the paired scalar operator. That is the previous section, and it is the standard charged scalar. The carrier fixes the measure, and this is where the propagation reaches the path integral. The spin-zero field is central, so the measure runs over the complex functions of $\mathbb{B}_C$ and the integral is the standard one for a charged scalar. An integral over all of $\mathbb{B}$ would be four decoupled copies of it, with the same operator in each and no curvature coupling, because a measure that is a product of four copies cannot mix them; that is the four-scalar theory, and the carrier is what keeps the block from it.

The curvature coupling needs a measure that does not factorise. The covariant square's vector part is $\frac{2\pi iϙ}{h}\xi\tilde F$, linear in the field and in the field strength. Its scalar part is exactly $\sum_{\imath} D_{\imath}^{2}\xi$ and its vector part is the field strength term: on a grid with a constant field strength the scalar part agrees with $\sum_{\imath} D_{\imath}^{2}\xi$ to $1.8\times10^{-16}$ and the vector part agrees with $\frac{2\pi ϙ}{h}\xi\,\mathrm{Vect}\tilde F$ to $5\times10^{-4}$, the residual being the difference scheme. The vector part is not small and it is not central, so a theory that carries it must integrate over the non-central directions.

What the article concludes about the fork. The integral over central fields is the standard theory and it is the one the action selects. The integral over $\mathbb{B}$ with the covariant square in the exponent would be a different theory, and whether it is admissible is the equation companion's open question, not this article's. **The integral's contribution is to say that the two theories differ in their measure and not only in their operator.**

## The Semiclassical Expansion

The classical field and the source. With a source the stationary point of the exponent is $\Box_{\mathrm{gco},\Phi}\tilde\Xi-4\pi^{2}\nu_m^{2}\tilde\Xi=-\tilde J$, the coupled equation with a source, and the expansion about it separates into the classical action, a vanishing linear term, and the quadratic fluctuation. The one-loop factor is $[\det(\Box_{\mathrm{gco},\Phi}-4\pi^{2}\nu_m^{2})]^{-1/2}$ for the squared reading and $[\det(\text{paired}-\nu_m^{2})]^{-1/2}$ for the integral's, and the two differ by the term of §*The Quadratic Form and the Operator It Inverts*.

Everything remains central. The classical field is central, the fluctuation operator's coefficients are central, the determinant is a central scalar, and the effective action is the Legendre transform of a central functional. **The coupling changes no object's type**, which is the free companion's verdict and the coupled companion's, and the integral adds no exception.

The background-field reading. The determinant depends on the connection only through the covariant operator, so its variation with respect to $A_{\imath}$ is the current's two-point function and the same Ward identity holds at every order. The article states this and does not compute it; the one-loop determinant of a charged scalar in a background is a standard object and the algebra adds nothing to it.

## What the Integral Adds and Does Not Add

Adds.

- The three-way split of the exponent, exact, with the potential-squared term identified as the one that carries the local invariance.
- The measure's invariance as a rotation, with the lattice requirement that the link be an exponential; the Wilson link reproduces the free determinant to machine precision and the linearised link does not.
- The identification of the operator the Gaussian inverts, and with it the statement that the integral and the equation can carry different poles in a scalar potential.
- The current as the first variation of the integral, and its conservation as the differentiated measure invariance rather than as a consequence of the equations.
- The fork between the two readings of the covariant square, restated as a choice of measure.

No new prediction and no new solution: the integral is the standard charged scalar's. No continuum measure and no regularisation of the determinant's phase. No resolution of the scalar-potential sign question; the article sharpens it to a statement about the pole. No treatment of the interacting theory and none of the connection's own integral, which belongs to the connection path integral article.

The honest ledger. The coupling contributes one term to the exponent, one freedom to the quadratic form, and one identity to the measure. Everything else — the centrality, the Gaussian, the semiclassical structure — is the free theory's, and the article's content is the location of the three.

## Open Questions

1. The pole in a scalar potential. The paired operator and the squared operator give two different shells, and the article does not decide which a physical propagator follows. The decision is a measurement or a first-principles argument about which operator the corpus's coupled equation should state, and the variational companion's open question is the same question.

2. The measure over $\mathbb{B}$. Whether an integral over the full algebra with the covariant square in the exponent is a consistent theory, and whether its measure can be defined, is open. The article states the fork and does not take a side.

3. The determinant's phase. The free companion leaves it open, and the coupling adds a dependence on the connection without changing the difficulty. A background with a nonzero field strength makes the operator's spectrum discrete in the transverse directions — the Landau levels of the equation companion — and the determinant's phase in that setting is a standard but unattractive computation.

4. The interacting theory. A central interaction $\digamma_{\mathrm{qtc}}\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)^{2}$ preserves the centrality of every object and the flatness of the measure, and the three-way split survives with an extra term. Whether the algebra suggests a preferred normalisation is the free companion's question and is not pursued here.

5. The lattice's exponential link in four dimensions. The one-dimensional check in this article is exact; whether the four-dimensional Wilson-link formulation of the *matter* integral preserves the free two-point function to the same precision, and what its continuum limit is, is not shown.

## Summary

The coupled Klein–Gordon functional integral is the free one with the exponent's kinetic term covariantised, and its structure is the expansion of one squared modulus. The exponent splits into the free action, the current times the potential, and the potential squared, exactly and for every connection, the split checked to $6\times10^{-15}$. The third term carries the local invariance, so the coupling cannot be read as a current term alone.

The measure is flat and the local transformation is a rotation at each point, so it is invariant with no Jacobian; on a lattice the invariance is exact only for a link that carries the phase in an exponential, and the free determinant is reproduced to machine precision in that case and not in the linearised one. The Gaussian inverts the paired operator: for a purely vector connection that is the equation's operator and the shell is the free one at the shifted wave number, and for a scalar potential the two operators differ and the difference is the variational companion's recorded cross term, here at the pole.

The current is the first variation of the integral with respect to the connection, and its conservation is the differentiated invariance of the measure, so it holds in every correlation function. The two readings of the covariant square become a choice of measure: the centre inverts the scalar operator, and the curvature's vector part needs a measure that does not factorise. Everything else in the integral is central, and the coupling changes no object's type.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{2\pi iϙ}{h}\tilde A_\Phi$ | The covariant derivative; coefficients central |
| $c_{\imath}=\frac{2\pi iϙ}{h}A_{\imath}$ | The slot's coefficient; $c_t$ real and $c_{\imath}$ imaginary for a material connection |
| $S_{\mathrm{gco}}$ | The coupled matter action; the exponent's numerator |
| $\exp(\frac{2\pi iS_{\mathrm{gco}}}{h})$ | The weight; central, $*$-unitary, invariant under a local transformation |
| $S_0$ | The free action |
| $J_{\imath}=2\,\mathrm{Re}\,\mathrm{Sc}\bigl[i\tilde\Xi^{*}\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde\Xi\bigr]$ | The current; the coefficient of the exponent's linear term |
| $\sum_{\imath}\lvert c_{\imath}\rvert^{2}\lvert\Xi\rvert^{2}$ | The potential-squared term; no derivative |
| $\prod_x\mathrm{d}\Xi_1\mathrm{d}\Xi_2$ | The flat measure; invariant under a local phase |
| $U_j=e^{i(\Lambda_j-\Lambda_{j+1})}$ | The Wilson link; exact local invariance on the lattice |
| $\sum_{\imath}(\partial_{\imath}-\bar c_{\imath})(\partial_{\imath}+c_{\imath})-\nu_m^{2}$ | The paired operator; the Gaussian's inverse |
| $\Box_{\mathrm{gco},\Phi}=\sum_{\imath}\tilde\nabla_{\mathrm{gco},\Phi,\imath}^{2}$ | The equation's operator; the squared reading |
| $\bar c_{\imath}=-c_{\imath}$ | The condition for the two operators to coincide; holds for a vector connection |
| $\vec\kappa=2\pi\vec\nu_{\Phi}+\frac{ϙ}{h}\vec A$ | The shifted wave number; the shell for a purely vector connection |
| $\tilde F$ | The field strength; the vector part of the covariant square is $\frac{2\pi iϙ}{h}\xi\tilde F$ |
| $\nu_m=\frac{mc}{h}$ | The mass parameter |

## Further Reading

- [The Path Integral and the Klein–Gordon Equation in Biquaternionic Form](the-path-integral-and-the-klein-gordon-equation-in-biquaternionic-form.html), for the free functional integral, its Gaussian and its lattice regulator, all of which this article reuses.
- [The Lagrangian and the Coupled Klein–Gordon Equation](the-lagrangian-and-the-coupled-klein-gordon-equation.html), for the coupled action, its variation in the field and in the connection, and the recorded discrepancy in the temporal slot.
- [The Coupled Klein–Gordon Equation in Biquaternionic Form](the-coupled-klein-gordon-equation-in-biquaternionic-form.html), for the covariant square's split, the prohibition on central fields in a nonzero field strength, and the two readings.
- [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the amplitude and transport equations that the integral's saddles reproduce.
- [The Path Integral and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-path-integral-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the same integral read in the chart, where the local transformation is a translation of one coordinate.
- [The Minimal Coupling in Biquaternionic Form](the-minimal-coupling-in-biquaternionic-form.html), for the covariant derivative and the sign convention.
- [The Connection Path Integral in Biquaternionic Form](the-connection-path-integral-in-biquaternionic-form.html), for the integral over the connection, which this article holds fixed.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the lattice definition of a scalar functional integral and the role of the link variable.
- K. G. Wilson, "Confinement of Quarks", *Physical Review D* 10 (1974), 2445, for the lattice link variable and the exact local invariance it carries.
- S. Weinberg, *The Quantum Theory of Fields, Vol. II: Modern Applications* (Cambridge, 1996), for the background-field method and the Ward identities of an abelian connection theory.
