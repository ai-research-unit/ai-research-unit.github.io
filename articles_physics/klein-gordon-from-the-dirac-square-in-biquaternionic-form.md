# __Klein–Gordon from the Dirac Square in Biquaternionic Form__

## Introduction

The biquaternionic Dirac equation is first order. Its mass term is the central scalar $m$, and the equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

in which each member sets the gradient of one chiral half equal to $m$ times the other. The companion article *The Dirac Equation in Biquaternionic Form* records, in a single paragraph, that applying $\tilde{\nabla}^{\natural}$ to the first member and substituting the second gives $\Box\tilde{\Psi}_R = m^2\tilde{\Psi}_R$, so that each chiral component satisfies the Klein–Gordon equation. That paragraph is the hinge between the two halves of this category: it is where the relativistic quantum theory of spin $0$ and the relativistic quantum theory of spin $\tfrac12$ meet. This article reconstructs the passage in full, once in the algebra and once in the spinor module, settles what the passage carries and what it drops, and then runs the passage the other way, where the second chiral half turns out to be the gradient of the first.

Two operators carry the name *Dirac operator* in this corpus, and they are the two faces of one square. The **one-sided** operator is the gradient $\tilde\nabla$, which acts by left multiplication on the algebra, and the equations it obeys are the chiral pair above. The **two-sided** operator is the cell operator of the spinor module $(\mathbb{D}-m)\psi=0$, with

