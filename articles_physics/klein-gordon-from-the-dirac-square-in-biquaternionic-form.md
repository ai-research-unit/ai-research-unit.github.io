# __Klein–Gordon from the Dirac Square in Biquaternionic Form__

## Introduction

The biquaternionic Dirac equation is first order. Its mass term is the linear, chirality-off-diagonal pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

and the companion article *The Dirac Equation in Biquaternionic Form* records, in a single paragraph, that applying $\tilde{\nabla}^{\natural}$ to the first member and substituting the second gives $\Box\tilde{\Psi}_R = m^2\tilde{\Psi}_R$, so that each chiral component satisfies the Klein–Gordon equation. That paragraph is the hinge between the two halves of this category: it is where the relativistic quantum theory of spin $0$ and the relativistic quantum theory of spin $\tfrac12$ meet. The present article is the door that hangs on that hinge. It reconstructs the passage in full — the square of the Dirac operator, in the spinor module and in the algebra — and it settles what the passage does and does not carry.

The question it answers is sharp because the companion article on the Klein–Gordon equation asked the mirror-image question and returned a negative result. *The Klein–Gordon Equation in Biquaternionic Form* showed that the second-order operator $\Box - m^2c^2/\hbar^2$ has **no first-order scalar square root inside the algebra** $\mathbb{B}$: the simplest attempt, $(\tilde{\nabla}^{\natural} + \mu)(\tilde{\nabla} - \mu)$, leaves the first-order residual $2\mu\vec\nabla$, with $\vec\nabla = \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ the vector part of the gradient, and with general constant biquaternion coefficients the residual $(A+B)\partial/\partial Q_t + \sum_\mu(A\vec e_\mu - \vec e_\mu B)\partial/\partial Q_\mu$ cannot be cancelled either, since cancellation would require an element anticommuting with all three $\vec e_\mu$ and none exists. If the Klein–Gordon operator has no first-order square root, how does a first-order equation — the Dirac pair — imply it? The answer, worked out below, is that the square root is **not scalar**: it is the gradient acting on the spinor module, and the mass term is off-diagonal between the two chiral halves. The scalar obstruction of the spin-$0$ article is exactly the evidence that the square root must be spinor-valued.

Three boundaries are respected. The Klein–Gordon **propagator** and the **scalar path integral** are the subject of the spin-$0$ companions and are not treated here. The d'Alembertian and its Green's functions are the subject of *the generalities*, and the involution lattice is not reopened. What is treated here is the algebraic transfer from the first-order pair to the second-order equation, the kernel it produces, and the sense in which the transfer is irreversible.

Two conventions are load-bearing and are stated once. The d'Alembertian is the series convention,

$$
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta = \Delta + \partial^2/\partial Q_t^2,
$$

with $\partial^2/\partial Q_t^2 = -c^{-2}\,\partial^2/\partial {t'}^2$. The mass parameter of the operator pair is measured in inverse-length units; restoring $\hbar$ and $c$, it is the inverse reduced Compton wavelength

$$
\mu = \frac{mc}{\hbar},
$$

so that the mass-shell condition reads $\tilde P\tilde P^{\natural} = -\mu^2$ and the second-order equation reads $(\Box - \mu^2)\tilde{\Phi} = 0$. In natural units $\hbar = c = 1$ the two symbols coincide and the corpus writes $m$ for both; where the distinction matters below, $\mu$ is written explicitly. This is the same parameter the Klein–Gordon article calls $\mu$, and the sign of $\Box$ is the series sign, not the opposite sign of *Exercise: Chirality and the Weyl Spinors*.

## The Gradient and Its Square

The reduction is carried out in the algebra. Left multiplication by $\tilde\nabla$ is the first-order operator, $\tilde\nabla^\natural$ is its conjugate, and the product is the central scalar
$$
\tilde\nabla\tilde\nabla^\natural=\tilde\nabla^\natural\tilde\nabla=\Box.
$$
No matrix, no Clifford generator and no frame enters the computation. A component check can be made by choosing a basis of $\mathbb{B}$ and writing left multiplication as a $4\times4$ matrix; the matrix depends on the basis, the operator does not. The reduction below stays with the operator.

## The Chiral Pair and the Two Reductions

The biquaternionic equation is not a single first-order equation in the algebra but the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

whose two members carry the two chiral halves. The reduction is a two-line computation. Apply $\tilde{\nabla}^{\natural}$ to the first member:

$$
\tilde{\nabla}^{\natural}\tilde{\nabla}\tilde{\Psi}_R = \tilde{\nabla}^{\natural}\!\left(m\tilde{\Psi}_L\right) = m\,\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m^2\tilde{\Psi}_R,
$$

where the middle equality uses that $m$ is a scalar and the last uses the second member. Since $\tilde{\nabla}^{\natural}\tilde{\nabla} = \Box$ is central, this is

$$
\boxed{\;\left(\Box - m^2\right)\tilde{\Psi}_R = 0\;}.
$$

Applying $\tilde{\nabla}$ to the second member instead gives the same statement for $\tilde{\Psi}_L$:

$$
\left(\Box - m^2\right)\tilde{\Psi}_L = 0 .
$$

Three features of this reduction deserve to be named, because they are what the algebra contributes and not merely what it transcribes.

First, the reduction uses the **two different gradients**. It is the passage from $\tilde{\nabla}$ to $\tilde{\nabla}^{\natural}$ — from the operator to its quaternion conjugate — that produces a central scalar. This is the algebraic content of the statement that a square root must be paired with its conjugate to square to a scalar: $\tilde{\nabla}$ alone squares to a non-central element, and it is the product $\tilde{\nabla}\tilde{\nabla}^{\natural}$ that is central; in the algebra that product is the concrete form of the anticommutator. The square is the biquaternion norm $\langle\tilde{\nabla}\rangle_{\natural} = \tilde{\nabla}\tilde{\nabla}^{\natural}$, exactly as $\tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ is the biquaternion norm of a biquaternion — the observation the Klein–Gordon article makes about its own operator.

Second, the reduction eliminates **both** members of the pair at once. It is not that one chiral half obeys Klein–Gordon and the other does not; the off-diagonal mass couples them so that squaring forces each half onto the same second-order shell. This is the biquaternion interpretation of the matrix statement that the mass term is off-diagonal: a diagonal mass term would square to a diagonal mass term, but the off-diagonal form is what makes the cross terms cancel between the two members and leaves the single central operator $\Box$.

Third, the reduction is **linear in the mass squared**. The second-order equation knows only $m^2$. It has no memory of the sign of $m$ and no memory of the chirality that carried it. That loss is the subject of the later section *What the Square Carries and What It Does Not*.

## The Square in the Biquaternion Algebra

The matrix reduction is the transcription of a purely biquaternionic statement, and it is worth writing the latter on its own. The gradient and its conjugate are

$$
\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z,
\qquad
\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x - \vec e_y\partial/\partial Q_y - \vec e_z\partial/\partial Q_z,
$$

and their product is central and scalar:

$$
\tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \partial^2/\partial Q_x^2 + \partial^2/\partial Q_y^2 + \partial^2/\partial Q_z^2 = \Box .
$$

The cancellation of the cross terms is the quaternion multiplication table: with $\vec\nabla = \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$ the vector part of the gradient, the two factors enter with opposite signs and $\vec\nabla\vec\nabla = -|\vec\nabla|^2 e_t$ has no vector remainder. This is why $\Box$ is scalar and central, and why it acts on a biquaternion field coefficient by coefficient,

$$
\Box\tilde{\Phi} = \sum_{\nu\in\{t,x,y,z\}}(\Box\Phi_\nu)\,e_\nu ,
$$

with no mixing of components. The spin-$0$ article records this as the reason its equation decouples into four complex scalars. Here the same centrality is what lets the square of the Dirac pair produce a single second-order equation rather than a system.

The mass term, by contrast, is **not central**: it is the off-diagonal coupling of the two chiral halves, the two central ideals of $\mathbb{B}\cong M_2(\mathbb{C})$. Because it is off-diagonal, it does not commute with the chirality but does commute with the central $\Box$; squaring the pair moves the mass across one gradient and leaves the central operator behind. In the algebra the reduction is therefore

$$
\tilde{\nabla}^{\natural}\!\left(\tilde{\nabla}\tilde{\Psi}_R\right) = \tilde{\nabla}^{\natural}\tilde{\nabla}\tilde{\Psi}_R = \Box\tilde{\Psi}_R
\quad\text{and}\quad
m\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m^2\tilde{\Psi}_R ,
$$

and the equality of the two expressions is the equation $(\Box - m^2)\tilde{\Psi}_R = 0$. Nothing in this step uses a gamma matrix, a spinor index, or a complex dimension count; it is the quaternion conjugation identity $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$ applied to the pair.

## Why the Square Root Is Spinor-Valued

The companion article on the Klein–Gordon equation proves an obstruction that appears, at first sight, to contradict the reduction just performed. Its theorem is that the scalar operator $\Box - \mu^2$ does not factor into first-order **scalar** operators inside $\mathbb{B}$. The proof is one line of the multiplication table. For constant biquaternion coefficients,

$$
(\tilde{\nabla}^{\natural} + A)(\tilde{\nabla} + B)
= \Box + (A+B)\partial/\partial Q_t + \sum_{\mu=1}^{3}\left(A\vec e_\mu - \vec e_\mu B\right)\partial/\partial Q_\mu + AB,
$$

so cancelling the first-order terms requires $B = -A$ together with $A\vec e_\mu + \vec e_\mu A = 0$ for $\mu = x,y,z$. An element anticommuting with all three quaternion units must vanish — the condition for $\mu=x$ removes the $e_t$ and $\vec e_x$ coefficients, and $\mu = y,z$ remove the rest — whereupon $AB = -A^2 = 0$, which cannot equal $-\mu^2$ for $\mu\neq0$.

The two results are consistent, and their consistency is the whole point. The Dirac square root is **not** a scalar factor of the form $\tilde{\nabla} + A$ multiplying another scalar factor. It is an operator on the two chiral halves. Write the pair, with $\Psi = (\tilde{\Psi}_L,\tilde{\Psi}_R)^{\mathsf T}$, as

$$
\mathbb{D}_\mp = \begin{pmatrix} \mp m & \tilde{\nabla} \\ \tilde{\nabla}^{\natural} & \mp m\end{pmatrix},
\qquad
\mathbb{D}_-\Psi = 0 ,
$$

so that $\mathbb{D}_-$ is the Dirac pair and $\mathbb{D}_+$ its opposite-mass partner. Because $m$ is central — it commutes with $\tilde{\nabla}$ and with $\tilde{\nabla}^{\natural}$ — the two matrices multiply cleanly:

$$
\boxed{\;\mathbb{D}_-\mathbb{D}_+
= \begin{pmatrix} -m & \tilde{\nabla} \\ \tilde{\nabla}^{\natural} & -m\end{pmatrix}
\begin{pmatrix} m & \tilde{\nabla} \\ \tilde{\nabla}^{\natural} & m\end{pmatrix}
= \begin{pmatrix} \Box - m^2 & 0 \\ 0 & \Box - m^2\end{pmatrix}
= \left(\Box - m^2\right)I\;},
$$

the off-diagonal entries cancelling because the mass passes through the gradients.

Equivalently, with $\mathcal{Q}$ the off-diagonal part alone,

$$
\mathcal{Q} = \begin{pmatrix} 0 & \tilde{\nabla} \\ \tilde{\nabla}^{\natural} & 0\end{pmatrix},
\qquad
\mathcal{Q}^2 = \Box\,I,
\qquad
\mathcal{Q}\Psi = m\Psi ,
$$

so that the pair is the statement that $\Psi$ is an eigenvector of $\mathcal{Q}$ with eigenvalue $m$, and $\mathcal{Q}^2\Psi = m^2\Psi$ is $(\Box - m^2)\Psi = 0$. This is the operator-valued square root: no scalar $(\tilde{\nabla} + A)$ works, as the previous section showed, but the matrix $\mathcal{Q}$ built from the conjugate pair does, because its square is the central $\Box\,I$; the opposite-mass product $\mathbb{D}_-\mathbb{D}_+$ is diagonal in the two chiral blocks with the central $(\Box - m^2)$ on each. The obstruction of the spin-$0$ article identifies precisely the missing ingredient: a scalar square root would need an element anticommuting with all three $\vec e_\mu$, and no biquaternion does; but an operator-valued square root needs only that the **two different gradients cancel each other's vector parts**, which the conjugate pair does. The spin-$0$ no-go and the spin-$\tfrac12$ square root are therefore the same fact read in two directions. This is what it means, in this framework, that the square root lives in the spinor module and not in the centre: the scalar field lives in $\mathbb{C}_{\mathbb{B}}$, and the square root requires the off-diagonal structure that only the module carries.

It is worth recording the matrix counterpart, because it isolates the same mechanism. In the Clifford algebra the square of the Dirac operator is scalar because the generators **anticommute** — the cross term is $\tfrac12\{\gamma_\mu,\gamma_\nu\}\partial^2/\partial Q_\mu\partial Q_\nu$ and the symmetric part survives while the antisymmetric part cancels. In the biquaternion algebra the three vector units do anticommute pairwise, $\{\vec e_\mu,\vec e_\nu\} = 0$ for $\mu\neq\nu$, so the purely spacelike cross terms cancel just as in the Clifford algebra and $\vec\nabla\vec\nabla = -|\vec\nabla|^2e_t$ has no vector part. What does not cancel is the cross term between the timelike direction and the vector part, because the timelike direction is carried by the algebra's unit $e_t$, which **commutes** with every $\vec e_\mu$ instead of anticommuting with it. Hence
$$
\tilde{\nabla}^2 = \left(\partial^2/\partial Q_t^2 - |\vec\nabla|^2\right)e_t + 2\partial/\partial Q_t\,\vec\nabla ,
$$
with the vector remainder $2\partial/\partial Q_t\,\vec\nabla$. The conjugate removes that remainder: writing $\tilde{\nabla} = \partial/\partial Q_t\,e_t + \vec\nabla$ and $\tilde{\nabla}^{\natural} = \partial/\partial Q_t\,e_t - \vec\nabla$, the product $\tilde{\nabla}\tilde{\nabla}^{\natural}$ contains the two cross terms $-\partial/\partial Q_t\,\vec\nabla$ and $+\vec\nabla\,\partial/\partial Q_t$, which cancel because the scalar and vector parts commute, leaving $\partial^2/\partial Q_t^2\,e_t - \vec\nabla\vec\nabla = (\partial^2/\partial Q_t^2 + |\vec\nabla|^2)e_t = \Box$. The conjugate is the algebra's image of the Clifford anticommutator, and it is why the correct algebraic statement is $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$ rather than $\tilde{\nabla}^2 = \Box$.

### The Square in the Reduced Theory

The reduction to one spatial dimension isolates the mechanism without the bookkeeping of three. Take

$$
\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x, \qquad
\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x,
\qquad
\Box = \partial^2/\partial Q_t^2 + \partial^2/\partial Q_x^2 .
$$

The chiral pair retains its form, and the reduction gives $(\Box - m^2)\tilde{\Psi}_{L,R} = 0$ exactly as before. The two-dimensional spinor module has the two chiral halves as its two one-dimensional factors, and the mass is again the off-diagonal coupling. The plane-wave substitution now gives $\tilde P = i\omega/c\,e_t + k \vec e_x$, $\tilde P\tilde P^{\natural} = -\omega^2/c^2 + k^2 = -\mu^2$, hence the 1+1-dimensional dispersion $\omega^2 = k^2c^2 + \mu^2c^2$. Everything the three-dimensional case does, the reduced case does with a single wave number, and the second-order operator is again central.

The reduced form is the one in which the **factorisation** is most visible. Writing the chiral pair as two coupled first-order equations and eliminating one half produces a single second-order equation for the other; conversely, the second-order equation can be recovered from the pair but not the pair from it. This is the setting in which the supersymmetric interpretation of the first-order operator becomes transparent, because the two halves of the pair are then the two components of a two-component object and the off-diagonal mass is a two-by-two matrix, which the companion article on supersymmetric quantum physics exploits.

## The Kernel and the Solution Space

The square is now applied to the plane waves of the series. Write the four-wavevector and the four-position as

$$
\tilde P = i\frac{\omega}{c}e_t + \vec k\in\mathbb{M}_-,
\qquad
\tilde{R} = ict'\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z\in\mathbb{M}_-,
\qquad \vec k = k_1\vec e_x + k_2\vec e_y + k_3\vec e_z,
$$

and take the phase $\mathrm{Sc}(\tilde P\tilde{R}^{\natural}) = -\omega t' + \vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, the scalar part of the product with the conjugate four-position. The exponent $i\,\mathrm{Sc}(\tilde P\tilde{R}^{\natural})$ is a purely imaginary central element, so the exponential is central and differentiates as an ordinary exponential. On a plane wave,

$$
\partial/\partial t' \longmapsto -i\omega, \qquad \partial/\partial x_j\longmapsto ik_j, \qquad \partial/\partial Q_t \longmapsto -\frac{\omega}{c},
$$

and therefore

$$
\tilde{\nabla} \longmapsto -\frac{\omega}{c}e_t + i\vec k, \qquad
\tilde{\nabla}^{\natural} \longmapsto -\frac{\omega}{c}e_t - i\vec k, \qquad
\Box \longmapsto \frac{\omega^2}{c^2} - \vec k^2 .
$$

The biquaternion norm of the wave biquaternion is

$$
\langle\tilde P\rangle_{\natural} = \tilde P\tilde P^{\natural} = \left(i\frac{\omega}{c}\right)^2 + \vec k^2 = -\frac{\omega^2}{c^2} + \vec k^2 = -\Box ,
$$

the last equality holding on the plane wave, so the second-order equation $(\Box - \mu^2)\tilde{\Psi} = 0$ is the mass-shell condition

$$
\tilde P\tilde P^{\natural} = -\mu^2,
\qquad\text{equivalently}\qquad
\omega^2 = \vec k^2c^2 + \mu^2c^2,
$$

which is $E^2 = \vec p^2c^2 + m^2c^4$ under $E = \hbar\omega$, $\vec p = \hbar\vec k$ and $\mu = mc/\hbar$. The sign is the series sign and is consistent with the Klein–Gordon article: the operator $\Box - \mu^2$ vanishes on the same shell on which the biquaternion norm equals $-\mu^2$.

The kernel of the square is larger than the kernel of the pair, and the difference is the information the square discards. For a fixed three-momentum $\vec p$, a **scalar** field obeying the Klein–Gordon equation has a two-dimensional complex solution space, spanned by the positive- and negative-frequency modes $\exp(\mp i(Et'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)))$. A **spinor-valued** field obeying the same second-order equation has one such pair for each of its four components, hence an eight-dimensional complex solution space at fixed $\vec p$, since $(\Box - \mu^2)$ acts on components without mixing them. The first-order Dirac equation selects a **four**-dimensional subspace of it: the two positive-frequency spinors $w^{(r)}(\vec p)\exp(-i(Et'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)))$ and the two negative-frequency spinors $v^{(r)}(\vec p)\exp(+i(Et'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)))$, with $r = 1,2$. Every one of the four is annihilated by $\Box - \mu^2$ — this was checked componentwise on a superposition of two plane waves — but the converse fails: a general second-order solution is a sum of **eight** independent modes with arbitrary coefficients, and the four linear relations $(\mathbb{D} - m)\psi = 0$ cut that space down to the four-dimensional first-order solution space. The square therefore has a kernel twice as large as the pair's; it is a necessary condition, not a sufficient one.

The same count can be read off the algebra. The square is the diagonal operator $(\Box - \mu^2)$ acting on the two chiral blocks, and it annihilates each block independently; the first-order pair is the off-diagonal operator that locks the two blocks together through the mass. The square forgets the lock, and the lost information is exactly the four linear relations that the lock imposes.

## The Massless Square and the Weyl Split

Setting $\mu = 0$ removes the coupling and separates the two halves:

$$
\tilde{\nabla}\tilde{\Psi}_R = 0, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = 0 .
$$

Each is a first-order equation whose square is the massless $\Box$, so each chirality separately obeys $\Box\tilde{\Psi} = 0$. The reduction, however, now carries no information: at $\mu = 0$ the pair is two independent first-order equations, and squaring either one loses the chirality that distinguished it from the other. This is the degenerate case of the general statement, and it is the biquaternion form of the standard fact that a massless Dirac field is two independent Weyl fields, each of which satisfies the massless Klein–Gordon equation. The spin-$0$ article's operator is exactly the square of each Weyl operator.

The mass is therefore what makes the square **imply** the first-order equation rather than merely follow from it: at $\mu\neq0$ the two Weyl equations are coupled by the off-diagonal mass, the square of the coupled system is the single scalar operator $\Box - \mu^2$, and the first-order pair is recovered from the square only together with the chirality lock. At $\mu = 0$ there is no lock and no recovery; the square is strictly weaker.

## What the Square Carries and What It Does Not

The transfer from the first-order pair to the second-order equation can now be accounted for.

**Carried.** The mass shell, with the correct relativistic dispersion $E^2 = \vec p^2c^2 + m^2c^4$; the mass-squared coefficient of the second-order operator, produced by the off-diagonal coupling rather than inserted; the decoupling of the four coefficient fields, a consequence of the centrality of $\Box$; and the statement that both chiral halves obey the same second-order equation, which is the biquaternion form of the operator identity $(\mathbb{D} + m)(\mathbb{D} - m) = \Box - m^2$.

**Not carried.** The sign of the mass, the chirality of each half, the spin label $r$, and the two linear relations per frequency branch that tie the large and small amplitudes together. The square is even in $m$ and diagonal in chirality-blind language; it cannot distinguish a solution of the pair from a second-order solution that violates the pair. The passage is therefore one-way: every solution of the first-order pair is a solution of the second-order equation, and not conversely.

**Not claimed.** The square does not turn the spin-$\tfrac12$ field into a spin-$0$ field. The Klein–Gordon equation is obeyed by each **component**, but the object that obeys it is spinor-valued: the reduction is a statement about the operator, not about the representation content. The genuine spin-$0$ field of the companion article lives in the centre $\mathbb{C}_{\mathbb{B}}$, where the Klein–Gordon equation is the whole of the dynamics; the spin-$\tfrac12$ field lives in the module, where the Klein–Gordon equation is the square's shadow and the first-order pair is the dynamics. The two share the operator and the mass shell, and nothing else. That is the precise sense in which this subcategory closes the loop to the spin-$0$ subcategory without absorbing it: the second-order equation is recovered, and what is recovered is exactly the part of the spin-$\tfrac12$ theory that the spin-$0$ theory already contained.

There is a final structural remark. The passage from the pair to the square is the passage from a **graded** object to its diagonal. The first-order pair is off-diagonal in the chirality grading — the mass maps $L$ to $R$ and back — while the square is diagonal, $(\Box - m^2)$ acting on each chirality separately. The grading is what the square erases, and it is the same grading that the supersymmetric structure of the first-order operator exploits, which the companion article on supersymmetric quantum physics develops. The Klein–Gordon equation is the bosonic shadow of the fermionic square root; it is the diagonal of a matrix whose off-diagonal entries are the Dirac operator and its conjugate.

The only identities used above are $\tilde\nabla\tilde\nabla^\natural=\tilde\nabla^\natural\tilde\nabla=\Box$, which is exact, and the mass-shell condition $\tilde P\tilde P^\natural=-m^2c^2/\hbar^2$, which is the definition of the on-shell four-momentum. No matrix identity enters the reduction.

## Summary

The biquaternionic Dirac equation is the first-order pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$. Applying $\tilde{\nabla}^{\natural}$ to the first member and substituting the second gives $\Box\tilde{\Psi}_R = m^2\tilde{\Psi}_R$, and symmetrically for $\tilde{\Psi}_L$; both chiral halves obey the Klein–Gordon equation $(\Box - m^2c^2/\hbar^2)\tilde{\Psi} = 0$ with the series d'Alembertian. In the spinor module it is the corresponding two-line computation on the representative. The matrix identity $(\gamma_{\mu}(Q)\partial/\partial Q_\mu + m)(\gamma_{\nu}(Q)\partial/\partial Q_\nu - m)=\Box-m^2$ holds in the all-plus $\mathbb{B}$ frame, where $(\gamma_{\mu}(Q)\partial/\partial Q_\mu)^2=\Box$; it does not hold for the contraction of the $\mathbb{M}_-$ frame.

The square root is not scalar. The companion article on the Klein–Gordon equation proves that $\Box - \mu^2$ has no first-order scalar factorisation in $\mathbb{B}$, because a scalar coefficient would have to anticommute with all three quaternion units and none does. The Dirac square root escapes the obstruction by being operator-valued and off-diagonal: it is the conjugate pair $(\tilde{\nabla},\tilde{\nabla}^{\natural})$ acting on the two chiral halves, coupled by the mass, and the pairing is the algebra's image of the Clifford anticommutator. Written as the matrix $\mathbb{D}_\mp$ defined above, the operator identity is $\mathbb{D}_-\mathbb{D}_+ = (\Box - m^2)I$; written as $\mathcal{Q}\Psi = m\Psi$ with $\mathcal{Q}$ the off-diagonal part, the square is the operator identity $\mathcal{Q}^2 = \Box\,I$. The scalar no-go and the spinor square root are the same multiplication table read in two directions.

The square carries the mass shell $\tilde P\tilde P^{\natural} = -\mu^2$, hence $E^2 = \vec p^2c^2 + m^2c^4$, and the mass-squared coefficient of the second-order operator; it does not carry the sign of the mass, the chirality of each half, or the four linear relations that select the first-order solution space from the larger second-order one. For fixed three-momentum the first-order equation has a four-dimensional complex solution space and the second-order equation a strictly larger one, so the square is a necessary and not a sufficient condition. The Klein–Gordon operator is the diagonal — the bosonic shadow — of a graded first-order object whose off-diagonal entries are the biquaternionic Dirac operator and its conjugate.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ | Biquaternionic gradient (the Dirac operator) |
| $\tilde{\nabla}^{\natural}$ | Quaternion conjugate gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta$ | d'Alembertian, series convention |
| $\tilde P = i\omega/c\,e_t + \vec k$, $\tilde{R} = ict'\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Four-wavevector and four-position |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm |
| $\tilde P\tilde P^{\natural} = -m^2c^2/\hbar^2$ | Mass-shell condition |
| $\mu = mc/\hbar$ | Mass parameter of the operator pair (inverse reduced Compton wavelength) |
| $\mathbb{D}$ | First-order pair operator, $\mathbb{D}^2=\Box$ |
| $\vec\nabla = \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ | Vector part of the biquaternionic gradient |
| $\tilde{\nabla}^2 = \left(\partial^2/\partial Q_t^2 - |\vec\nabla|^2\right)e_t + 2\partial/\partial Q_t\,\vec\nabla$ | Square of the gradient alone; non-central, with a vector remainder |
| $\mathbb{D}_\mp$ | The Dirac pair as a $2\times2$ matrix of gradients, $\mathbb{D}_-\mathbb{D}_+ = (\Box - m^2)I$ |
| $\Psi = (\tilde{\Psi}_L,\tilde{\Psi}_R)^{\mathsf T}$ | The chiral pair as a two-component object, $\mathcal{Q}\Psi = m\Psi$ |
| $\mathcal{Q}$ | Off-diagonal part of $\mathbb{D}_\mp$; $\mathcal{Q}^2 = \Box\,I$ |
| $(\tilde{\nabla}\tilde{\nabla}^{\natural} - m^2) = \Box - m^2$ | The square in the algebra |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Linear, chirality-off-diagonal mass pair |
| $w^{(r)}(\vec p)$, $v^{(r)}(\vec p)$ | Positive- and negative-frequency spinors |
| $E^2 = \vec p^2c^2 + m^2c^4$ | Dispersion relation |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original first-order equation and its second-order consequence.
- O. Klein, "Elektrodynamik und Wellenmechanik vom Standpunkt des Korrespondenzprinzips," *Zeitschrift für Physik* **41** (1927) 407–442, and W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the second-order relativistic wave equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the first-order equation, its second-order square and the plane-wave spinors.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the square of the Dirac operator and the Weyl decomposition.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Clifford algebra, the gamma matrices, and the mass shell.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the even subalgebra, minimal left ideals, and the square root of the wave operator.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra interpretation of the Dirac operator and its square.
- R. P. Feynman, "Space-time approach to non-relativistic quantum mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the second-order wave equation as the square of a first-order operator in the path-integral setting.