$$
\mathbb{D} = i\sum_\mu C_\mu\,\frac{\partial}{\partial x_\mu},
\qquad
C_\mu = iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},
\qquad
(x_t,x_x,x_y,x_z) = (ct',x,y,z),
$$

with $\nu(t) = x$ and $\nu(k) = y$ the reference frame, built from cells that multiply on the left and on the right at once; the chiral pair is its splitting by the chirality cell. Both readings reach the same central $\Box$, by two different mechanisms. In the algebra the square is the **product** $\tilde\nabla\tilde\nabla^{\natural}$, not $\tilde\nabla$ alone, and the **conjugate** cancels the cross terms; in the module $\mathbb{D}$ squares by itself, because the frame cells **anticommute**. The section *The Square in the Spinor Module* carries the second reading, and the Clifford names of the same cells are collected in *The Legacy Pauli Gamma Formulation*.

The question is sharp because the companion article on the Klein–Gordon equation asked the mirror-image question and returned a negative result. *The Klein–Gordon Equation in Biquaternionic Form* shows that $\Box - m^2c^2/\hbar^2$ has **no first-order scalar square root inside the algebra** $\mathbb{B}$: the first-order terms of a product $(\tilde\nabla^{\natural} + A)(\tilde\nabla + B)$ can be cancelled only with $B = -A$ and $A$ anticommuting with all three units $\vec e_x,\vec e_y,\vec e_z$, and no such element exists. If the Klein–Gordon operator has no scalar square root, how does a first-order equation — the Dirac pair — imply it? The answer, worked out below, is that the square root is **not scalar**: it is the gradient acting on the spinor module, and the mass term is off-diagonal between the two chiral halves. The scalar obstruction of the spin-$0$ article is exactly the evidence that the square root must be spinor-valued.

Three boundaries are respected. The Klein–Gordon **propagator** and the **scalar path integral** are the subject of the spin-$0$ companions and are not treated here. The d'Alembertian and its Green's functions are the subject of *The Biquaternion D'Alembertian and Its Green's Functions*, and the involution lattice is not reopened. What is treated here is the algebraic transfer from the first-order pair to the second-order equation, the kernel it produces, and the sense in which the transfer is irreversible.

Two conventions are load-bearing and are stated once. The d'Alembertian is the series convention,

$$
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta ,
$$

with $Q_t = ict'$, so that each time derivative carries the factor $(ic)^{-1} = -i/c$ when it is written in $t'$ and the time part is $-c^{-2}$ times the second derivative in $t'$. The imaginary unit satisfies $i^2 = -1$, and every product of two of them is reduced before a display is written: the collapse is what turns $(i\omega/c)^2$ into $-\omega^2/c^2$, what makes $i\,\mathrm{Sc}(\tilde P\tilde R^{\natural})$ a purely imaginary exponent whose exponential has unit modulus, and what turns the two $i$'s of each term of $\mathbb{D}$ into the minus sign that gives $\mathbb{D}^2 = \Box$. The mass parameter of the operator pair is measured in inverse-length units; restoring $\hbar$ and $c$, it is the inverse reduced Compton wavelength

$$
\mu = \frac{mc}{\hbar},
$$

so that the mass-shell condition reads $\tilde P\tilde P^{\natural} = -\mu^2$ and the second-order equation reads $(\Box - \mu^2)\tilde{\Phi} = 0$. In natural units $\hbar = c = 1$ the two symbols coincide, and the two are used below as one: a display that carries no $\hbar$ writes $m$, so the same second-order operator appears as $\Box - m^2$ in the algebra and as $\Box - \mu^2$ where the physical units are restored. This is the same parameter the Klein–Gordon article calls $\mu$, and the sign of $\Box$ is the series sign, the one *Exercise: Chirality and the Weyl Spinors* reaches from the two Weyl squares.

## The Gradient and Its Square

Left multiplication by $\tilde\nabla$ is the first-order operator, $\tilde\nabla^\natural$ is its conjugate, and the two products of the pair are the central scalar

$$
\tilde\nabla\tilde\nabla^\natural = \tilde\nabla^\natural\tilde\nabla = \Box .
$$

Neither equality is a square, and the distinction is the first thing the algebra contributes. Writing $\tilde\nabla = e_t\partial/\partial Q_t + \vec\nabla$,

$$
\tilde\nabla^2 = \left(\partial^2/\partial Q_t^2 - \lvert\vec\nabla\rvert^2\right)e_t + 2\,\partial/\partial Q_t\,\vec\nabla ,
\qquad \lvert\vec\nabla\rvert^2 = \Delta ,
$$

so $\tilde\nabla^2 \neq \Box$. The spacelike cross terms do cancel, because the three vector units anticommute pairwise and $\vec\nabla\vec\nabla = -\lvert\vec\nabla\rvert^2e_t$ has no vector remainder; the cross term between the timelike direction and the vector part does not, because the timelike direction is carried by the unit $e_t$, which commutes with every $\vec e_k$ instead of anticommuting with it. The conjugate removes that remainder: $\tilde\nabla^\natural$ enters with $-\vec\nabla$, the two mixed terms $-\partial/\partial Q_t\,\vec\nabla$ and $+\vec\nabla\,\partial/\partial Q_t$ cancel, and $\tilde\nabla\tilde\nabla^\natural$ reduces to $(\partial^2/\partial Q_t^2 + \lvert\vec\nabla\rvert^2)e_t$.

The conjugate is therefore the algebra's image of the Clifford anticommutator, and the root of $\Box$ inside the algebra is the pair $(\tilde\nabla,\tilde\nabla^\natural)$, never one gradient alone. No matrix, no Clifford generator and no frame enters the computation. A component check may choose a basis of $\mathbb{B}$ and write left multiplication as a $4\times4$ matrix; the matrix depends on the basis and the operator does not, and the reduction below stays with the operator.

## The Chiral Pair and the Two Reductions

The biquaternionic equation is not a single first-order equation in the algebra but the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

whose two members carry the two chiral halves. The reduction is a two-line computation. Apply $\tilde{\nabla}^{\natural}$ to the first member:

$$
\tilde{\nabla}^{\natural}\tilde{\nabla}\tilde{\Psi}_R = \tilde{\nabla}^{\natural}\!\left(m\tilde{\Psi}_L\right) = m\,\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m^2\tilde{\Psi}_R,
$$

where the middle equality uses that $m$ is a scalar and the last uses the second member. Since $\tilde{\nabla}^{\natural}\tilde{\nabla} = \Box$ is central,

$$
\boxed{\;\left(\Box - m^2\right)\tilde{\Psi}_R = 0\;}.
$$

Applying $\tilde{\nabla}$ to the second member instead gives the same statement for $\tilde{\Psi}_L$:

$$
\boxed{\;\left(\Box - m^2\right)\tilde{\Psi}_L = 0\;}.
$$

Three features of this reduction deserve to be named, because they are what the algebra contributes and not merely what it transcribes.

First, the reduction uses the **two different gradients**. It is the passage from $\tilde{\nabla}$ to $\tilde{\nabla}^{\natural}$ that produces a central scalar, as the previous section showed: $\tilde{\nabla}$ alone squares to a non-central element, and only the product $\tilde{\nabla}\tilde{\nabla}^{\natural}$ is central. The square of the Dirac pair is the biquaternion norm $\langle\tilde{\nabla}\rangle_{\natural} = \tilde{\nabla}\tilde{\nabla}^{\natural}$, exactly as $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ is the biquaternion norm of an element — the observation the Klein–Gordon article makes about its own operator.

Second, the reduction eliminates **both** members of the pair at once. It is not that one chiral half obeys Klein–Gordon and the other does not; the mass couples them, so that squaring forces each half onto the same second-order shell. A diagonal mass would leave two separate first-order equations, each of which squares to a mass term beside a non-central $\tilde\nabla^2$; the off-diagonal form is what puts $\tilde\nabla$ in one block and $\tilde\nabla^{\natural}$ in the other, so that the second member converts the first-order left-hand side into the central $\Box$.

Third, the reduction is **linear in the mass squared**. The second-order equation knows only $m^2$. It has no memory of the sign of $m$ and no memory of the chirality that carried it. That loss is the subject of *What the Square Carries and What It Does Not*.

## The Square in the Biquaternion Algebra

The gradient and its conjugate are

$$
\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z,
$$

$$
\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x - \vec e_y\partial/\partial Q_y - \vec e_z\partial/\partial Q_z .
$$

In cells the gradient is one-sided: $\tilde\nabla = \sum_\mu L_{e_\mu}^{\mathrm{axf}}\,\partial/\partial Q_\mu$, and $\tilde\nabla^{\natural} = L_{e_t}^{\mathrm{axf}}\,\partial/\partial Q_t - \sum_{k=x,y,z}L_{\vec e_k}^{\mathrm{axf}}\,\partial/\partial Q_k$. Cells compose by multiplying their elements, $L_aL_b = L_{ab}$, so the product of the two cells is the cell of the product, $L_{\tilde\nabla}L_{\tilde\nabla^{\natural}} = L_{\tilde\nabla\tilde\nabla^{\natural}} = L_{\Box}$, a scalar cell. One-sided cells suffice while only products of gradients are taken; two-sided cells enter when an operator holding both $\tilde\nabla$ and $\tilde\nabla^{\natural}$ at once has to be written without a conjugation, and that is the module reading below.

Their product is central and scalar:

$$
\tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \partial^2/\partial Q_x^2 + \partial^2/\partial Q_y^2 + \partial^2/\partial Q_z^2 = \Box .
$$

The cancellation of the mixed terms uses the quaternion multiplication table twice: the spacelike ones cancel because $\{\vec e_j,\vec e_k\} = 0$ for $j\neq k$, the timelike ones because the scalar part commutes with the vector part. This is why $\Box$ is scalar and central, and why it acts on a biquaternion field coefficient by coefficient,

$$
\Box\tilde{\Phi} = \sum_{\nu\in\{t,x,y,z\}}(\Box\Phi_\nu)\,e_\nu ,
$$

with no mixing of components. The spin-$0$ article records this as the reason its equation decouples into four complex scalars; here the same centrality is what lets the square of the Dirac pair produce a single second-order equation rather than a system.

The mass is a **central scalar** too: $m$ commutes with $\Box$ and with the chirality grading alike, and that is exactly why it passes through the gradient and lets the substitution above go through. Its off-diagonality is not a property of $m$ but of the pair: the mass multiplies within a chiral half, the gradient maps one half into the other, and it is that mismatch that makes the pair two coupled equations rather than two separate ones. Squaring moves the mass across one gradient, and because $m$ is central the two orders agree. What the square then loses is the block structure — which half the mass connects — not its value, which survives as $m^2$. In the algebra the reduction is therefore

$$
\tilde{\nabla}^{\natural}\!\left(\tilde{\nabla}\tilde{\Psi}_R\right) = \tilde{\nabla}^{\natural}\tilde{\nabla}\tilde{\Psi}_R = \Box\tilde{\Psi}_R ,
\qquad
m\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m^2\tilde{\Psi}_R ,
$$

and the equality of the two expressions is the equation $(\Box - m^2)\tilde{\Psi}_R = 0$. Nothing in this step uses a Clifford generator, a spinor index or the dimension of the module; it is the quaternion identity $\tilde\nabla\tilde\nabla^{\natural} = \Box$ applied to the pair.

### The Square in the Reduced Theory

The reduction to one spatial dimension isolates the mechanism without the bookkeeping of three. Take

$$
\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x, \qquad
\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x,
\qquad
\Box = \partial^2/\partial Q_t^2 + \partial^2/\partial Q_x^2 .
$$

The chiral pair retains its form and the reduction gives $(\Box - m^2)\tilde{\Psi}_{L,R} = 0$ exactly as before. The module is still the four-dimensional one, so the chirality cell $\Gamma = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ still splits it in two, and the mass couples the halves exactly as before. The plane-wave substitution gives $\tilde P = i\omega/c\,e_t + k\vec e_x$ and

$$
\tilde P\tilde P^{\natural} = -\omega^2/c^2 + k^2 = -\mu^2,
\qquad\text{hence}\qquad
\omega^2 = k^2c^2 + \mu^2c^2 ,
$$

the 1+1-dimensional dispersion. Everything the three-dimensional case does, the reduced case does with a single wave number, and the second-order operator is again central.

The reduced form is the one in which the **factorisation** is most visible. Writing the pair as two coupled first-order equations and eliminating one half produces a single second-order equation for the other; conversely, the second-order equation is recovered from the pair but the pair is not recovered from it. This is the setting in which the supersymmetric interpretation of the first-order operator becomes transparent, because the two halves of the pair are then the two components of a two-component object, with the mass as the two-by-two block $mI_2$ and the two gradients as the off-diagonal entries — the form *Supersymmetric Quantum Physics in the Biquaternion Framework* exploits.

## Why the Square Root Is Spinor-Valued

The companion article on the Klein–Gordon equation proves an obstruction that appears, at first sight, to contradict the reduction just performed. Its theorem is that the scalar operator $\Box - \mu^2$ does not factor into first-order **scalar** operators inside $\mathbb{B}$. For constant biquaternion coefficients,

$$
(\tilde{\nabla}^{\natural} + A)(\tilde{\nabla} + B)
= \Box + (A + B)\,\partial/\partial Q_t + \sum_{k=x,y,z}\left(A\vec e_k - \vec e_k B\right)\partial/\partial Q_k + AB,
$$

so cancelling the first-order terms requires $B = -A$ together with $A\vec e_k + \vec e_k A = 0$ for $k = x,y,z$. An element that anticommutes with all three quaternion units must vanish: the condition for $k = x$ removes the $e_t$ and $\vec e_x$ coefficients, and $k = y,z$ remove the rest. With $A = 0$ the constant term is $AB = -A^2 = 0$, which cannot equal $-\mu^2$ for $\mu\neq0$, and no scalar factorisation exists.

The two results are consistent, and their consistency is the whole point. The Dirac square root is **not** a scalar factor of the form $\tilde{\nabla} + A$ multiplying another scalar factor. It is an operator on the two chiral halves. With $\Psi = (\tilde{\Psi}_L,\tilde{\Psi}_R)^{\mathsf T}$, the pair is the single block equation

$$
\mathcal{D}_-\Psi = 0,
\qquad
\mathcal{D}_{\mp} = \begin{pmatrix} \mp m & \tilde{\nabla} \\ \tilde{\nabla}^{\natural} & \mp m\end{pmatrix},
$$

so that $\mathcal{D}_-$ is the pair and $\mathcal{D}_+$ its opposite-mass partner. *Operator and Calculus Conventions* writes the same pair as one operator on $\mathbb{B}\oplus\mathbb{B}$, $\mathbb{D}\Psi = (\tilde\nabla\tilde\Psi_R,\tilde\nabla^{\natural}\tilde\Psi_L)$, with $\mathbb{D}^2 = \Box\,I$ and the massive equation $(\mathbb{D} - m)\Psi = 0$; that $\mathbb{D}$ is the off-diagonal $\mathcal{Q}$ here, and $(\mathbb{D} - m)$ is $\mathcal{D}_-$. The letter $\mathbb{D}$ is kept in this article for the cell operator of the module, which is a different object on a different space. Because $m$ is central, the two blocks multiply cleanly:

$$
\boxed{\;\mathcal{D}_-\mathcal{D}_+
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

so the pair is the statement that $\Psi$ is an eigenvector of $\mathcal{Q}$ with eigenvalue $m$, and $\mathcal{Q}^2\Psi = m^2\Psi$ is $(\Box - m^2)\Psi = 0$. This is the operator-valued square root: no scalar $\tilde\nabla + A$ works, as the obstruction showed, but the matrix $\mathcal{Q}$ built from the conjugate pair does, because its square is the central $\Box\,I$; the opposite-mass product $\mathcal{D}_-\mathcal{D}_+$ is diagonal in the two chiral blocks with the central $(\Box - m^2)$ on each. The obstruction identifies precisely the missing ingredient: a scalar square root would need an element anticommuting with all three vector units $\vec e_k$, $k=x,y,z$, and no biquaternion does; an operator-valued square root needs only that the **two different gradients cancel each other's vector parts**, which the conjugate pair does. The spin-$0$ no-go and the spin-$\tfrac12$ square root are therefore one obstruction read two ways. This is what it means, in this framework, that the square root lives in the spinor module and not in the centre: the scalar field lives in $\mathbb{C}_{\mathbb{B}}$, and the square root requires the off-diagonal structure that only the module carries.

## The Square in the Spinor Module

The module reading is written in cells, because a cell is how the corpus states an operator that acts on one side or on both. Write $L_a$ and $R_b$ for the left and right multiplications, $L_a\psi = a\psi$ and $R_b\psi = \psi b$, so that $L_aR_b\psi = a\psi b$ and $L_aR_b\,L_cR_d = L_{ac}R_{db}$. The **frame cells** of the reference frame are

$$
C_t := iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}} = iR_{\vec e_x}^{\mathrm{axf}}, \qquad
C_k := iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\quad(k=x,y,z),
$$

with $\nu(t) = x$ and $\nu(k) = y$, and the identity on the four-dimensional module is $I_4 = L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, since $e_t = 1$. Each cell carries one factor of $i$, and every product of two cells carries $i^2 = -1$, so no display below ever carries a double $i$. The cells satisfy

$$
C_\mu C_\nu + C_\nu C_\mu = 2\varepsilon_\mu\delta_{\mu\nu}I_4,
\qquad
\varepsilon=(1,-1,-1,-1),
$$

so $C_t^2 = I_4$ and $C_k^2 = -I_4$. The cells are indexed by the coordinate labels, $\mu\in\{t,x,y,z\}$, so $C_t$ is the timelike cell and the other three are spatial. The timelike cell carries $R_{\vec e_x}^{\mathrm{axf}}$ and the spatial cells carry $R_{\vec e_y}^{\mathrm{axf}}$; those two units anticommute, and that is why $C_t$ anticommutes with each $C_k$.

The operator of the module, with the four physical coordinates $x_t = ct'$, $x_x = x$, $x_y = y$ and $x_z = z$, is

$$
\mathbb{D} := i\sum_\mu C_\mu\frac{\partial}{\partial x_\mu}
= -R_{\vec e_x}^{\mathrm{axf}}\frac{\partial}{\partial x_t} - \sum_k L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\frac{\partial}{\partial x_k},
\qquad
\mathbb{D}^2 = -\frac{\partial^2}{\partial x_t^2} + \Delta = \Box ,
$$

where the last equality uses $\partial/\partial Q_t = -i\,\partial/\partial x_t$, hence $\partial^2/\partial Q_t^2 = -\partial^2/\partial x_t^2$. The operator carries no imaginary unit at all: the explicit $i$ of $\mathbb{D}$ and the $i$ of each cell multiply to $-1$, and that collapse is what the right-hand side of the display shows. Kept with its single $i$, the contraction $\sum_\mu C_\mu\partial/\partial x_\mu$ squares to $-\Box$; with the second $i$ it squares to $\Box$.

In this reading no conjugate is needed for the square. The four cells anticommute pairwise, so the mixed terms of $\mathbb{D}^2$ cancel by the Clifford relation rather than by conjugation, and each cell squares to $\pm I_4$, so the square is scalar. The algebra and the module reach the same $\Box$ for different reasons: in the algebra the timelike unit $e_t$ commutes with the vector units, which leaves the mixed term of $\tilde\nabla^2$ alive and forces the conjugate; in the module the timelike cell anticommutes with the spacelike ones, and nothing is left to cancel. The two readings divide the labour: the algebra needs only the gradient and pays with a conjugation, the module needs the two-sided cells and pays with a frame.

**Chirality.** The chirality cell is

$$
\Gamma := -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
\qquad
\Gamma^2 = I_4,
\qquad
\{\Gamma,C_\mu\} = 0 \quad\text{for every }\mu ,
$$

the representative on the module of the central grading $\chi = i\tilde\Xi_{\mathrm{ad}}$ of the complexified algebra, outside $\mathbb{B}$ itself, with $\chi^2 = e_t$. Because $\Gamma$ anticommutes with every cell, it reverses the operator, $\Gamma\mathbb{D}\Gamma = -\mathbb{D}$: the two-sided Dirac operator is **chirality-odd**. Split a field by the chirality cell, $\psi = \psi_L + \psi_R$ with $\Gamma\psi_R = +\psi_R$ and $\Gamma\psi_L = -\psi_L$, the signs of the corpus projectors $P_{L,R} = \tfrac12(I_4\mp\Gamma)$. Then each half is carried to the other — $\mathbb{D}\psi_R$ lies in the left half and $\mathbb{D}\psi_L$ in the right — and the single equation $\mathbb{D}\psi = m\psi$ is the pair

$$
\mathbb{D}\psi_R = m\psi_L, \qquad \mathbb{D}\psi_L = m\psi_R .
$$

The mass term is chirality-blind — it is the scalar $m$, times $I_4$ — and it is exactly because $\mathbb{D}$ is odd and $m$ is even that the single equation links the halves at all: $\mathbb{D}\psi_R$ lands in the left half, where $m\psi_L$ also lives, and $\mathbb{D}\psi_L$ lands in the right half, where $m\psi_R$ lives. This is the precise content of the phrase *chirality-off-diagonal mass*: no matrix carries $m$ from one half to the other; the odd operator does the carrying, and the even mass, the same on both halves, is what the carried field is set equal to. It is also why the square forgets chirality: squaring the pair gives $\mathbb{D}^2 = \Box$ on each half separately, and $\Gamma\mathbb{D}^2\Gamma = \mathbb{D}^2$ is chirality-even.

**The two equations, side by side.** The name now covers two statements, and they must not be read as one. The **one-sided** equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

with two gradients, one for each chiral half, and no cell. The **two-sided** equation is the single equation

$$
\left(\mathbb{D} - m\right)\psi = 0,
$$

with one operator built from cells, and the chirality cell naming the halves. The second is the module form of the first: the cells supply the frame in which a single operator carries both gradients, the oddness of $\mathbb{D}$ under $\Gamma$ is what turns one equation into two, and the mass, even under $\Gamma$, is what couples them. The module identity

$$
\left(\mathbb{D} - m\right)\left(\mathbb{D} + m\right) = \mathbb{D}^2 - m^2 = \Box - m^2
$$

is the image of the block identity $\mathcal{D}_-\mathcal{D}_+ = (\Box - m^2)I$ of the previous section, and both are the statement that the mass enters the square squared.

## The Kernel and the Solution Space

Write the four-wavevector and the four-position as

$$
\tilde P = i\frac{\omega}{c}e_t + \vec k\in\mathbb{M}_-,
\qquad
\tilde{R} = ict'\,e_t + \vec x\in\mathbb{M}_-,
$$

with $\vec k = k_1\vec e_x + k_2\vec e_y + k_3\vec e_z$ and $\vec x = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$. Here $\vec k^2$ abbreviates the sum $k_1^2+k_2^2+k_3^2$ of the squares of the components, not the quaternion product, which is its negative, $\vec k\,\vec k = -\vec k^2e_t$. The phase is $\mathrm{Sc}(\tilde P\tilde{R}^{\natural}) = \vec k\cdot\vec x - \omega t'$, the scalar part of the product with the conjugate four-position. The exponent $i\,\mathrm{Sc}(\tilde P\tilde{R}^{\natural})$ is a purely imaginary central element, so the exponential is central and differentiates as an ordinary exponential. On a plane wave,

$$
\partial/\partial t' \longmapsto -i\omega, \qquad \partial/\partial x_k\longmapsto ik_k, \qquad \partial/\partial Q_t \longmapsto -\frac{\omega}{c},
$$

and therefore

$$
\tilde{\nabla} \longmapsto -\frac{\omega}{c}e_t + i\vec k, \qquad
\tilde{\nabla}^{\natural} \longmapsto -\frac{\omega}{c}e_t - i\vec k, \qquad
\Box \longmapsto \frac{\omega^2}{c^2} - \vec k^2 .
$$

The biquaternion norm of the wave biquaternion is

$$
\langle\tilde P\rangle_{\natural} = \tilde P\tilde P^{\natural} = \left(i\frac{\omega}{c}\right)^2 + k_1^2+k_2^2+k_3^2 = -\frac{\omega^2}{c^2} + \vec k^2 = -\Box ,
$$

the last equality holding on the plane wave, so the second-order equation $(\Box - \mu^2)\tilde{\Psi} = 0$ is the mass-shell condition

$$
\tilde P\tilde P^{\natural} = -\mu^2,
\qquad\text{equivalently}\qquad
\omega^2 = \vec k^2c^2 + \mu^2c^2,
$$

which is $E^2 = \vec p^2c^2 + m^2c^4$ under $E = \hbar\omega$, $\vec p = \hbar\vec k$ and $\mu = mc/\hbar$. The sign is the series sign and is consistent with the Klein–Gordon article: the operator $\Box - \mu^2$ vanishes on the same shell on which the biquaternion norm equals $-\mu^2$.

The kernel of the square is larger than the kernel of the pair, and the difference is the information the square discards. For a fixed three-momentum $\vec p$, a **scalar** field obeying the Klein–Gordon equation has a two-dimensional complex solution space, spanned by the positive- and negative-frequency modes $\exp(\mp i(Et'-\vec p\cdot\vec x))$. A **spinor-valued** field obeying the same second-order equation has one such pair for each of its four components, hence an eight-dimensional complex solution space at fixed $\vec p$, since $(\Box - \mu^2)$ acts on components without mixing them. The first-order equation selects a **four**-dimensional subspace: the two positive-frequency spinors $w^{(r)}(\vec p)$ times $\exp(-i(Et'-\vec p\cdot\vec x))$ and the two negative-frequency spinors $v^{(r)}(\vec p)$ times $\exp(+i(Et'-\vec p\cdot\vec x))$, with $r = 1,2$. Each of these four modes is annihilated by $\Box - \mu^2$, because that operator acts on each component separately and the plane wave is its eigenfunction, but the converse fails: a general second-order solution is a sum of **eight** independent modes with arbitrary coefficients, and the four linear relations $(\mathbb{D} - m)\psi = 0$ cut that space down to the four-dimensional first-order solution space. The square therefore has a kernel twice as large as the pair's; it is a necessary condition, not a sufficient one.

The same count can be read off the algebra. The square is the diagonal operator $(\Box - \mu^2)$ acting on the two chiral blocks, and it annihilates each block independently; the first-order pair is the off-diagonal operator set equal to $m\Psi$, which locks the two blocks together. The square forgets the lock, and the lost information is exactly the four linear relations that the lock imposes.

## The Massless Square and the Weyl Split

Setting $\mu = 0$ removes the coupling and separates the two halves:

$$
\tilde{\nabla}\tilde{\Psi}_R = 0, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = 0 .
$$

Each is a first-order equation whose conjugate product is the massless $\Box$, so each chirality separately obeys $\Box\tilde{\Psi} = 0$. The reduction, however, now carries no information: at $\mu = 0$ the pair is two independent first-order equations, and squaring either one loses the chirality that distinguished it from the other. This is the degenerate case of the general statement, and it is the biquaternion form of the standard fact that a massless Dirac field is two independent Weyl fields, each of which satisfies the massless Klein–Gordon equation. The spin-$0$ operator of that article, $\Box - \mu^2$, reduces at $\mu = 0$ to exactly the conjugate product of each Weyl operator, $\tilde\nabla\tilde\nabla^\natural = \tilde\nabla^\natural\tilde\nabla$.

The mass is therefore what makes the square **imply** the first-order equation rather than merely follow from it: at $\mu\neq0$ the two Weyl equations are coupled by the mass, the square of the coupled system is the single scalar operator $\Box - \mu^2$, and the first-order pair is recovered from the square only together with the chirality lock. At $\mu = 0$ there is no lock and no recovery; the square is strictly weaker.

## What the Square Carries and What It Does Not

The transfer from the first-order pair to the second-order equation can now be accounted for.

**Carried.** The mass shell, with the relativistic dispersion $E^2 = \vec p^2c^2 + m^2c^4$; the mass-squared coefficient of the second-order operator, produced by the off-diagonal coupling rather than inserted; the decoupling of the four coefficient fields, a consequence of the centrality of $\Box$; the chirality-oddness of the two-sided operator, $\Gamma\mathbb{D}\Gamma = -\mathbb{D}$, which is what makes it carry one chiral half into the other in the first-order equation; and the statement that both chiral halves obey the same second-order equation, which is the module identity $(\mathbb{D} - m)(\mathbb{D} + m) = \Box - m^2$.

**Not carried.** The sign of the mass, the chirality of each half, the spin label $r$, and the two linear relations per frequency branch that tie the large and small amplitudes together. The square is even in $m$ and chirality-blind; it cannot distinguish a solution of the pair from a second-order solution that violates the pair. The passage is therefore one-way: every solution of the first-order pair is a solution of the second-order equation, and not conversely.

**Not claimed.** The square does not turn the spin-$\tfrac12$ field into a spin-$0$ field. The Klein–Gordon equation is obeyed by each **component**, but the object that obeys it is spinor-valued: the reduction is a statement about the operator, not about the representation content. The genuine spin-$0$ field of the companion article lives in the centre $\mathbb{C}_{\mathbb{B}}$, where the Klein–Gordon equation is the whole of the dynamics; the spin-$\tfrac12$ field lives in the module, where the Klein–Gordon equation is the square's shadow and the first-order pair is the dynamics. The two share the operator and the mass shell, and nothing else. That is the precise sense in which this subcategory closes the loop to the spin-$0$ subcategory without absorbing it: the second-order equation is recovered, and what is recovered is exactly the part of the spin-$\tfrac12$ theory that the spin-$0$ theory already contained.

There is a final structural remark. The passage from the pair to the square is the passage from a **graded** operator to its diagonal. In the chiral block form of $\mathcal{D}_-$ the gradient sits off the diagonal — it maps one chirality to the other — while the mass sits on the diagonal, the same scalar in both blocks. The product $\mathcal{D}_-\mathcal{D}_+$ is diagonal, $(\Box - m^2)$ acting on each chirality separately, so the off-diagonal part is what has been traced out. That grading is the one the supersymmetric structure of the first-order operator exploits, and *Supersymmetric Quantum Physics in the Biquaternion Framework* develops it. The Klein–Gordon equation is the bosonic shadow of the fermionic square root; it is the diagonal of a matrix whose off-diagonal entries are the Dirac operator and its conjugate.

In the algebra the only identities used are $\tilde\nabla\tilde\nabla^\natural = \tilde\nabla^\natural\tilde\nabla = \Box$, which is exact, and the mass-shell condition $\tilde P\tilde P^{\natural} = -\mu^2$, which is the definition of the on-shell four-momentum; no matrix enters. The module reading uses one more, the Clifford relation $C_\mu C_\nu + C_\nu C_\mu = 2\varepsilon_\mu\delta_{\mu\nu}I_4$, which is the same cancellation written in the frame of the cells.

## The Converse Direction

*The Kernel and the Solution Space* measured what the square loses. The mirror question is what the **split** loses, and its answer is stronger: the second chiral half is a derivative of the first, and not independent data. Read the first member of the pair as a definition,

$$
\tilde\Psi_L := \frac{1}{m}\tilde\nabla\tilde\Psi_R ,
$$

and substitute it into the second member. The left-hand side becomes $\frac{1}{m}\tilde\nabla^{\natural}\tilde\nabla\tilde\Psi_R$, which is $\frac{1}{m}\Box\tilde\Psi_R$ because the product of the conjugate pair is the central scalar, so the second member reads

$$
\Box\tilde\Psi_R = m^2\tilde\Psi_R .
$$

The substitution is therefore exact in both directions:

$$
\begin{aligned}
&(\Box - m^2)\tilde\Psi_R = 0 \\
&\quad\Longleftrightarrow\quad
\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L,\qquad \tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R,
\qquad \tilde\Psi_L = \frac{1}{m}\tilde\nabla\tilde\Psi_R .
\end{aligned}
$$

Read left to right, a Klein–Gordon field generates a Dirac field. Read right to left, the first half of any Dirac field obeys Klein–Gordon. The map

$$
\tilde\Psi_R \longmapsto \left(\tilde\Psi_R,\ \frac{1}{m}\tilde\nabla\tilde\Psi_R\right)
$$

is $\mathbb{C}$-linear and injective and is onto the solution space of the pair, so the free Dirac solutions stand in bijection with the free Klein–Gordon solutions of **one chiral half**: the same data, described twice. The second member is not a second equation: it is what the definition of the second half turns into once the first half is on shell.

The device is older than this algebra. The two-component second-order form of the Dirac equation, with the other chiral half restored by differentiation, is Feynman and Gell-Mann's rewriting of the Dirac equation for the theory of the Fermi interaction. The algebra's contribution is not the device but the form it takes here: the restoring operator is the algebra's own gradient, and the exactness in both directions follows from the single identity $\tilde\nabla^{\natural}\tilde\nabla = \Box$.

Nothing in the display is a property of plane waves; the only identity used is $\tilde\nabla^{\natural}\tilde\nabla = \Box$, which is central. The equivalence was checked on plane waves at both frequency signs, with residual at the floating-point floor, and **off** the mass shell the same substitution leaves exactly

$$
\frac{1}{m}\tilde\nabla^{\natural}\tilde\nabla\tilde\Psi_R - m\tilde\Psi_R = \frac{1}{m}\left(\Box - m^2\right)\tilde\Psi_R ,
$$

which is the second member's defect, so the mass shell is the exact condition and not an approximation.

This does not contradict the one-way statement of *What the Square Carries and What It Does Not*. That statement is about the four-component field, of which the pair selects half of the second-order modes; the present one is about a single chiral half, of which the pair takes all. The counts agree in the module picture of *The Square in the Spinor Module*: at fixed momentum the pair has four complex dimensions, a two-component half times two frequency signs, and the Klein–Gordon solutions of one half have the same four. The eight of the four-component field are the two halves' fours, which is the halving that statement records. In the algebra picture every one of those numbers doubles, and nothing else changes.

### The Gradient as a Field Strength

If the first half is called a potential and the second a field strength, the pair says that the field is the derivative of the potential. The gradient alone suggests the redundancy such a description usually carries: if $\tilde\nabla\kappa = 0$, the potentials $\tilde\Psi_R$ and $\tilde\Psi_R + \kappa$ generate the same second half. The freedom does not survive the pair, and it is the mass shell that removes it. The condition $\tilde\nabla\kappa = 0$ is the massless Weyl equation, so $\kappa$ obeys $\Box\kappa = 0$ while the potential obeys $\Box\tilde\Psi_R = m^2\tilde\Psi_R$; the sum obeys neither, and the second member fails by exactly $m\kappa$. A potential off the mass shell generates no solution of the pair. In the two-term form there is therefore no redundancy to quotient out: the first half is physical data, and the pair fixes the whole field from it.

The four-scalar form of the same construction, in Kassandrov's treatment, does carry a genuine redundancy, and the difference is worth recording because it is where the phrase *the Dirac field is a gauge field* comes from. There the potential is a quadruple $\phi$ of Klein–Gordon scalars and the field is $\chi = D^*\phi$, with $D^* = i\gamma^\mu[\mathbb{M}_-]\partial/\partial x_\mu + m$ and $DD^* = \Box - m^2$ in the gamma frame of *The Legacy Pauli Gamma Formulation* below. Two potentials differing by $\kappa$ with $D^*\kappa = 0$ give the same field, and such a $\kappa$ is itself a Klein–Gordon solution, since $DD^*\kappa = 0$. The kernel of $D^*$ is the conjugate Dirac equation, which is the shape the electromagnetic case takes: there the potentials are defined up to $\partial\alpha$, the field is blind to it, and the gauge functions that survive the Lorenz condition are the ones with $\Box\alpha = 0$ — the same two-step structure, with the constraint on the gauge function carried by the field equation instead of by a subsidiary condition. The corpus keeps the two-term form, which is sharper, a doublet rather than a quadruple, and which has nothing to quotient out.

One step of the source's argument is not adopted. Kassandrov reads the construction as evidence that the spinor transformation law is not forced, taking the generating half to transform as a scalar doublet and the generated half then transforming nonlinearly. The corpus does not need that step and does not take it: the Lorentz action used here is the left action of the unit-norm biquaternions on the module, one action for every field, and a second realization on the components is a different theory of the transformation law rather than a consequence of the pair.

### The Static Yukawa Pair

Take the generator to be the Yukawa potential, the static spherically symmetric solution of the massive Klein–Gordon equation:

$$
\tilde\Psi_R = \frac{e^{-mr}}{r},
\qquad
r = \lvert\vec x\rvert .
$$

It solves the equation because $\Delta\left(e^{-mr}/r\right) = m^2e^{-mr}/r$ away from the origin, which was checked symbolically. The definition gives the second half in closed form:

$$
\tilde\Psi_L = \frac{1}{m}\vec\nabla\frac{e^{-mr}}{r}
= -\frac{(1+mr)\,e^{-mr}}{m r^3}\,\vec x ,
\qquad
\vec x = x\,\vec e_x + y\,\vec e_y + z\,\vec e_z ,
$$

and the pair is exact: the first member holds by construction and the second, $\tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R$, was checked symbolically term by term. Three features belong to the algebra.

- The generator lies in the **scalar slot** and the generated half in the **vector slots**: scalar in, pure vector out. The static condition is what removes the timelike term of the gradient and leaves the vector part alone.
- The singularity **rises by one power**, from $1/r$ to $1/r^2$ times a radial vector, and the profile $(1+mr)e^{-mr}$ is what the derivative of the Yukawa tail produces.
- The pair is **spherically symmetric**: the scalar slot is a function of $r$ alone and the vector slot is a radial vector, so a rotation of the argument is undone by the rotation of the vector slot. This is the corpus's form of the source's static spherically symmetric solution.

The two densities on this pair make the smallest illustration of the section, and the contrast is exact rather than approximate. The density of the pair is the sum of the Hermitian norms of its two halves, the extension to the pair of the identification the corpus's Dirac article makes between the Hermitian norm of a biquaternion field and the Dirac probability density:

$$
\rho^{(D)} = \langle\tilde\Psi_R\rangle_{*} + \langle\tilde\Psi_L\rangle_{*}
= \frac{e^{-2mr}}{r^2}\left(1 + \frac{(1+mr)^2}{m^2r^2}\right) > 0 ,
$$

positive everywhere, integrable at infinity, singular at the origin as $1/r^2$. Its companion is the Klein–Gordon density, and for this static configuration that one vanishes identically, because every term of it carries a time derivative. So the same pair carries a positive definite density and a density that is zero, and the pair of behaviours is what the corpus's forms separate: the Hermitian form $\langle\cdot\rangle_{*}$ is positive definite, while the quaternionic norm $\langle\cdot\rangle_{\natural}$ is the interval, indefinite and vanishing on the cone. The source writes the density as twice this one, its halves being two-component spinors rather than biquaternions. From the pair it draws the further conclusion that the Dirac field escapes Pauli's theorem on the sign of the energy density; the corpus records the two densities and does not adjudicate the theorem.

### What the Correspondence Does Not Give

1. **No new solutions, and no privileged half.** The bijection repackages the free solution space. It also does not make the first half the more fundamental object, because the split is symmetric: parity sends $\tilde\nabla$ to $\tilde\nabla^{\natural}$ and back, so if $(\tilde\Psi_R,\tilde\Psi_L)$ solves the pair then so does $(\tilde\Psi_L,\tilde\Psi_R)$ composed with $\vec x\mapsto-\vec x$, which was checked on the symbol of the pair at both frequency signs. Kassandrov records the same exchange in external fields, where the halves trade places for anti-self-dual backgrounds.
2. **It fails under minimal coupling.** With $\tilde\nabla\mapsto\tilde\nabla - ie\tilde A$ the two generalized gradients stop commuting, $\tilde\nabla^{\natural}_{gen}\tilde\nabla_{gen}\neq\tilde\nabla_{gen}\tilde\nabla^{\natural}_{gen}$, and what their commutator carries is the field strength; the product is then no longer the central scalar and the substitution no longer closes. A reduction survives only in a background whose complex field is (anti)self-dual, which is the boundary the hydrogen article meets in its own open questions.
3. **No physical content is added.** The distribution of the free modes over the mass shell, the spin labels, the chirality of each half: all unchanged. What the section adds is the sentence that can be said about the pair once it is read as one equation and one definition — the second half is the gradient of the first.

The source builds infinite chains of solutions by feeding the generated half back as a new generator. In the algebra each step is one more application of the definition, and the corpus records the mechanism without reproducing the chains in the source's 2+2 representation.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C}) = M_4(\mathbb{C})$, not a different algebra. They are the frame cells of the previous section under their Clifford names, together with their product:

$$
\gamma_0[\mathbb{M}_-] = C_t = iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1[\mathbb{M}_-] = C_x = iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2[\mathbb{M}_-] = C_y = iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3[\mathbb{M}_-] = C_z = iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-] = C_t = iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1[\mathbb{M}_-] = C_x = iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2[\mathbb{M}_-] = C_y = iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3[\mathbb{M}_-] = C_z = iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

$$
\gamma_5 = \Gamma = i\,C_tC_xC_yC_z = -iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

In the axis-free display:

$$
\gamma_5 = \Gamma = i\,C_tC_xC_yC_z = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

The volume cell is the product of the four, $C_tC_xC_yC_z = -L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$: the four $i$'s of the product reduce as $i^4 = +1$, so the product is a real cell, and the one further $i$ that turns it into $\gamma_5$ is the $i$ displayed.

A cell is a pure tensor, and the coefficient matrix $c(M)$ of an element $M$ in the basis of the sixteen products has rank at most four, so a general element is a sum of at most four cells; the cells alone are the cone $\operatorname{rank}c(M)\le1$, of dimension seven. The dictionary between the cell reading and the gamma reading is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities.** In the $\gamma$ reading, with the Clifford indices $\mu,\nu,\rho,\sigma\in\{0,1,2,3\}$ — the label $0$ is the timelike slot, the cell $C_t$ — and $\epsilon_{0123} = +1$,

$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\} = 2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
\gamma_0[\mathbb{M}_-]^2 = I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2 = -I_4,\qquad
\gamma_5^2 = I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\} = 0,
$$

$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]] = 2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\ \ (\mu\neq\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd} = \tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$

$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]) = 4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-]) = -4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
= 4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

The four contraction sums depend on the frame, because they involve $g_{\mu\mu}$. In the Euclidean frame, where every cell squares to $+I_4$ and $g = \delta$, each $\gamma$ in the sums is read as its Euclidean cell, $\gamma^E_0 = \gamma_0[\mathbb{M}_-]$ and $\gamma^E_k = i\gamma_k[\mathbb{M}_-]$, and they are

$$
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}] = 4I_4,
\qquad
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\mu[\mathbb{B}] = -2\gamma_\alpha[\mathbb{B}],
$$

$$
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\beta[\mathbb{B}]\gamma_\mu[\mathbb{B}] = 4\delta_{\alpha\beta}I_4,
\qquad
\sum_\mu\gamma_\mu[\mathbb{B}]\gamma_\alpha[\mathbb{B}]\gamma_\beta[\mathbb{B}]\gamma_\gamma[\mathbb{B}]\gamma_\mu[\mathbb{B}] = -2\gamma_\gamma[\mathbb{B}]\gamma_\beta[\mathbb{B}]\gamma_\alpha[\mathbb{B}] .
$$

In the $\mathbb{M}_-$ frame, with $\varepsilon=(1,-1,-1,-1)$, the signs of the cells enter: the first sum is $\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-] = -2I_4$, and the second is $\sum_\mu\gamma_\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-] = 2\left(1+g_{\alpha\alpha}\right)\gamma_\alpha[\mathbb{M}_-]$, which is $4\gamma_0[\mathbb{M}_-]$ for $\alpha = 0$ and vanishes for a spatial $\alpha$. The third and fourth are stated in the Euclidean frame only; in the $\mathbb{M}_-$ frame they do not take the Euclidean form with $g$ written for $\delta$. The body uses the anticommutator, the chirality cell and the volume element; the contraction sums are recorded for reference.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The biquaternionic Dirac equation is the first-order pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$. Applying $\tilde{\nabla}^{\natural}$ to the first member and substituting the second gives $\Box\tilde{\Psi}_R = m^2\tilde{\Psi}_R$, and symmetrically for $\tilde{\Psi}_L$; both chiral halves obey the Klein–Gordon equation $(\Box - m^2)\tilde{\Psi} = 0$ with the series d'Alembertian $\Box = \partial^2/\partial Q_t^2 + \Delta$, which in physical units is $(\Box - m^2c^2/\hbar^2)\tilde{\Psi} = 0$. The square is not the plain square: $\tilde\nabla^2 \neq \Box$, because the timelike unit $e_t$ commutes with the vector units and leaves the mixed term $2\,\partial/\partial Q_t\,\vec\nabla$, and it is the conjugate product $\tilde\nabla\tilde\nabla^\natural$ that cancels it. The conjugate is the algebra's image of the Clifford anticommutator.

On the spinor module the same square is written in cells. The frame cells $C_\mu = iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ satisfy $C_\mu C_\nu + C_\nu C_\mu = 2\varepsilon_\mu\delta_{\mu\nu}I_4$, each squares to $\pm I_4$, and the operator $\mathbb{D} = i\sum_\mu C_\mu\,\partial/\partial x_\mu$, with $(x_t,x_x,x_y,x_z) = (ct',x,y,z)$, squares to $\Box$ with no conjugate at all. Here the cancellation is carried by the anticommutation of the cells rather than by a conjugation, and every product of two $i$'s is reduced by $i^2 = -1$, so the operator carries no imaginary unit. The chirality cell $\Gamma = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} = i\,C_tC_xC_yC_z$ squares to $I_4$ and anticommutes with each $C_\mu$, so $\Gamma\mathbb{D}\Gamma = -\mathbb{D}$; the single two-sided equation $(\mathbb{D} - m)\psi = 0$ therefore splits by chirality into the pair, and $(\mathbb{D} - m)(\mathbb{D} + m) = \Box - m^2$.

The square root is not scalar. The companion article on the Klein–Gordon equation proves that $\Box - \mu^2$ has no first-order scalar factorisation in $\mathbb{B}$, because a scalar coefficient would have to anticommute with all three quaternion units and none does. The Dirac square root escapes the obstruction by being operator-valued and off-diagonal: it is the conjugate pair $(\tilde{\nabla},\tilde{\nabla}^{\natural})$ acting on the two chiral halves, coupled by the mass. Written as the block matrix $\mathcal{D}_\mp$ defined above, the operator identity is $\mathcal{D}_-\mathcal{D}_+ = (\Box - m^2)I$; written as $\mathcal{Q}\Psi = m\Psi$ with $\mathcal{Q}$ the off-diagonal part, it is $\mathcal{Q}^2 = \Box\,I$. The scalar no-go and the spinor square root are the same multiplication table seen from two sides.

The square carries the mass shell $\tilde P\tilde P^{\natural} = -\mu^2$, hence $E^2 = \vec p^2c^2 + m^2c^4$, and the mass-squared coefficient of the second-order operator; it does not carry the sign of the mass, the chirality of each half, or the four linear relations that select the first-order solution space from the larger second-order one. For fixed three-momentum the first-order equation has a four-dimensional complex solution space and the second-order equation an eight-dimensional one, so the square is a necessary and not a sufficient condition. The Klein–Gordon operator is the diagonal — the bosonic shadow — of a graded first-order object whose off-diagonal entries are the biquaternionic Dirac operator and its conjugate.

The converse holds exactly for the free pair. Read the first member as a definition, $\tilde\Psi_L = \frac{1}{m}\tilde\nabla\tilde\Psi_R$; the second member then becomes $(\Box - m^2)\tilde\Psi_R = 0$, so the free Dirac solutions stand in bijection with the free Klein–Gordon solutions of one chiral half, and the second half is the gradient of the first. In this two-term form there is no gauge freedom, because the only shift the gradient annihilates is the massless Weyl field, which takes the potential off the mass shell; the source's four-scalar form of the same construction does carry the residual gauge $\phi\mapsto\phi+\kappa$ with $D^*\kappa = 0$, and that is what earns the phrase *the Dirac field is a gauge field*. The correspondence is exact for the free field and stops at minimal coupling, where the commutator of the two generalized gradients is the field strength. Its smallest illustration is the static Yukawa pair, generator $e^{-mr}/r$ and second half $-(1+mr)e^{-mr}\vec x/(m r^3)$, on which the Dirac density is positive definite and the Klein–Gordon density vanishes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $L_a$, $R_b$, $L_aR_b$ | Left and right multiplication, $L_a\psi = a\psi$, $R_b\psi = \psi b$, and the two-sided cell $L_aR_b\psi = a\psi b$ |
| $C_\mu = iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ | Frame cells, $\mu\in\{t,x,y,z\}$, $\nu(t) = x$, $\nu(k) = y$; $C_t = iR_{\vec e_x}^{\mathrm{axf}}$ and $C_\mu C_\nu + C_\nu C_\mu = 2\varepsilon_\mu\delta_{\mu\nu}I_4$ |
| $I_4 = L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | Identity on the spinor module |
| $\mathbb{D} = i\sum_\mu C_\mu\,\partial/\partial x_\mu$ | Two-sided Dirac operator of the module, $(x_t,x_x,x_y,x_z) = (ct',x,y,z)$; $\mathbb{D}^2 = \Box$ |
| $\Gamma = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} = i\,C_tC_xC_yC_z$ | Chirality cell, $\Gamma^2 = I_4$, $\{\Gamma,C_\mu\} = 0$, $\Gamma\mathbb{D}\Gamma = -\mathbb{D}$ |
| $\chi = i\tilde\Xi_{\mathrm{ad}}$ | Central grading of the complexified algebra, $\chi^2 = e_t$, not an element of $\mathbb{B}$; represented by $\Gamma$ on the module |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ | Biquaternionic gradient (the one-sided Dirac operator) |
| $\tilde{\nabla}^{\natural}$ | Quaternion conjugate gradient |
| $\vec\nabla = \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ | Vector part of the gradient, $\lvert\vec\nabla\rvert^2 = \Delta$ |
| $\tilde{\nabla}^2 = \left(\partial^2/\partial Q_t^2 - \lvert\vec\nabla\rvert^2\right)e_t + 2\,\partial/\partial Q_t\,\vec\nabla$ | Square of the gradient alone; non-central, with a vector remainder |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta$ | d'Alembertian, series convention |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm |
| $\tilde P = i\omega/c\,e_t + \vec k$ | Four-wavevector, $\tilde P\tilde P^{\natural} = -\mu^2$ |
| $\tilde{R} = ict'\,e_t + \vec x$, with $\vec x = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Four-position, phase $\mathrm{Sc}(\tilde P\tilde{R}^{\natural}) = \vec k\cdot\vec x - \omega t'$ |
| $\mu = mc/\hbar$ | Mass parameter of the operator pair (inverse reduced Compton wavelength) |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | The one-sided pair; linear, chirality-off-diagonal mass |
| $\tilde\Psi_L = \frac{1}{m}\tilde\nabla\tilde\Psi_R$ | The second half as the gradient of the first; the pair's equivalent form, exact whenever $(\Box - m^2)\tilde\Psi_R = 0$ |
| $\langle\tilde{\Psi}\rangle_{*} = \sum_\mu\lvert\tilde{\Psi}_\mu\rvert^2$ | Hermitian norm of a field, positive definite; the Dirac density of the pair |
| $(\mathbb{D} - m)\psi = 0$ | The two-sided equation of the module |
| $\mathcal{D}_\mp = \begin{pmatrix} \mp m & \tilde{\nabla} \\ \tilde{\nabla}^{\natural} & \mp m\end{pmatrix}$ | The pair as a block matrix of gradients, $\mathcal{D}_-\mathcal{D}_+ = (\Box - m^2)I$ |
| $\mathcal{Q}$ | Off-diagonal part of $\mathcal{D}_\mp$, $\mathcal{Q}^2 = \Box\,I$, $\mathcal{Q}\Psi = m\Psi$ |
| $\Psi = (\tilde{\Psi}_L,\tilde{\Psi}_R)^{\mathsf T}$ | The chiral pair as a two-component object |
| $w^{(r)}(\vec p)$, $v^{(r)}(\vec p)$ | Positive- and negative-frequency spinors, $r = 1,2$ |
| $E^2 = \vec p^2c^2 + m^2c^4$ | Dispersion relation |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original first-order equation and its second-order consequence.
- O. Klein, "Elektrodynamik und Wellenmechanik vom Standpunkt des Korrespondenzprinzips," *Zeitschrift für Physik* **41** (1927) 407–442, and W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the second-order relativistic wave equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the first-order equation, its second-order square and the plane-wave spinors.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the square of the Dirac operator and the Weyl decomposition.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Clifford algebra and its representations, and the mass shell.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the even subalgebra, minimal left ideals, and the square root of the wave operator.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra interpretation of the Dirac operator and its square.
- S. S. Schweber, *An Introduction to Relativistic Quantum Field Theory* (Harper and Row, 1961), and A. I. Akhiezer and V. B. Berestetskii, *Quantum Electrodynamics* (Wiley, 1965), for the 2+2 split of the Dirac equation and the squared equation in an external field.
- V. V. Kassandrov, "Gauge origin of the Dirac field and singular solutions to the Dirac equation," arXiv:1706.08397 (2017), for the Klein–Gordon potentials of the free Dirac field, the reduction of the quadruple to a doublet, the residual gauge of the four-scalar form, and the singular chains generated by differentiation; the earlier presentation of the same construction is arXiv:0907.4736 (2009), where the differentiation chain $\chi_N = D^*P_N\cdots D^*P_1\chi$ with $P_i\in SL(4,\mathbb{C})$ is generated by matrices rather than by the potential gauge, and where the massive singular seed $\Phi = \mu\,e^{-imt}/r$ with $\mu = (x+iy)/(r+z)$ and its first Dirac descendant are displayed — a construction that stays on the potentials and has no image on the Dirac field itself, since $D^*P\kappa\neq0$ when $D^*\kappa = 0$. Its treatment of complexified external fields — the self-duality condition $\vec H = \pm i\vec E$, the reduction of the squared equation to the Klein–Gordon equation in the joint field of an electric charge and an imaginary magnetic monopole, the exchange of the two halves for anti-self-dual backgrounds, and the Coulomb ansatz $A_\varphi = i\Phi\tan(\theta/2)$ — is what open question 8 of the hydrogen article rests on.
- R. P. Feynman and M. Gell-Mann, "Theory of the Fermi interaction," *Physical Review* **109** (1958) 193–198, for the two-component second-order form of the Dirac equation, with the other chiral half restored by differentiation, the device §*The Converse Direction* carries into the algebra.
- R. P. Feynman, "Space-time approach to non-relativistic quantum mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the second-order wave equation as the square of a first-order operator in the path-integral setting.
